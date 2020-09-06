import pandas as pd
import pymongo


df = pd.read_excel (r'地方铁路局总表.xlsx')
# print (df)


# 打印列名
''' 1
for col in df.columns:
    print(col)
'''
''' 2
print(list(df.columns))

# ['序号', '档案编号', '申请人', '身份证号', '小区名称', '楼栋号', '单元号', '楼层号', '房号', '建筑面积', '发改部门核定价格', '楼栋建成时间（质检部门）', '缴纳土地出让金百分比', '土地出让金金额', 'Unnamed: 14']
'''


mongo = pymongo.MongoClient("mongodb://localhost:27017")

for index,row in df.iterrows():
    '''
    print(row['档案编号'])
    print(row['小区名称'])
    print(row['楼栋号'])
    print(row['单元号'])
    print(row['楼层号'])
    print(row['房号'])
    print(row['建筑面积'])
    print(row['发改部门核定价格'])
    print(row['楼栋建成时间（质检部门）'])
    print(row['缴纳土地出让金百分比'])
    print(row['土地出让金金额'])
    print(row['申请人'])
    print(row['身份证号'])
    '''
    
    jsf_dftlj_org_data = {'档案编号':row['档案编号'], '家庭成员':[{'申请人':row['申请人'], '身份证号':row['身份证号']}], '小区名称':row['小区名称'], '楼栋号':row['楼栋号'], '单元号':row['单元号'], '楼层号':row['楼层号'], '房号':row['房号'], '建筑面积':row['建筑面积'], '发改部门核定价格':row['发改部门核定价格'], '楼栋建成时间':row['楼栋建成时间（质检部门）'], '缴纳土地出让金百分比':row['缴纳土地出让金百分比'], '土地出让金金额':row['土地出让金金额']}
    print(jsf_dftlj_org_data)
    mongo.bzb.jzs.insert_one(jsf_dftlj_org_data)
