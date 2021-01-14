# coding:utf-8
import easyquotation
import datetime,time
from pymongo import MongoClient, ASCENDING
import json
import asyncio

# 加载配置
config = open('config.json')
setting = json.load(config)

MONGO_HOST = setting['MONGO_HOST']
MONGO_PORT = setting['MONGO_PORT']
DB_NAME = setting['DB_NAME']

mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
db = mc[DB_NAME]                         # 数据库
cl = db["tick_data"]
#cl.ensure_index([('code', ASCENDING)], unique=True)         # 添加索引
cl.create_index([('code',1), ('time',1)], name = 'idx_code_time')

async def snapshot_data_from_sina():
    #print(f"抓取数据started at {time.strftime('%X')}")
    quotation = easyquotation.use('sina') # 新浪 ['sina'] 腾讯 ['tencent', 'qq'] 
    snapshot_data = quotation.market_snapshot(prefix=True) # prefix 参数指定返回的行情字典中的股票代码 key 是否带 sz/sh 前缀
    #print(f"抓取数据finished at {time.strftime('%X')}")
    await save_data_to_mongodb(snapshot_data)


async def save_data_to_mongodb(data):

    #print(f"保存数据started at {time.strftime('%X')}")
    for code,tick_data in data.items():
        tick_data["code"] = code
        #print(str(tick_data))
        flt = {'code': code, 'time':tick_data['time']}
        cl.replace_one(flt, tick_data, True)
    #print(f"保存数据finished at {time.strftime('%X')}")


if __name__ == '__main__':
    
    # 生成一个随机的任务下载时间，用于避免所有用户在同一时间访问数据服务器
    taskStartTime = datetime.time(hour=9, minute=15)
    taskEndTime = datetime.time(hour=15, minute=15)
    
    # 进入主循环
    while True:
        t = datetime.datetime.now()

        if (t.time() > taskStartTime and t.time() <taskEndTime):
            print(u'当前时间%s，执行定时任务' %(time.strftime('%X')))
            asyncio.run(snapshot_data_from_sina())
        else:
            print(u'当前时间%s，任务开始时间%s，任务结束时间%s' %(time.strftime('%X'), taskStartTime, taskEndTime))
            time.sleep(60)


