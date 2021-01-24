# 导入pandas包
import pandas as pd
import numpy as np

folderName = "./importData/"
fileName = "longxiang.xlsx"

#导入标题行
cols = pd.read_excel(folderName+fileName, engine="openpyxl", usecols=[2,3,4,5,6,7,8,9,10,11,12], header=None,nrows=2).values[1] # read first row

import_data = pd.read_excel(folderName+fileName, engine="openpyxl", usecols=[2,3,4,5,6,7,8,9,10,11,12],  header=None, skiprows=2) # skip 1 row

#赋值标题
import_data.columns = cols

#删除NA数据
import_data.dropna(inplace=True)
#或者
#df = df.dropna(axis=0,how='any')


# 显示前10行数据
#print(import_data)

import datetime
from dbs import mysql_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import EconomicsHousingToCommercialHousing


DB_USER = "bzb_manage_system"
DB_NAME = "bzb_manage_system"
DB_PASSWORD ="ghlhj2891"
engine = create_engine('mysql+pymysql://'+ DB_USER +':'+ DB_PASSWORD +'@localhost/'+DB_NAME, max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()



e2c_data = []
for index, row in import_data.iterrows():
    applicantNmae = row["申请人"]
    identityNumber = row["身份证号"]
    e2c = EconomicsHousingToCommercialHousing(applicantNmae,identityNumber)
    e2c.communityName = row["小区名称"]
    e2c.buildingNumber = row["楼栋号"]
    e2c.unitNumber = row["单元号"]
    e2c.floorNumber = row["楼层号"]
    e2c.roomNo = row["房号"]
    e2c.constructionArea = row["建筑面积"]
    e2c.approvedPrice = row["发改部门核定价格"]
    d = datetime.datetime.strptime(row["楼栋建成时间（质检部门）"], '%Y年%m月%d日')
    e2c.buildingCompletionDate = d.strftime("%Y-%m-%d")
    e2c.transferRatio = row["缴纳土地出让金百分比"]
    e2c.transferAmount = e2c.approvedPrice * e2c.transferRatio
    e2c_data.append(e2c)

#print(e2c_data)
#session.add(obj)
#add_all 列表形式
session.add_all(e2c_data)
#提交
session.commit()
