# -*- coding:utf-8 -*-
'''
Created on 2019/05/12
@author: Hunk Guo
'''
import datetime

import time

def getTushareDate():
	return time.strftime("%Y%m%d", time.localtime());

def tushare2Date(tsDate):
    date = datetime.datetime.strptime(tsDate,'%Y%m%d') 
    return date
        
if __name__ == "__main__":
    print(tushare2Date('20200930'))

