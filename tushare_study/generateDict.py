#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tushare as ts
from pandas import DataFrame
import sys
import json



class generateDict:
    def __init__ (self):
    	ts.set_token('d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b')
    	self.pro = ts.pro_api()
        
    def run(self):
        df = self.pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,fullname,enname')
        df['enname'].to_csv('excel2txt.txt', sep='\t', index=False)

if __name__ == "__main__":
    
    s = generateDict()
    s.run()
    #print('开始交易日为：%s ;结束交易日为：%s ' % (start_date_open, end_date_open))
