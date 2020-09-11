
import json
import datetime
from pymongo import MongoClient

from collections import Counter


# 加载配置
config = open('config.json')
setting = json.load(config)
MONGO_HOST = setting['MONGO_HOST']
MONGO_PORT = setting['MONGO_PORT']
News_DB_NAME = setting['News_DB_NAME']
mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
db = mc[News_DB_NAME]                         # 数据库

cl = db["news"]

# convert your date string to datetime object
start = datetime.datetime.utcnow().isoformat()
end = (datetime.datetime.utcnow()-datetime.timedelta(minutes=60)).isoformat()
print('-'*20)
count_frq = Counter()

useless_eyword = ['--','div','class','style','appendQr','align','font','cms','...','normal','11','justify','img','ul','start','strong','Bold','span','Center','width','https','page','list']
for row in cl.find({'published': {'$lt': start, '$gte': end }}):
    #print(row['tags'])
    for keyword in row['tags']:
        #print(keyword)
        if keyword in useless_eyword:
            print(keyword)
            row['tags'].remove(keyword)
    #print(row['tags'])
    count_frq.update(row['tags'])
print(count_frq)
print('-'*20)