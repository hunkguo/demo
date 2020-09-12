
import json
from pymongo import MongoClient,ASCENDING
from rssObject import RssData
import jieba
import jieba.analyse
jieba.set_dictionary('dict.txt')


# 加载配置
config = open('config.json')
setting = json.load(config)
MONGO_HOST = setting['MONGO_HOST']
MONGO_PORT = setting['MONGO_PORT']
News_DB_NAME = setting['News_DB_NAME']
mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
db = mc[News_DB_NAME]                         # 数据库

cl = db["news"]

def reBuild():

    cl = db["news"]
    cl.ensure_index([('link', ASCENDING)], unique=True)         # 添加索引
    
    for row in cl.find():
        rssDate = RssData()        
        rssDate.ObjectId = row['_id']
        rssDate.title = row['title']
        rssDate.summary = row['summary']
        rssDate.published = row['published']
        rssDate.link = row['link']
        rssDate.tags = jieba.analyse.extract_tags(rssDate.summary, topK=100, allowPOS=('ns', 'n', 'nr', 'nt', 'nz'))

        
        d = rssDate.__dict__
        flt = {'link': rssDate.link}
        cl.replace_one(flt, d, True) 

        
        print(u'【%s】分词更新完成' %(rssDate.title))


if __name__ == '__main__':
    reBuild()


