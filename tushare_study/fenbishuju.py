# -*- coding:utf-8 -*-
'''
Created on 2019/05/12
@author: Hunk Guo
'''
import datetime,time
import tushare as ts
import numpy as np
import pandas as pd


# 
class tushareMain:
    def __init__ (self):
        #self.pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')
        pass

    def run(self):
        # 初始化
        # pro = ts.pro_api('d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b')
        df = ts.get_tick_data('002185',date='2020-06-12',src='tt')
        #print(df)
        print(df[df['volume']>1000].to_string())
        

        
if __name__ == "__main__":
    
    tm = tushareMain()
    tm.run()
    #print('开始交易日为：%s ;结束交易日为：%s ' % (start_date_open, end_date_open))

