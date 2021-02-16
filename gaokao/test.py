from pymongo import MongoClient, ASCENDING


Client = MongoClient()

MONGO_HOST = "localhost"
MONGO_PORT = 27017
News_DB_NAME = "db_gaokao"


import logging
LOG_FORMAT = "%(message)s"
logging.basicConfig(filename='console.log', level=logging.DEBUG, format=LOG_FORMAT)

if __name__ == '__main__':
    mc = MongoClient(MONGO_HOST, MONGO_PORT)
    db = mc[News_DB_NAME]                   
    schoolList = list(db["school_data"].find())
    provinceList = list(db["province_data"].find())

    for school in schoolList:
        schoolId = str(school['school_id'])
        # print(schoolId)
        logging.info('*'*20)
        school_province_all_count =  len(db['school_score_data'].distinct('province_id', {'school_id':schoolId}))
        school_province_special_all_count =  len(db['school_special_score_data'].distinct('province', {'school_id':schoolId}))
        logging.info('%s    %d      专业  %d', school['name'],school_province_all_count, school_province_special_all_count)
        for province in provinceList:
            provinceId = province['provinceid']
            # print(provinceId)
            
            school_province_count =  db['school_score_data'].count_documents({'school_id':schoolId, 'province_id':provinceId})
            school_province_special_count =  db['school_special_score_data'].count_documents({'school_id':schoolId, 'province':provinceId})
            # print(school_province_count)
            if(school_province_count>0 and school_province_special_count>0):
                logging.info('%-3s    %d      专业  %d', province['province'],school_province_count, school_province_special_count)
            else:
                logging.info('%-3s    %s', province['province']," - ")