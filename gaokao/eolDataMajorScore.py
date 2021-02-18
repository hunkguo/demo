from fake_useragent import UserAgent
import urllib.request
import json
from json.decoder import JSONDecodeError


from pymongo import MongoClient, ASCENDING
import time
import socket

from gaokao import schools,provinces


Client = MongoClient()

MONGO_HOST = "localhost"
MONGO_PORT = 27017
News_DB_NAME = "db_gaokao"

mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
db = mc[News_DB_NAME]                         # 数据库

ua = UserAgent(verify_ssl=False)
# 伪装浏览器
headers = {
            'Origin': 'https://gkcx.eol.cn',
            'Referer': 'https://gkcx.eol.cn/school/566/provinceline',
            'User-Agent':ua.random
}


from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, ALL_COMPLETED, as_completed
from urllib import request,error

cl2 = db["school_special_score_data"]
cl2.create_index([('school_id', ASCENDING),('special_id',ASCENDING ),('type',ASCENDING),('id',ASCENDING),('year',ASCENDING),('spid',ASCENDING),('batch',ASCENDING),('zslx_name', ASCENDING),('province', ASCENDING),('max',ASCENDING),('min',ASCENDING),('min_section',ASCENDING),('average',ASCENDING),('level1', ASCENDING),('level2', ASCENDING),('level3', ASCENDING),('local_batch_name',ASCENDING)], unique=True)
def spider(url_path):
    # time.sleep(0.1)
    # print("线程开始 : %s" % time.ctime())
    try:
        req = urllib.request.Request(
                        url, 
                        data=None, 
                        headers = headers
                    )
        # print(url_path)
        f = urllib.request.urlopen(req, timeout=60)
        if(f.getcode()==200):
            result = json.loads(f.read().decode('utf-8'))
            if( result['code'] == '0000' and result['message'] =='成功'):
                COUNT = 0
                for item in result['data']['item']:
                    COUNT = COUNT + 1
                    item['year'] = url.split('/')[6]
                    flt = {'school_id':item['school_id'],'special_id':item['special_id'],'type':item['type'],'year':item['year'],'id':item['id'],'spid':item['spid'],'batch':item['batch'],'zslx_name':item['zslx_name'],'province': item['province'],'max': item['max'],'min': item['min'],'min_section': item['min_section'],'average': item['average'],'level1':item['level1'],'level2':item['level2'],'level3':item['level3'],'local_batch_name':item['local_batch_name']}
                    # print(item)
                    cl2.replace_one(flt, item, True)
                logging.info('Crawl %d records  - URL %s', COUNT, url_path)    
    except urllib.error.HTTPError as error:
        logging.error('Data not retrieved because %s - URL: %s', error, url)
    except urllib.error.URLError as error:
        if isinstance(error.reason, socket.timeout):
            logging.error('socket timed out because %s - URL: %s', error, url)
        else:
            logging.error('some other error happened %s - URL: %s', error, url)
    except socket.timeout as error: 
        logging.error('socket timed out because %s - URL: %s', error, url)
    except JSONDecodeError as error:
        logging.error('json decode error  because %s - URL: %s', error, url)
    except:
        pass
    else:
        pass
        
    # print("线程结束 : %s" % time.ctime())
    return data_html







from tqdm import tqdm
if __name__=="__main__":
    

    url_list = ['https://static-data.eol.cn/www/2.0/schoolspecialindex/2019/102/11/1/1.json']
    # url_list = majorScoreUrlList()
    
    executor = ThreadPoolExecutor(max_workers=8)
    tasks = []

    print("任务开始 : %s" % time.ctime())
    # with tqdm(total=len(url_list)) as pbar:
    for url in url_list:
        # 执行函数，并传入参数
        task = executor.submit(spider, url)
        tasks.append(task)
        time.sleep(0.5)
        # for future in as_completed(tasks):
        #     # data_html = future.result()
        #     # saveData(data_html)
        #     pbar.update(1)
    print("线程执行完毕 : %s" % time.ctime())

    '''
    executor = ThreadPoolExecutor(max_workers=8)
    # url_list = ['https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/102/52/6/7.json']
    url_list = schoolScoreUrlList()
    tasks = []
    # 执行蜘蛛并加入执行列表
    # 循环方式添加
    for url in url_list:
        # 执行函数，并传入参数
        task = executor.submit(spider, url)
        tasks.append(task)
        time.sleep(randint(1,5))
    # 等待方式1： 结束
    # wait(tasks, return_when=ALL_COMPLETED)
    # 等待方式2：结束
    for future in as_completed(tasks):
        data_html = future.result()
        saveData(data_html)
    # 等待方式3: 结束 - 替代submit并伴随等待！
    # for data in executor.map(spider, url_list):
    #     print(data)
    '''
