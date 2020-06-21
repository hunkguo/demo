import tushare as ts
import matplotlib.pyplot as plt
from datetime import datetime


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
import seaborn as sns
import seaborn.linearmodels as snsl

# 概念
class stock:
    def __init__ (self):
        #self.pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')
        pass

    def run(self):
        # 初始化
        pro = ts.pro_api('d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b')
        sns.set_style("whitegrid")
        END_DATE = datetime.date.today() #开始时间结束时间，选取最近一年的数据
        START_DATE = datetime.date(END_DATE.year-1,END_DATE.month,END_DATE.day)
        END_DATE = str(END_DATE)[0:10]
        START_DATE = str(START_DATE)[0:10]
        #提取股票每日行情
        stock = pro.daily(ts_code='000001.SZ', start_date=START_DATE, end_date=END_DATE).sort_values(by='trade_date')

        #stock['close'].plot(legend=True ,figsize=(10,4))
        #stock['pct_chg'].plot(legend=True ,figsize=(10,4))
        stock['Daily Return'] = stock['close'].pct_change()
        stock['Daily Return'].plot(legend=True,figsize=(10,4))
        plt.show()


        
if __name__ == "__main__":    
    s = stock()
    s.run()
    #print('开始交易日为：%s ;结束交易日为：%s ' % (start_date_open, end_date_open))



