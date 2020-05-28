# -*- coding:utf-8 -*-
'''
Created on 2019/05/12
@author: Hunk Guo
'''
import datetime,time
import tushare as ts
import numpy as np
import pandas as pd


# 概念
class concept:
    def __init__ (self):
        #self.pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')
        pass

    def run(self):
        # 初始化
        pro = ts.pro_api('d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b')


        #获取单日全部股票数据
        moneyflow = pro.moneyflow(trade_date='20200528',fields='ts_code,net_mf_vol,net_mf_amount')
        #print(moneyflow)

        '''
        ts_code  net_mf_vol  net_mf_amount
        0     600462.SH      -15855        -268.68
        1     601155.SH       -5341       -1651.54
        2     300596.SZ       -5279       -1509.12
        3     300750.SZ       -4989       -7302.78
        4     600593.SH        3219        1361.85
        '''     
        
        # 概念版块净资金注入情况
        df_concept_net_mf_amount = pd.DataFrame(columns=['code', 'net_mf_amount'])
        
        
        # 取所有概念
        concept_list = pro.concept(fields='code,name')

        for concept in concept_list.iterrows():
            #print(concept[1]['code'])
            #print(concept[1]['name'])
            time.sleep(0.3)
            concept_detail = pro.concept_detail(id=concept[1]['code'], fields='ts_code,name')

            concept_amount = pd.merge(moneyflow,concept_detail,on=['ts_code'])
            #print(concept_amount['net_mf_amount'].sum())

            series = pd.Series({"code":concept[1]['code'],'net_mf_amount':concept_amount['net_mf_amount'].sum()},name=concept[1]['name'])

            df_concept_net_mf_amount = df_concept_net_mf_amount.append(series)
            
            print(df_concept_net_mf_amount)
        df_concept_net_mf_amount.to_csv('概念20200528.csv')
            
'''
ts_code  name
0  000937.SZ  冀中能源
1  002080.SZ  中材科技
2  002201.SZ  九鼎新材

'''

        
if __name__ == "__main__":
    
    s = concept()
    s.run()
    #print('开始交易日为：%s ;结束交易日为：%s ' % (start_date_open, end_date_open))

