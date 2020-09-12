# encoding: UTF-8
import sys
import json
from datetime import datetime
from time import time, sleep

from pymongo import MongoClient, ASCENDING
import feedparser
from rssObject import RssData
import jieba
import jieba.analyse
from util import filter_tags,convertISODate


jieba.set_dictionary('dict.txt')

# 加载配置
config = open('config.json')
setting = json.load(config)

MONGO_HOST = setting['MONGO_HOST']
MONGO_PORT = setting['MONGO_PORT']
News_DB_NAME = setting['News_DB_NAME']
RSS_SOURCE = setting["RSS_SOURCE"]
RSS_HOTS = setting["RSS_HOTS"]

mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
db = mc[News_DB_NAME]                         # 数据库




def downloadRssDara(rssFeed):
    """下载Rss数据"""

    feedData=feedparser.parse(rssFeed)


    #start = time()
    cl = db["news"]
    cl.ensure_index([('link', ASCENDING)], unique=True)         # 添加索引
    for i in range(len(feedData.entries)):  
        '''       
        print('-' * 20)
        print("开始下载[文章%d]数据" % i)
        print('-' * 20)
        print(convertISODate(feedData.entries[i].published))
        print(filter_tags(feedData.entries[i].summary))
        print(feedData.entries[i].link)
        '''

        rssDate = RssData()
        try:
            rssDate.title = feedData.entries[i].title
            rssDate.summary = filter_tags(feedData.entries[i].summary)
            #rssDate.published = formatGMTime(feedData.entries[i].published)
            try:
                rssDate.published = convertISODate(feedData.entries[i].published)
            except:
                pass
            rssDate.link = feedData.entries[i].link

            rssDate.tags = jieba.analyse.extract_tags(rssDate.summary, topK=200, allowPOS=('ns', 'n', 'nr', 'nt', 'nz'))
        except:
            print(feedData.entries[i])
            continue
        
        d = rssDate.__dict__
        flt = {'link': rssDate.link}
        cl.replace_one(flt, d, True)   

    #end = time()
    #cost = (end - start) * 1000
    #print(u'数据下载完成，耗时%s毫秒' %(cost))
    print(u'【%s】数据下载完成' %(rssFeed))

def downloadAllData():

    print('-' * 50)
    print("开始下载RSS数据")
    print('-' * 50)

    # 添加下载任务
    for feed in RSS_SOURCE:
        downloadRssDara(RSS_HOTS+feed)
        #print(RSS_HOTS+feed)

    print('-' * 50)
    print(u'RSS数据下载完成')
    print('-' * 50)