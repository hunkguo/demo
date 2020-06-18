# -*- coding:utf-8 -*-
'''
Created on 2019/05/12
@author: Hunk Guo
'''
import time



def getTushareDate():

	return time.strftime("%Y%m%d", time.localtime());


# 概念
class utils:
    def __init__ (self):
        pass

        
if __name__ == "__main__":
    
    
    print(getTushareDate())

