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

def schools():
    cl = db["school_data"]
    cl.create_index([('school_id', ASCENDING)], unique=True)         # 添加索引
    
    if(cl.estimated_document_count()==0):
        for i in range(1,100):
            url = ('https://api.eol.cn/gkcx/api/?page=%d&request_type=1&size=30&sort=view_total&uri=apidata/api/gk/school/lists' % i)

            req = urllib.request.Request(
                url, 
                data=None, 
                headers = {
                    'Origin': 'https://gkcx.eol.cn',
                    'Referer': 'https://gkcx.eol.cn/school/566/provinceline',
                    'User-Agent':ua.random}
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
            headers = {
                    'Origin': 'https://gkcx.eol.cn',
                    # 'Referer':'https://gkcx.eol.cn/school/54'
                    'Referer': 'https://gkcx.eol.cn/school/566/provinceline',
                    'User-Agent':ua.random}
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


def schoolScore():
    
    cl = db["school_score_data"]
    cl.create_index([('school_id', ASCENDING),('type',ASCENDING),('batch',ASCENDING),('xclevel',ASCENDING),('zslx_name', ASCENDING),('province_id', ASCENDING),('type_control',ASCENDING),('batch_control',ASCENDING),('proscore',ASCENDING),('max',ASCENDING),('min',ASCENDING),('min_section',ASCENDING),('average',ASCENDING),('filing',ASCENDING),('year', ASCENDING)], unique=True)
    schoolList = schools()
    provinceList = provinces()
    for school in schoolList:
        print('*'*50)
        print('学校名称 - %s' % school['name'])
        schoolId = school['school_id']
        for province in provinceList:
            COUNT = 0
            provinceId = province['provinceid']
            print('省份 - %s' % province['province'])
            for recruit_type in range(1,10):
#                 print(recruit_type)
                for i in range(1,10):
#                     print(i)
                    #url = ('https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/%d/41/1/2.json' % schoolId)
                    url ='https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/{}/{}/{}/{}.json'.format(schoolId,provinceId,recruit_type,i)
                    req = urllib.request.Request(
                        url, 
                        data=None, 
                        headers = {
                                'Origin': 'https://gkcx.eol.cn',
                                'Referer': 'https://gkcx.eol.cn/school/566/provinceline',
                                'User-Agent':ua.random}
                    )

                    f = urllib.request.urlopen(req)
                    if(f.getcode()==200):
                        result = json.loads(f.read().decode('utf-8'))
                        if(result!=''):
                            if( result['code'] == '0000' and result['message'] =='成功'):
                                for item in result['data']['item']:
                                    COUNT = COUNT + 1
            #                                         cl.insert_one(item)
                                    flt = {'school_id':item['school_id'],'type':item['type'],'batch':item['batch'],'zslx_name':item['zslx_name'],'province_id': item['province_id'],'xclevel': item['xclevel'],'type_control': item['type_control'],'batch_control': item['batch_control'],'proscore': item['proscore'],'max': item['max'],'min': item['min'],'min_section': item['min_section'],'average': item['average'],'filing': item['filing'],'year':item['year']}
                                    cl.replace_one(flt, item, True)
            print(str(COUNT))
        time.sleep(randint(1,2))

if __name__=="__main__":
    schoolScore()
    #print(randint(1,5))
