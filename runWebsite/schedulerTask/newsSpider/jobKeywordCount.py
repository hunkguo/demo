# encoding: UTF-8
import sys
import json
import datetime
from pymongo import MongoClient, ASCENDING
from Object import NewsData
#from util import filter_tags,convertISODate
from collections import Counter

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




def keywordCount():
    cl = db["keyword_count"]
    cl.ensure_index([('datetime', ASCENDING)], unique=True)         # 添加索引   
    
    start = datetime.datetime.utcnow().isoformat()
    end = (datetime.datetime.utcnow()-datetime.timedelta(days=3)).isoformat()
    count_frq = Counter()
    useless_eyword = ['11','...','编辑','时间','来源','责任编辑','记者']
    cl_news = db["news_data"]
    for row in cl_news.find({'published': {'$lt': start, '$gte': end }}):
        #print(row['tags'])
        for keyword in row['tags']:
            #print(keyword)
            if keyword in useless_eyword:
                #print(keyword)
                row['tags'].remove(keyword)
        #print(row['tags'])
        count_frq.update(row['tags'])
    dict_count_frq = dict(count_frq.most_common(1000))
    current_date = datetime.datetime.now()
    flt = {'datetime': str(current_date)}
    cl.replace_one(flt, {"datetime":current_date, "frq": dict_count_frq}, True)


def keywordCountSchedulerTaskJob():
    keywordCount()

if __name__ == "__main__":
    keywordCountSchedulerTaskJob()

