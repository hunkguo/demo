# -*- coding:utf-8 -*-
import pandas as pd
import jieba.analyse
import MySQLdb as mdb
from collections import Counter
import datetime
def main():
    today = datetime.datetime.now().date();
    useless_words = ['谢谢','上市','股价','有限公司','你好','的', '董秘', '公司', '管理层', '请问', '吗', '我', '您好','有没有', '有何', '方案', '贵司', '贵公司','问下','信心','感谢','们','是否','多久','应该','应当','建议','最好','为何','为什么','多少','！','，','。','？','、','…','……','...',',','哪些','已','贵','披露','公告','影响','股东','关心','客观'];#,'！','，','。','？','、','…','……','...',','
    useless_words.extend(['潜力','业务','投资者','是不是','如何','17','18','20'])
    data=pd.read_csv('comments_'+today.strftime("%Y%m%d")+'.xls');
    grouped=data.groupby(['code']).size()
    grouped=pd.DataFrame(grouped,columns=['ask_num']);
    grouped['code'] = grouped.index;grouped.index=range(len(grouped));
    data=pd.merge(data,grouped,on=['code']);
    data=data[data.ask_num>=3].copy();
    codes=sorted(set(data.code.values));
    ## 读取证券名称
    Names=get_names_from_wind(codes)
    data=pd.merge(data,Names,on=['code'])

    data.sort_values(by=['ask_num'],ascending=False,inplace=True)
    #print data
    ## t,code,ask,ask_num,name
    Lists=[]
    for code in codes:
        data_i=data[data.code==code].copy();
        n=data_i.ask_num.max();
        name_i=data_i.name.max()
        ## 每一条评论筛选关键词，去除单条评论中的重复词语
        questions=''
        for j in data_i.ask:
            keywords=[];
            for k in jieba.cut(j):
                keywords.append(k);
            keywords=set(keywords)
            questions=questions+ ' '.join(keywords);
        if code == '002642.SZ':
            print questions;
        ##将无意义词汇删除（打招呼、公司名、语气词等,股票简称）
        name_i_ = [x for x in jieba.cut(name_i,cut_all=True,HMM=True)];## 列表。如果是iteration，则第二次不能迭代
        for j in name_i_:
            useless_words.append(j)
        for word in useless_words:
            questions=questions.replace(word,'')
        for j in name_i_:
            useless_words.pop(useless_words.index(j))
        questions=questions.strip()##只去除了两边的空格

        keywords=jieba.analyse.extract_tags(questions, topK=5, withWeight=True, allowPOS=());
        if code == '002642.SZ':
            print questions;
            for x in keywords:
                print x[0],x[1]

        keyword1 = keywords[0][0];        keyword1_weight = keywords[0][1];
        keyword2 = keywords[1][0];        keyword2_weight = keywords[1][1];
        keyword3 = keywords[2][0];        keyword3_weight = keywords[2][1]
        ##添加词（有些新生关键词，extract可以提取出来重复词，但cut不能识别）
        keywords = [keyword1, keyword2, keyword3];
        for word in keywords:
            jieba.add_word(word,tag=None)
        ##统计关键词keywords1,2,3 出现次数
        words_all=[];appeared_times=[]

        for x in jieba.cut(questions,cut_all=True,HMM=True):
            words_all.append(x)

        keywords=[keyword1,keyword2,keyword3];
        for i in range(len(keywords)):
            appeared_times.append(0)

        for i in range(len(keywords)):
            for word in words_all:
                if len(word)==0:## 速度快
                    continue
                elif word==keywords[i]:
                    appeared_times[i]=appeared_times[i]+1;
                else:
                    continue
        Lists.append([code,name_i,n,keyword1,appeared_times[0],keyword1_weight,keyword2,appeared_times[1],keyword2_weight,keyword3,appeared_times[2],keyword3_weight])
    results=pd.DataFrame(Lists,columns=['code','name','num','keyword1','n1','weight1','keyword2','n2','wight2','keyword3','n3','wight3'])
    results=results[(results.n1>2)|(results.n2>2)|(results.n3>2)].copy()
    results.sort_values(by=['num'],ascending=False,inplace=True);results.index=range(len(results.index))
    print results

    results=results[['code','name','num','keyword1','n1','keyword2','n2','keyword3','n3']].copy()
    results.to_csv('keywords_'+today.strftime("%Y%m%d")+'.xls',index=False,encoding='utf-8_sig')

    data = pd.read_csv('comments_' + today.strftime("%Y%m%d") + '.xls');
    tem=results[['code','name']].copy();
    data=pd.merge(data,tem,on=['code']);
    data.to_csv('comments_abnormal'+today.strftime("%Y%m%d")+'.xls',index=False,encoding='utf-8_sig')



### codes is a list
def get_names_from_wind(codes):
    codes="','".join(codes);
    codes="('"+codes+"')"
    sql="select s_info_windcode as code,s_info_name as name from Wind.ASHAREDESCRIPTION where s_info_windcode in "+codes+";"
    cnn = mdb.connect('10.10.40.310', 'report', 'raP1_Hdr2', 'Wind',charset='utf8');
    cnn = cnn.cursor(mdb.cursors.SSDictCursor)
    cnn.execute(sql)
    dictionary = cnn.fetchall();
    table = pd.DataFrame(list(dictionary))
    return table;

if __name__=='__main__':
    main()