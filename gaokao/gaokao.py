from fake_useragent import UserAgent
import urllib.request
import json


from pymongo import MongoClient, ASCENDING
import time

from random import randint

Client = MongoClient()

MONGO_HOST = "localhost"
MONGO_PORT = 27017
News_DB_NAME = "db_gaokao"

mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
db = mc[News_DB_NAME]                         # 数据库

ua = UserAgent()
# 伪装浏览器
headers = {
            'Origin': 'https://gkcx.eol.cn',
            'Referer': 'https://gkcx.eol.cn/school/566/provinceline',
            'User-Agent':ua.random
}

def schools():
    cl = db["school_data"]
    cl.create_index([('school_id', ASCENDING)], unique=True)         # 添加索引
    
    if(cl.estimated_document_count()==0):
        for i in range(1,100):
            url = ('https://api.eol.cn/gkcx/api/?page=%d&request_type=1&size=30&sort=view_total&uri=apidata/api/gk/school/lists' % i)

            req = urllib.request.Request(
                url, 
                data=None, 
                headers = headers
            )

            f = urllib.request.urlopen(req)

            if(f.getcode()==200):
                #print(f.read().decode('utf-8'))
                result = json.loads(f.read().decode('utf-8'))
                if(result!=''):
                    returnCode = result['code'] 
                    returnMessage = result['message'] 
                    if( returnCode== '0000' and returnMessage=='成功'):
                        schools = result['data']['item']
                        for item in schools:
                            flt = {'school_id': item['school_id']}
                            cl.replace_one(flt, item, True)
                        time.sleep(0.5)
    #print(list(cl.find()))
    return list(cl.find())


def provinces():
    import string
    cl = db["province_data"]
    cl.create_index([('provinceid', ASCENDING)], unique=True) 

    if(cl.estimated_document_count()==0):
    
        url = 'https://static-data.eol.cn/www/location/location.json'
        req = urllib.request.Request(
            url, 
            data=None, 
            headers = headers
        )

        alphabet_list = list(string.ascii_uppercase)

        f = urllib.request.urlopen(req)
        if(f.getcode()==200):
            result = json.loads(f.read().decode('utf-8'))

            # print(result['H'])
            if(result!=''):
                for i in alphabet_list:
                    if(i in result):
                        for item in result[i]:
                            flt = {'provinceid': item['provinceid']}
                            cl.replace_one(flt, item, True)
    #                         print(s['provinceid'])
    #                         print(s['province'])
    #     print(list(cl.find()))
    return list(cl.find())


def schoolScoreUrlList():
    url_list = []
    schoolList = schools()
    provinceList = provinces()
    for school in schoolList:
        schoolId = school['school_id']
        for province in provinceList:
            provinceId = province['provinceid']
            for recruit_type in range(1,10):
                for i in range(1,10):
                    url = 'https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/{}/{}/{}/{}.json'.format(schoolId,provinceId,recruit_type,i)
                    url_list.append(url)
    return url_list
                    

from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, ALL_COMPLETED, as_completed
from urllib import request,error
import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def spider(url_path):
    data_html = ''
    time.sleep(randint(1,3))
    try:
        req = urllib.request.Request(
                        url, 
                        data=None, 
                        headers = headers
                    )

        f = urllib.request.urlopen(req, timeout=60)
        result = json.loads(f.read().decode('utf-8'))
        COUNT = 0
        if(f.getcode()==200 and result!=''):
            if( result['code'] == '0000' and result['message'] =='成功'):
                for item in result['data']['item']:
                    COUNT = COUNT + 1
#                                         cl.insert_one(item)
                    flt = {'school_id':item['school_id'],'type':item['type'],'batch':item['batch'],'zslx_name':item['zslx_name'],'province_id': item['province_id'],'xclevel': item['xclevel'],'type_control': item['type_control'],'batch_control': item['batch_control'],'proscore': item['proscore'],'max': item['max'],'min': item['min'],'min_section': item['min_section'],'average': item['average'],'filing': item['filing'],'year':item['year']}
                    cl.replace_one(flt, item, True)

                logging.info('Crawl %d records   - URL %s', COUNT, url_path)   
            else:
                logging.error('Return json data error - URL %s', url_path)    
    except urllib.error.HTTPError as error:
        logging.error('Data not retrieved because %s\nURL: %s', error, url)
    except urllib.error.URLError as error:
        if isinstance(error.reason, socket.timeout):
            logging.error('socket timed out - URL %s', url)
        else:
            logging.error('some other error happened')
    except socket.timeout as error: 
        logging.error('socket timed out - URL %s', url)    
    else:
        pass
    return data_html






    
cl = db["school_score_data"]
cl.create_index([('school_id', ASCENDING),('type',ASCENDING),('batch',ASCENDING),('xclevel',ASCENDING),('zslx_name', ASCENDING),('province_id', ASCENDING),('type_control',ASCENDING),('batch_control',ASCENDING),('proscore',ASCENDING),('max',ASCENDING),('min',ASCENDING),('min_section',ASCENDING),('average',ASCENDING),('filing',ASCENDING),('year', ASCENDING)], unique=True)


def saveData(data_html):
    result = json.loads(data_html)
    if(result!=''):
        if( result['code'] == '0000' and result['message'] =='成功'):
            for item in result['data']['item']:
                flt = {'school_id':item['school_id'],'type':item['type'],'batch':item['batch'],'zslx_name':item['zslx_name'],'province_id': item['province_id'],'xclevel': item['xclevel'],'type_control': item['type_control'],'batch_control': item['batch_control'],'proscore': item['proscore'],'max': item['max'],'min': item['min'],'min_section': item['min_section'],'average': item['average'],'filing': item['filing'],'year':item['year']}
                cl.replace_one(flt, item, True)

# 创建一个最大容量为1的线程
executor = ThreadPoolExecutor(max_workers=16)
if __name__=="__main__":
    #print(url_list)
    #print(randint(1,5))

    #url_list = ['https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/102/13/1/1.json']


    url_list = schoolScoreUrlList()
    tasks = []
    # 执行蜘蛛并加入执行列表
    for url in url_list:
        # 执行函数，并传入参数
        task = executor.submit(spider, url)
        tasks.append(task)
        time.sleep(randint(3,10))
    # 等待方式1： 结束
    # wait(tasks, return_when=ALL_COMPLETED)
    # 等待方式2：结束
    for future in as_completed(tasks):
        # spider方法无返回，则返回为None
        data_html = future.result()
        saveData(data_html)
    # 等待方式3: 结束 - 替代submit并伴随等待！
    # for data in executor.map(spider, url_list):
    #     print(data)

