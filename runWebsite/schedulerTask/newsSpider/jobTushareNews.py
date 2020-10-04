# -*- coding:utf-8 -*-
import tushare as ts
from pandas import DataFrame
import json,time
from pymongo import MongoClient, ASCENDING
from Object import NewsData
import jieba
import jieba.analyse
import datetime


jieba.set_dictionary('./schedulerTask/newsSpider/dict.txt')
#jieba.set_dictionary('dict.txt')

# 加载配置
config = open('./schedulerTask/config.json')
#config = open('config.json')
setting = json.load(config)

MONGO_HOST = setting['MONGO_HOST']
MONGO_PORT = setting['MONGO_PORT']
News_DB_NAME = setting['News_DB_NAME']
RSS_SOURCE = setting["RSS_SOURCE"]
RSS_HOTS = setting["RSS_HOTS"]

mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
db = mc[News_DB_NAME]                         # 数据库

ts.set_token('d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b')
pro = ts.pro_api()

def sinaNews():
    df = pro.news(src='sina')
    saveDb(df)

def wallstreetcnNews():
    df = pro.news(src='wallstreetcn')
    saveDb(df)

def jqkaNews():
    df = pro.news(src='10jqka')
    saveDb(df)


def eastmoneyNews():
    df = pro.news(src='eastmoney')
    saveDb(df)

def yuncaijingNews():
    df = pro.news(src='yuncaijing')
    saveDb(df)
def saveDb(df):

    cl = db["news_data"]
    cl.create_index([('content', ASCENDING)], unique=True)         # 添加索引
    newsData = NewsData()

    
    for index,row in df.iterrows():
        try:
            # title 有时为空
            newsData.title = row['title']
            if(newsData.title == ""):
                newsData.title = newsData.content
            try:
                newsData.published = datetime.datetime.strptime(row['datetime'],'%Y-%m-%d %H:%M:%S').isoformat()
            except:
                #print(row)
                continue
            newsData.content = row['content']
            if(newsData.content == ""):
                newsData.content = newsData.title
            if(newsData.title == ""):
                newsData.title = newsData.content

            newsData.tags = jieba.analyse.extract_tags(newsData.content, topK=200, allowPOS=('ns', 'n', 'nr', 'nt', 'nz'))

            d = newsData.__dict__
            flt = {'content': newsData.content}
            cl.replace_one(flt, d, True)
        except:
            print('--'*50)
            continue

     
def tushareNewsSpiderSchedulerTaskJob():
    sinaNews()
    time.sleep(10)
    wallstreetcnNews()
    time.sleep(10)
    jqkaNews()
    time.sleep(10)
    eastmoneyNews()
    time.sleep(10)
    yuncaijingNews()


if __name__ == "__main__":
    tushareNewsSpiderSchedulerTaskJob()