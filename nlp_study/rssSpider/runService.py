# encoding: UTF-8

"""
定时服务，可无人值守运行，实现每日自动下载更新历史行情数据到数据库中。
"""

import time
import datetime

from dataService import *

if __name__ == '__main__':
    
    # 进入主循环
    while True:
        downloadAllData()
        sleep(600)