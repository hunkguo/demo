# encoding: UTF-8
import sys
import json
from datetime import datetime
from time import time, sleep

from pymongo import MongoClient, ASCENDING
import feedparser
from rssObject import RssData

# 加载配置
config = open('config.json')
setting = json.load(config)

MONGO_HOST = setting['MONGO_HOST']
MONGO_PORT = setting['MONGO_PORT']
SYMBOLS = setting['SYMBOLS']
News_DB_NAME = setting['News_DB_NAME']
RSS_SOURCE = setting["RSS_SOURCE"]

mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
db = mc[News_DB_NAME]                         # 数据库




def downloadRssDara(rss):
    """下载Rss数据"""

    feedData=feedparser.parse(rss)


    start = time()
    cl = db["news"]
    cl.ensure_index([('datetime', ASCENDING)], unique=True)         # 添加索引
    for i in range(len(feedData.entries)):
        print('-' * 20)
        print("开始下载[文章%d]数据" % i)
        print('-' * 20)
        #print(feedData.entries[i].title)
        print(feedData.entries[i].summary)
        #print(feedData.entries[i].link)


        rss = RssData()
        rss.title = feedData.entries[i].title
        rss.summary = feedData.entries[i].summary
        rss.link = feedData.entries[i].link
        
        d = rss.__dict__
        flt = {'datetime': start}
        cl.replace_one(flt, d, True)            

    end = time()
    cost = (end - start) * 1000

    print(u'数据下载完成，耗时%s毫秒' %(cost))

def downloadAllData():

    print('-' * 50)
    print("开始下载RSS数据")
    print('-' * 50)

    # 添加下载任务
    for rss in RSS_SOURCE:
        downloadRssDara(rss)

    print('-' * 50)
    print(u'RSS数据下载完成')
    print('-' * 50)