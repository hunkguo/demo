from dbs import mysql_db
from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date, DateTime, TIMESTAMP, func, Boolean, DECIMAL
from sqlalchemy.dialects.mysql import FLOAT
from uuid import uuid4
from decimal import *


class identityIdCard(mysql_db.Model):
    
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()), comment='uuid')

    id = mysql_db.Column(mysql_db.Integer, autoincrement=True, primary_key=True)
    # 姓名
    identityName = mysql_db.Column(mysql_db.String(50), nullable=False)
    # 身份证号
    identityNumber = mysql_db.Column(mysql_db.String(30), nullable=False)
    # 出生日期
    dateOfBirth = mysql_db.Column(mysql_db.String(100))
    # 住址
    address = mysql_db.Column(mysql_db.String(200))
    # 性别
    gender = mysql_db.Column(mysql_db.String(20))
    # 民族
    nation = mysql_db.Column(mysql_db.String(20))

    createtime = Column(DateTime, server_default=func.now(), comment='创建时间')
    # onupdate设置自动更改
    updatetime = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='修改时间')

    def __init__(self, identityName, identityNumber):
        self.identityName = identityName
        self.identityNumber = identityNumber

    def __repr__(self):
        return '<EconomicsHousingToCommercialHousing {}>'.format(self.identityName, self.identityNumber)



'''
        print(ocrResult['words_result']['住址']['words'])
        print(ocrResult['words_result']['公民身份号码']['words'])
        print(ocrResult['words_result']['出生']['words'])
        print(ocrResult['words_result']['姓名']['words'])
        print(ocrResult['words_result']['性别']['words'])
        print(ocrResult['words_result']['民族']['words'])
'''