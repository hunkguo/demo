from dbs import mysql_db
from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date, DateTime, TIMESTAMP, func, Boolean, DECIMAL
from sqlalchemy.dialects.mysql import FLOAT
from uuid import uuid4
from decimal import *


class EconomicsHousingToCommercialHousing(mysql_db.Model):
    
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()), comment='uuid')

    id = mysql_db.Column(mysql_db.Integer, autoincrement=True, primary_key=True)
    # 申请人
    applicantName = mysql_db.Column(mysql_db.String(50), nullable=False)
    # 身份证号
    identityNumber = mysql_db.Column(mysql_db.String(30), nullable=False)
    # 小区名称
    communityName = mysql_db.Column(mysql_db.String(100))
    # 楼号
    buildingNumber = mysql_db.Column(mysql_db.String(20))
    # 单元号
    unitNumber = mysql_db.Column(mysql_db.String(20))
    # 楼层
    floorNumber = mysql_db.Column(mysql_db.String(20))
    # 房号
    roomNo = mysql_db.Column(mysql_db.String(20))
    # 建筑面积
    constructionArea = mysql_db.Column(mysql_db.DECIMAL(10,2), default=0.00)
    # 建成时间
    buildingCompletionDate = mysql_db.Column(mysql_db.Date)
    # 核准价格
    approvedPrice = mysql_db.Column(mysql_db.DECIMAL(10,2), default=0.00)
    # 出让金比例
    transferRatio = mysql_db.Column(mysql_db.DECIMAL(10,2), default=0.00)
    # 出让金额
    transferAmount = mysql_db.Column(mysql_db.DECIMAL(10,0), default=0)

    createtime = Column(DateTime, server_default=func.now(), comment='创建时间')
    # onupdate设置自动更改
    updatetime = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='修改时间')
    is_del = Column(Boolean, default=False, nullable=False, comment='是否删除')

    def __init__(self, applicantName, identityNumber):
        self.applicantName = applicantName
        self.identityNumber = identityNumber

    def __repr__(self):
        return '<EconomicsHousingToCommercialHousing {}>'.format(self.applicantName, self.identityNumber)

    

'''
申请人	身份证号	小区名称	楼栋号	单元号	楼层号	房号	建筑面积	发改部门核定价格	楼栋建成时间（质检部门）	缴纳土地出让金百分比	土地出让金金额
王红艳	411381199002102346	卧龙区经济房一期	1	1	32	03	96.24	215866.32	2016年7月28日	35%	75553 
周贵英	411302198507105745	卧龙区经济房一期	1	1	28	03	96.24	221640.72	2016年7月28日	35%	77574 
刘长军	412901196405110517	卧龙区经济房一期	1	1	8	04	95.08	197100.84	2016年7月28日	35%	68985 
王宗勤	412927197610156360	卧龙区经济房一期	1	1	30	03	96.24	217791.12	2016年7月28日	35%	76227 
郁金玲	411381199305103960	卧龙区经济房一期	1	1	15	04	95.97	219099.51	2016年7月28日	35%	76685 
王平	411303198109052867	卧龙区经济房一期	1	1	25	02	97.13	228546.89	2016年7月28日	35%	79991 









'''