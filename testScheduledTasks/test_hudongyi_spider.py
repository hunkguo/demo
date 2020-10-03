# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4  import BeautifulSoup
import re
import datetime
import pandas as pd
import jieba.analyse
import requests
from bs4 import BeautifulSoup
import bs4
import tushare as ts
from pandas import DataFrame

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# open it, go to a website, and get results
driver = webdriver.Chrome('chromedriver',options=options)

ts.set_token('d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b')
pro = ts.pro_api()

def main():
    #0.0 时间初始化
    today = datetime.datetime.now().date();
    lastday=get_tradecalendar(today);
    
    ##1.0 读取800成分股
    all_stock=get_all_stock();
    h=0;
    ##上证e互动 和 深交所互动易
    Failed_reading=[];Data=pd.DataFrame([]);j=0
    for i in all_stock:
        code=i[0:6];        exchange=i[7:];
        h=h+1;
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
        break
    Data.index=range(len(Data.index))
    Data.to_csv('comments_'+today.strftime("%Y%m%d")+'.xls',index=False,encoding='utf-8_sig')


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
    url = r"http://irm.cninfo.com.cn/ircs/company/companyDetail?stockcode=" + code 
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features='lxml')
    x = [];
    print(soup.find_all('div',class_='question-content pd-20 pb-10'))
    #返回数据为{{}}，无真实数据，卡壳
    '''
    for i in soup.find_all(re.compile('p')):
        if (type(i.a) == bs4.element.Tag) & (type(i.span) == bs4.element.Tag):
            t = i.span.string.strip()[1:12];
            t = datetime.datetime.strptime(t, "%Y年%m月%d日").date()
            comment = i.a.string.strip()
            x.append([t, comment])
    x = pd.DataFrame(x, columns=['t', 'ask'])
    x = x[(x.t >= yesterday) & (x.t <= today)].copy();
    x.drop_duplicates(inplace=True);
    '''
    return  x


def get_all_stock():
    df = pro.stock_basic()
    return df['ts_code']

def get_tradecalendar(today):
    start = today - datetime.timedelta(days=30);    start = start.strftime("%Y%m%d");
    end = today;    end = end.strftime("%Y%m%d");
    df = pro.trade_cal(exchange='', start_date=start, end_date=end, is_open='1')
    return(df['cal_date']);

if __name__ == "__main__":
    main()

