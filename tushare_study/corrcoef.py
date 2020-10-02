#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 07:47:14 2017

@author: 柯西君_BingWong， 瘾金融
"""
import tushare as ts
from pandas import DataFrame

'''老版接口
#先建立一个字典，用来存储股票对应的价格
all_data = {} 
#遍历list里面的股票，可以写入多个股票
for ticker in ['601398', '601939', '601857', '600028']:
    #获取各股票某时段的价格
    all_data[ticker] = ts.get_k_data(ticker, '2015-01-01', '2017-05-26')
#用for循环遍历股票价格并转换为dataframe的形式
price = DataFrame({tic: data['close']
                    for tic, data in all_data.items()})
#计算股票价格每日变化
returns = price.pct_change()
#计算相关性
corr=returns.corr()
#计算协方差
cov=returns.cov()

print(corr)
print(cov)
'''



class tickerData:
    def __init__ (self):
    	ts.set_token('d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b')
    	self.pro = ts.pro_api()
        
    def run(self):
    	
    	df = ts.pro_bar(ts_code='601398.sh', start_date='20200901',end_date='20200930',freq='D', factors='vr')
    	print(df)

if __name__ == "__main__":
    
    s = tickerData()
    s.run()
    #print('开始交易日为：%s ;结束交易日为：%s ' % (start_date_open, end_date_open))
