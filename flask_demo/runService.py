# encoding: UTF-8
import requests 

"""
定时服务，可无人值守运行。
"""

import time
import datetime

from downloadService import GetVideoItem


if __name__ == '__main__':    
    # 进入主循环
    while True:
        response = requests.get('http://106.55.33.30:5000/api/nodownloadvideolist')
        videolist = response.json()

        getVideoItem =  GetVideoItem()
        for l in videolist:
            #print(l['id'])
            getVideoItem.download(l['id'], l['link'])
   
        print('休息一下...')
        time.sleep(60)
