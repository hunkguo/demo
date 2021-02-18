from pymongo import MongoClient, ASCENDING
import multiprocessing

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
    

    cl_school_score_link_data = db["school_score_link_data"]
    data = list(cl_school_score_link_data.find().sort('check_at', -1).limit(100))
    print(len(data))


    print(multiprocessing.cpu_count())