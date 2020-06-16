# encoding: UTF-8
import requests 
import random

"""
定时服务，可无人值守运行。
"""

import time
import datetime

from downloadService import GetVideoItem


if __name__ == '__main__':    
    # 进入主循环
    while True:
        sleepTime = random.randint(30,60)
        try:
            response = requests.get('http://192.168.30.55/api/nodownloadvideolist')
            videolist = response.json()

            getVideoItem =  GetVideoItem()
            for l in videolist:
                #print(l['id'])
                getVideoItem.download(l['id'], l['link'])
                print('休息一下...%s秒' % sleepTime)
                time.sleep(sleepTime)
        except:
            print('有异常，休息一下...%s秒' % sleepTime)
            time.sleep(sleepTime)
