# encoding: UTF-8
import sys
import json
from datetime import datetime
from pymongo import MongoClient, ASCENDING
import feedparser
from Object import NewsData
import jieba
import jieba.analyse
from schedulerTask.newsSpider.util import filter_tags,convertISODate
#from util import filter_tags,convertISODate


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




def downloadRssDara(rssFeed):
    """下载Rss数据"""

    feedData=feedparser.parse(rssFeed)
    cl = db["news_data"]
    cl.ensure_index([('content', ASCENDING)], unique=True)         # 添加索引
    for i in range(len(feedData.entries)):  
        newsData = NewsData()
        try:
            newsData.title = feedData.entries[i].title
            newsData.content = filter_tags(feedData.entries[i].summary)
            try:
                newsData.published = convertISODate(feedData.entries[i].published)
            except:
                continue

            newsData.tags = jieba.analyse.extract_tags(newsData.content, topK=200, allowPOS=('ns', 'n', 'nr', 'nt', 'nz'))
        except:
            print('#'*50)
            continue
        
        d = newsData.__dict__
        flt = {'content': newsData.content}
        cl.replace_one(flt, d, True)   


def rssNewsSpiderSchedulerTaskJob():
    # 添加下载任务
    for feed in RSS_SOURCE:
        downloadRssDara(RSS_HOTS+feed)

if __name__ == "__main__":
    rssNewsSpiderSchedulerTaskJob()

