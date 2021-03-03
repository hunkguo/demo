# 导入pandas包
import pandas as pd
import numpy as np
from pymongo import MongoClient, ASCENDING

folderName = "./data/"
fileName = "section.xlsx"


Client = MongoClient()

MONGO_HOST = "localhost"
MONGO_PORT = 27017
News_DB_NAME = "db_gaokao"

mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
db = mc[News_DB_NAME]                         # 数据库

#导入标题行
# cols = pd.read_excel(folderName+fileName, engine="openpyxl", usecols=[1,2,3,4,5], header=None,nrows=1).values[1] # read first row

import_data = pd.read_excel(folderName+fileName, engine="openpyxl", usecols=[0,1,2,3,4]) # skip 1 row

#赋值标题
# import_data.columns = cols

#删除NA数据
import_data.dropna(inplace=True)
#或者
#df = df.dropna(axis=0,how='any')


# 显示前10行数据
# print(import_data)
cl_section = db["score_section_data"]
cl_section.create_index([('year', ASCENDING),('province',ASCENDING),('type',ASCENDING),('score',ASCENDING),('section', ASCENDING)], unique=True)

for _, row in import_data.iterrows():
    item = {}
    item["year"] = row["year"]
    item["province"] = row["province"]
    item["type"] = row["type"]
    item["score"] = row["score"]
    item["section"] = row["section"]
    # print(item)
    flt = {'year':item['year'],'province':item['province'],'type':item['type'],'score':item['score'],'section': item['section']}             
    cl_section.replace_one(flt, item, True)

				
'''
    cl_section = self.db["score_section_data"]
    cl_section.create_index([('year', ASCENDING),('province',ASCENDING),('type',ASCENDING),('score',ASCENDING),('section', ASCENDING)], unique=True)

    
'''

