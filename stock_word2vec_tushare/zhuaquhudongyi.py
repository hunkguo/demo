# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4  import BeautifulSoup
import re
import datetime
import pandas as pd
import jieba.analyse
import MySQLdb as mdb
import requests
from bs4 import BeautifulSoup
import bs4

chrome_options = webdriver.chrome.options.Options();
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

def main():
    #0.0 时间初始化
    today = datetime.datetime.now().date();
    tradedays=get_tradecalendar(today);
    if today not in tradedays:
        lastday = tradedays[-1]
    else:
        lastday=tradedays[tradedays.index(today)-1]

    ##1.0 读取800成分股
    members_800=get_index800(today);
    h=0;
    print 'crawler start'
    ##上证e互动 和 深交所互动易
    Failed_reading=[];Data=pd.DataFrame([]);j=0
    for i in members_800:
        code=i[0:6];        exchange=i[7:];
        h=h+1;print h,code
        if exchange=='SH':
            try:
                x=get_ask_from_SHExchange(code,lastday,today)
                if len(x) == 0:
                    continue
                else:
                    x['code'] = i;
                    Data = Data.append(x)
            except :
                Failed_reading.append(i)

        elif exchange=="SZ":
            x=get_ask_from_SZExchange(code,lastday,today);
            if len(x)==0:
                continue
            else:
                x['code']=i;
                Data = Data.append(x)
        else:
            continue;
    Data.index=range(len(Data.index))
    Data.to_csv('comments_'+today.strftime("%Y%m%d")+'.xls',index=False,encoding='utf-8_sig')
    print 'failed reading:', Failed_reading

def main1():
    today = datetime.datetime.now().date();
    tradedays = get_tradecalendar(today);
    if today not in tradedays:
        today=tradedays[-1];
    lastday = tradedays[tradedays.index(today) - 1]
    print     get_ask_from_SHExchange('600000',lastday,today)

###读取上交所评论
def get_ask_from_SHExchange(code,yesterday,today):
    # driver = webdriver.Chrome()

    driver.get("http://sns.sseinfo.com")
    # 搜索code
    driver.find_element_by_id("com_search_txt").send_keys(code)
    driver.find_element_by_id("to_companyByCode").click()
    time.sleep(1)
    # 点击“最新提问
    driver.find_element_by_link_text('最新提问').click()
    time.sleep(1)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, features='lxml')
    Tem = []
    for i in soup.find_all('div', attrs={'class': "m_feed_item m_question"}):
        soup_i = BeautifulSoup(str(i), features='lxml')
        question = soup_i.find('div', {'class': 'm_feed_txt'}).a.nextSibling.strip()
        webtime = soup_i.find('div', {'class': 'm_feed_from'}).span.string.strip()
        if '昨天' in webtime:  ### 昨天08：50
            t = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
        elif '前' in webtime:  ##8分钟前
            t = (datetime.datetime.now()).date()
        else:
            t = webtime[0:6]
            t = datetime.datetime.strptime(u"2018年" + str(t), "%Y年%m月%d日").date()  ##有误，全都按当年处理。后续应筛选
        Tem.append([t, question])
    Data = pd.DataFrame(Tem, columns=['t', 'ask']);
    Data=Data[(Data.t>=yesterday)&(Data.t<=today)].copy()
    Data.drop_duplicates(inplace=True);
    return Data

##深交所 互动易 ==》读取上一交易日到当天的评论
def get_ask_from_SZExchange(code,yesterday,today):
    url = r"http://irm.cninfo.com.cn/ircs/interaction/lastQuestionforSzseSsgs.do?condition.type=2&condition.stockcode=" + code + "&condition.stocktype=S"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features='lxml')
    x = [];
    for i in soup.find_all(re.compile('p')):
        if (type(i.a) == bs4.element.Tag) & (type(i.span) == bs4.element.Tag):
            t = i.span.string.strip()[1:12];
            t = datetime.datetime.strptime(t, "%Y年%m月%d日").date()
            comment = i.a.string.strip()
            x.append([t, comment])
    x = pd.DataFrame(x, columns=['t', 'ask'])
    x = x[(x.t >= yesterday) & (x.t <= today)].copy();
    x.drop_duplicates(inplace=True);
    return  x

    ###后续处理
    '''
    
    questions = ""
    for i in x.ask:
        questions = questions + i

    print questions
    
    for word in useless_words:
        questions = questions.replace(word, '');

    questions = questions.strip()
    print questions
    for x in jieba.analyse.extract_tags(questions, topK=8, withWeight=True, allowPOS=()):
        print x[0], x[1]
    '''


def get_index800(today):
    start = today - datetime.timedelta(days=10);    start = start.strftime("%Y%m%d");
    end = today;    end = end.strftime("%Y%m%d");
    csi300 = get_indexmembers(start, end, '000300.SH');    csi300 = sorted(set(csi300.ticker.values));
    csi500 = get_indexmembers(start, end, '000905.SH');    csi500 = sorted(set(csi500.ticker.values));
    index800 = [];
    index800.extend(csi300);
    index800.extend(csi500)
    return index800



def get_indexmembers(start,end,index_code):
    if index_code=='000300.SH':index_code='csi300';
    if index_code=='000905.SH':index_code='csi500';
    sql="select distinct ticker from Research.windIndexWgtsSSE where tradedate>='"+start+"' and tradedate<='"+end+"' and "+index_code+">0 ; "
    cnn=mdb.connect('10.10.40.310', 'report', 'raP1_Hdr2', 'Wind');
    cnn = cnn.cursor(mdb.cursors.SSDictCursor)
    cnn.execute(sql)
    dictionary = cnn.fetchall();
    table = pd.DataFrame(list(dictionary))
    return table;

def get_tradecalendar(today):
    start = today - datetime.timedelta(days=10);    start = start.strftime("%Y%m%d");
    end = today;    end = end.strftime("%Y%m%d");
    sql="select distinct str_to_date(trade_days,'%Y%m%d') as trade_days from Wind.ASHARECALENDAR where trade_days>='"+start+"' and trade_days<='"+end+"' and s_info_exchmarket='SZSE' order by trade_days;"
    print sql
    cnn = mdb.connect('10.10.40.310', 'report', 'raP1_Hdr2', 'Wind');
    cnn = cnn.cursor(mdb.cursors.SSDictCursor)
    cnn.execute(sql)
    dictionary = cnn.fetchall();
    table = pd.DataFrame(list(dictionary))
    table=sorted(set(table.trade_days.values));
    return table;

if __name__ == "__main__":
   main()