# -*- coding:utf-8 -*-
'''
Created on 2019/05/12
@author: Hunk Guo
'''
import datetime,time
import tushare as ts
import numpy as np
import pandas as pd
from utils import getTushareDate
import math
from scipy import stats
import matplotlib.pyplot as plt
from pylab import mpl

# 概念
class concept:
    def __init__ (self):
        #self.pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')
        pass

    def run(self):
        # 初始化
        pro = ts.pro_api('d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b')

        START_DATE = '20170101'
        END_DATE = '20181025'

        #提取股票每日行情
        df1 = pro.daily(ts_code='000001.SZ', start_date=START_DATE, end_date=END_DATE).sort_values(by='trade_date')

        #提取深市指数
        df2 = pro.index_daily(ts_code='399300.SZ', start_date=START_DATE, end_date=END_DATE).sort_values(by='trade_date')

        print(df1)
        #计算贝塔系数
        s1 = df1['pct_chg']
        s2 = df2['pct_chg']
        print((np.cov(s1, s2))[0][1]/np.var(s2))
        print(np.cov(s1, s2))
        print(np.var(s2))

        #计算夏普比率
        df1['ex_pct_close'] = df1['pct_chg'] - 0.04/252
        print((df1['ex_pct_close'].mean() * math.sqrt(252))/df1['ex_pct_close'].std())
            
'''
ts_code  name
0  000937.SZ  冀中能源
1  002080.SZ  中材科技
2  002201.SZ  九鼎新材

'''

        
if __name__ == "__main__":
    mpl.rcParams['font.sans-serif']=['SimHei']
    mpl.rcParams['axes.unicode_minus']=False        
    s = concept()
    s.run()
    #print('开始交易日为：%s ;结束交易日为：%s ' % (start_date_open, end_date_open))



