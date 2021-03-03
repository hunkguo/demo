from fake_useragent import UserAgent
import urllib.request
import json
from json.decoder import JSONDecodeError


from pymongo import MongoClient, ASCENDING
import time,datetime
import socket

from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, ALL_COMPLETED, as_completed
from urllib import request,error

from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, ALL_COMPLETED, as_completed
from urllib import request,error
import logging
import multiprocessing
from tqdm import tqdm
import requests


import aiohttp
import asyncio

# 教育在线数据

# 写死了数据库连接，待优化

class eolData:
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

    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(filename='error.log', level=logging.ERROR, format=LOG_FORMAT, datefmt=DATE_FORMAT)


    executor = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())

    
    # 学校数据
    def schools(self):
        cl_school_data = self.db["school_data"]
        cl_school_data.create_index([('school_id', ASCENDING)], unique=True)         # 添加索引
        
        if(cl_school_data.estimated_document_count()==0):
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
                                cl_school_data.replace_one(flt, item, True)
                            # time.sleep(0.5)
        #print(list(cl.find()))
        return list(cl_school_data.find())

    # 省市数据
    def provinces(self):
        import string
        cl_province_data = self.db["province_data"]
        cl_province_data.create_index([('provinceid', ASCENDING)], unique=True) 

        if(cl_province_data.estimated_document_count()==0):
        
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
                                cl_province_data.replace_one(flt, item, True)
        #                         print(s['provinceid'])
        #                         print(s['province'])
        #     print(list(cl.find()))
        return list(cl_province_data.find())




    # 学校分数线数据待抓取链接
    def schoolScoreLink(self):
        cl_school_score_link_data = self.db["school_score_link_data"]
        cl_school_score_link_data.create_index([('link', ASCENDING)], unique=True) 
        if(cl_school_score_link_data.estimated_document_count()==0):
            schoolList = self.schools()
            provinceList = self.provinces()
            for school in schoolList:
                schoolId = school['school_id']
                for province in provinceList:
                    provinceId = province['provinceid']
                    for recruit_type in range(1,10):
                    # for recruit_type in range(1,2):
                        for i in range(1,10):
                        # for i in range(1,2):
                            item = {}
                            link = 'https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/{}/{}/{}/{}.json'.format(schoolId,provinceId,recruit_type,i)
                            item['link'] = link
                            item['responseData'] = ''
                            item['check_at'] = datetime.datetime.utcnow()


                            flt = {'link': item['link']}
                            cl_school_score_link_data.replace_one(flt, item, True)
        data = list(cl_school_score_link_data.find().sort('check_at', -1).limit(100000))
        return data
                        

    # 专业分数线待抓取链接
    def majorScoreLink(self):
        cl_major_score_link_data = self.db["major_score_link_data"]

        if(cl_major_score_link_data.estimated_document_count()==0):
            cl_major_score_link_data.create_index([('link', ASCENDING)], unique=True) 
            schoolList = self.schools()
            provinceList = self.provinces()


            cl_school_score = self.db["school_score_data"]

            for school in schoolList:
                schoolId = school['school_id']
                # recruit_type_data = cl_school_score.distinct("type", {"school_id":schoolId})
                recruit_type_data = cl_school_score.distinct("type", {"school_id":str(schoolId)})
                for province in provinceList:
                    provinceId = province['provinceid']
                    # 录取类型
                    # db.school_score_data.distinct("type", {school_id:"42"})
                    for recruit_type in recruit_type_data:
                    # for recruit_type in range(1,2):
                        for i in range(1,5):    #待验证是否够用
                        # for i in range(1,2):
                            for yearNumber in range(2020,2014,-1):
                                item = {}
                                # link = 'https://static-data.eol.cn/www/2.0/schoolspecialindex/{}/{}/13/{}/{}.json'.format(yearNumber, schoolId,provinceId,recruit_type,i)
                                link = 'https://static-data.eol.cn/www/2.0/schoolspecialindex/{}/{}/{}/{}/{}.json'.format(yearNumber, schoolId,provinceId,recruit_type,i)
                                item['link'] = link
                                item['responseData'] = ''
                                item['check_at'] = datetime.datetime.utcnow()
                                flt = {'link': item['link']}
                                # print(item)
                                cl_major_score_link_data.replace_one(flt, item, True)

        data = list(cl_major_score_link_data.find().sort('check_at', -1).limit(100000))
        return data

    # 学校招生计划待抓取链接
    def enrollPlanLink(self):
        cl_enroll_plan_link_data = self.db["enroll_plan_link_data"]
        if(cl_enroll_plan_link_data.estimated_document_count()==0):
            cl_enroll_plan_link_data.create_index([('link', ASCENDING)], unique=True) 
            schoolList = self.schools()
            provinceList = self.provinces()

            cl_school_score = self.db["school_score_data"]

            for school in schoolList:
                schoolId = school['school_id']
                recruit_type_data = cl_school_score.distinct("type", {"school_id":str(42)})
                batchNumber_data = cl_school_score.distinct("batch", {"school_id":str(42)})
            # print(recruit_type_data)
            # print(batchNumber_data)
            # https://static-data.eol.cn/www/2.0/schoolplanindex/2019/42/33/1/12/1.json
            for province in provinceList:
                provinceId = province['provinceid']
                for recruit_type in recruit_type_data:
                    # print(type(recruit_type))
                    # 录取类型
                    # db.school_score_data.distinct("type", {school_id:"42"})
                    # for recruit_type in range(1,2):
                        for batchNumber in batchNumber_data:
                        # db.school_score_data.distinct("batch", {school_id:"42"})
                        # 没猜对
                        # 根据学校录取情况取批次
                            for i in range(1,5):
                            # for i in range(1,2):
                                for yearNumber in range(2020,2014,-1):
                                    link ='https://static-data.eol.cn/www/2.0/schoolplanindex/{}/{}/{}/{}/{}/{}.json'.format(yearNumber,schoolId,provinceId,recruit_type,batchNumber,i)
                                    # data_json = self.crawler(link)

                                    item = {}
                                    item['link'] = link
                                    item['responseData'] = ''
                                    item['check_at'] = datetime.datetime.utcnow()
                                    flt = {'link': item['link']}
                                    cl_enroll_plan_link_data.replace_one(flt, item, True)
        data = list(cl_enroll_plan_link_data.find().sort('check_at', -1).limit(100000))
        return data








    def noticeIfttt(self, msg):
        try:
            d = { "value1" : msg}
            url = 'https://maker.ifttt.com/trigger/notice_task_iphone/with/key/eT7xmvYI5fXlIgjmmYoHQ'
            requests.post(url, data=d)
        except:
            pass






    
    # v3
    # 抓取学校分数线数据
    def SchoolScoreMain(self):
        cl_school_score = self.db["school_score_data"]
        cl_school_score.create_index([('school_id', ASCENDING),('type',ASCENDING),('batch',ASCENDING),('xclevel',ASCENDING),('zslx_name', ASCENDING),('province_id', ASCENDING),('type_control',ASCENDING),('batch_control',ASCENDING),('proscore',ASCENDING),('max',ASCENDING),('min',ASCENDING),('min_section',ASCENDING),('average',ASCENDING),('filing',ASCENDING),('year', ASCENDING)], unique=True)

        
        # https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/102/52/1/1.json
        school_score_link_list = self.schoolScoreLink()

        for school_score_link in school_score_link_list:
            # print(school_score_link['link'])
            response_data = school_score_link['responseData']
            if(response_data!="none" and response_data!=""):
                # print(response_data)
                try:
                    response_data_json = json.loads(response_data)
                except:
                    cl_school_score_link_data = self.db["school_score_link_data"]
                    item = {}
                    item['link'] = school_score_link['link']
                    item['responseData'] = ''
                    item['check_at'] = datetime.datetime.utcnow()
                    flt = {'link': item['link']}
                    cl_school_score_link_data.replace_one(flt, item, True)


                if( response_data_json['code'] == '0000' and response_data_json['message'] =='成功'):
                    # print(url)
                    data_json = response_data_json['data']['item']
                    # print(response_data_json)
                    for item in data_json:
                        # print(item['school_id'])
                        flt = {'school_id':item['school_id'],'type':item['type'],'batch':item['batch'],'zslx_name':item['zslx_name'],'province_id': item['province_id'],'xclevel': item['xclevel'],'type_control': item['type_control'],'batch_control': item['batch_control'],'proscore': item['proscore'],'max': item['max'],'min': item['min'],'min_section': item['min_section'],'average': item['average'],'filing': item['filing'],'year':item['year']}
                    
                        cl_school_score.replace_one(flt, item, True)
                        
    # 测试是否有返回值
    def crawler(self, url):
        data_json = ''
        try:
            # print(url)
            req = urllib.request.Request(
                            url, 
                            data=None, 
                            headers = self.headers
                        )
            f = urllib.request.urlopen(req, timeout=60)
            
            if(f.getcode()==200):
                result = json.loads(f.read().decode('utf-8'))

                # 判断json数据是否正确
                if( result['code'] == '0000' and result['message'] =='成功'):
                    print(url)
                    data_json = result['data']['item']
        except:
            pass
        return data_json



if __name__=="__main__":
    eol = eolData()
    try:
        # while True:
            # 完成
            # print("任务[专业分数线链接]开始  "+str(datetime.datetime.now()))
            # eol.majorScoreLink()

            # print("任务[招生计划链接]开始"+str(datetime.datetime.now()))
            eol.enrollPlanLink()


            # 23059.pts-0.vmDebian
            # print("任务[学校分数线]开始"+str(datetime.datetime.now()))
            # eol.SchoolScoreMain()
            






        


        # pass



        # cl_school_score = eol.db["school_score_data"]

        # # for school in schoolList:
        #     # schoolId = school['school_id']
        # # recruit_type_data = cl_school_score.distinct("type", {"school_id":str(42), "province_id":str(33)})
        # # batchNumber_data = cl_school_score.distinct("batch", {"school_id":str(42), "province_id":str(33)})
        # recruit_type_data = cl_school_score.distinct("type", {"school_id":str(42)})
        # batchNumber_data = cl_school_score.distinct("batch", {"school_id":str(42)})
        # print(recruit_type_data)
        # print(batchNumber_data)

        # for recruit_type in range(1,4):
        #     for batchNumber in range(1,100):
        #         for i in range(1,6):
        #             link ='https://static-data.eol.cn/www/2.0/schoolplanindex/2020/42/13/{}/{}/{}.json'.format(recruit_type,batchNumber,i)
        #             data_json = eol.crawler(link)


    except Exception as e: 
        logging.error('Unknow error : '+ str(e))
        eol.noticeIfttt('任务有错')










'''


    # 共用爬虫
    def spider(self, url, cl):
        # time.sleep(0.1)
        # print("线程开始 : %s" % time.ctime())
        data_json = ''
        try:
            # print(url)
            req = urllib.request.Request(
                            url, 
                            data=None, 
                            headers = self.headers
                        )
            f = urllib.request.urlopen(req, timeout=60)
            
            if(f.getcode()==200):
                result = json.loads(f.read().decode('utf-8'))
                # 更新返回数据
                myquery = { "link": url}
                newvalues = { "$set": { "responseData": result, "check_at":datetime.datetime.utcnow()} }
                cl.update_one(myquery, newvalues)

                # 判断json数据是否正确
                if( result['code'] == '0000' and result['message'] =='成功'):
                    # print(url)
                    data_json = result['data']['item']
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
        return data_json


    # 保存专业分数线数据
    def saveDataMajorScore(self, data_json, url, cl):
        try:
            # COUNT = 0
            for item in data_json:
                # COUNT = COUNT + 1

                item['year'] = url.split('/')[6]
                flt = {'school_id':item['school_id'],'special_id':item['special_id'],'type':item['type'],'year':item['year'],'id':item['id'],'spid':item['spid'],'batch':item['batch'],'zslx_name':item['zslx_name'],'province': item['province'],'max': item['max'],'min': item['min'],'min_section': item['min_section'],'average': item['average'],'level1':item['level1'],'level2':item['level2'],'level3':item['level3'],'local_batch_name':item['local_batch_name'],'year':item['year']}
                # print(item)
                cl.replace_one(flt, item, True)
            # logging.info('Crawl %d records  - URL %s', COUNT, url)   
        except:
            logging.error('some error - URL %s', url)  
            # pass

    # 抓取专业分数线数据
    def runMajorScore(self):
        
        cl_major_score = self.db["major_score_data"]
        cl_major_score.create_index([('school_id', ASCENDING),('special_id',ASCENDING ),('type',ASCENDING),('id',ASCENDING),('year',ASCENDING),('spid',ASCENDING),('batch',ASCENDING),('zslx_name', ASCENDING),('province', ASCENDING),('max',ASCENDING),('min',ASCENDING),('min_section',ASCENDING),('average',ASCENDING),('level1', ASCENDING),('level2', ASCENDING),('level3', ASCENDING),('local_batch_name',ASCENDING),('year',ASCENDING)], unique=True)

        # major_score_link_list = ['https://static-data.eol.cn/www/2.0/schoolspecialindex/2019/102/11/1/1.json']
        major_score_link_list = self.majorScoreLink()
        
        tasks = []

        # startTime = datetime.datetime.now()
        # print("任务开始 : %s" % startTime)
        for major_score_link in major_score_link_list:
            url = major_score_link['link']
            # 执行函数，并传入参数
            task = self.executor.submit(self.spider, url, cl = self.db["major_score_link_data"])
            tasks.append(task)
            for future in as_completed(tasks):
                data_json = future.result()
                self.saveDataMajorScore(data_json, url, cl_major_score) 


        # endTime = datetime.datetime.now()
        # print("任务完成 : %s" % endTime)
        # print("用时%s" % (endTime-startTime))

    

    # 保存学校分数线数据
    def saveDataSchoolScore(self, data_json, url, cl):
        try:
            # COUNT = 0
            # print(url_path)
            for item in data_json:
                # COUNT = COUNT + 1
                flt = {'school_id':item['school_id'],'type':item['type'],'batch':item['batch'],'zslx_name':item['zslx_name'],'province_id': item['province_id'],'xclevel': item['xclevel'],'type_control': item['type_control'],'batch_control': item['batch_control'],'proscore': item['proscore'],'max': item['max'],'min': item['min'],'min_section': item['min_section'],'average': item['average'],'filing': item['filing'],'year':item['year']}
                # print(item)
                cl.replace_one(flt, item, True)
            # logging.info('Crawl %d records  - URL %s', COUNT, url_path)   
        except:
            logging.error('some error - URL %s', url)  
            # pass
    

    # 抓取学校分数线数据
    def runSchoolScore(self):
        cl_school_score = self.db["school_score_data"]
        cl_school_score.create_index([('school_id', ASCENDING),('type',ASCENDING),('batch',ASCENDING),('xclevel',ASCENDING),('zslx_name', ASCENDING),('province_id', ASCENDING),('type_control',ASCENDING),('batch_control',ASCENDING),('proscore',ASCENDING),('max',ASCENDING),('min',ASCENDING),('min_section',ASCENDING),('average',ASCENDING),('filing',ASCENDING),('year', ASCENDING)], unique=True)

        
        # https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/102/52/1/1.json
        school_score_link_list = self.schoolScoreLink()

        tasks = []

        # startTime = datetime.datetime.now()
        # print("任务开始 : %s" % startTime)
        for school_score_link in school_score_link_list:
            url = school_score_link['link']
            # 执行函数，并传入参数
            task = self.executor.submit(self.spider, url, cl = self.db["school_score_link_data"])
            tasks.append(task)
            for future in as_completed(tasks):
                data_json = future.result()
                self.saveDataSchoolScore(data_json, url, cl_school_score) 


    # 保存学校招生计划数据
    def saveDataEnrollPlan(self, data_json, url, cl):
        try:
            for item in data_json:
                # print(item)
                item['year'] = url.split('/')[6]
                flt = {'school_id':item['school_id'],'special_id':item['special_id'],'type':item['type'],'year':item['year'],'id':item['id'],'spid':item['spid'],'batch':item['batch'],'zslx_name':item['zslx_name'],'province': item['province'],'max': item['max'],'min': item['min'],'min_section': item['min_section'],'average': item['average'],'level1':item['level1'],'level2':item['level2'],'level3':item['level3'],'local_batch_name':item['local_batch_name']}
                # print(item)
                cl.replace_one(flt, item, True)
        except:
            logging.error('some error - URL %s', url)  
            # pass
    # 抓取学校招生计划数据
    def runEnrollPlan(self):
        cl_enroll_plan = self.db["enroll_plan_data"]
        cl_enroll_plan.create_index([('school_id', ASCENDING),('special_id',ASCENDING ),('type',ASCENDING),('id',ASCENDING),('year',ASCENDING),('spid',ASCENDING),('batch',ASCENDING),('zslx_name', ASCENDING),('province', ASCENDING),('max',ASCENDING),('min',ASCENDING),('min_section',ASCENDING),('average',ASCENDING),('level1', ASCENDING),('level2', ASCENDING),('level3', ASCENDING),('local_batch_name',ASCENDING)], unique=True)
        
        # https://static-data.eol.cn/www/2.0/schoolspecialindex/2019/102/11/1/1.json
        enroll_plan_link_list = self.enrollPlanLink()

        tasks = []
        # startTime = datetime.datetime.now()
        # print("任务开始 : %s" % startTime)
        for enroll_plan_link in enroll_plan_link_list:
            url = enroll_plan_link['link']
            # 执行函数，并传入参数
            task = self.executor.submit(self.spider, url, cl = self.db["enroll_plan_link_data"])
            tasks.append(task)
            for future in as_completed(tasks):
                data_json = future.result()
                self.saveDataEnrollPlan(data_json, url, cl_enroll_plan) 

    # 基于aiohttp
    # 公用爬虫
    async def fetch(self, client, uri):
        try:
            async with client.get(uri,headers=self.headers, timeout=60) as resp:
                assert resp.status == 200
                return await resp.json()
        except:
            pass

    # 保存学校分数线数据  v2


    async def SchoolScoreTask(self, uri,  cl_school_score_link, cl_school_score):
        async with aiohttp.ClientSession() as client:
            data_json = await self.fetch(client, uri)
            # print(uri)

            # 更新返回数据
            myquery = { "link": uri}
            newvalues = { "$set": { "responseData": data_json, "check_at":datetime.datetime.utcnow()} }
            print(uri)
            cl_school_score_link.update_one(myquery, newvalues)

            try:
                for item in data_json:
                    flt = {'school_id':item['school_id'],'type':item['type'],'batch':item['batch'],'zslx_name':item['zslx_name'],'province_id': item['province_id'],'xclevel': item['xclevel'],'type_control': item['type_control'],'batch_control': item['batch_control'],'proscore': item['proscore'],'max': item['max'],'min': item['min'],'min_section': item['min_section'],'average': item['average'],'filing': item['filing'],'year':item['year']}
                    
                    cl_school_score.replace_one(flt, item, True)
                # logging.info('Crawl %d records  - URL %s', COUNT, url_path)   
            except:
                logging.error('some error - URL %s', uri)  
                # pass

'''

