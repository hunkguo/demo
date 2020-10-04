# encoding: UTF-8

"""
定时服务，可无人值守运行，
"""

import time
from schedulerTask.jobYoutubeVideo2audio import youtubeForVideoToAudioSchedulerTaskJob
from schedulerTask.newsSpider.jobRssNews import rssNewsSpiderSchedulerTaskJob
from schedulerTask.newsSpider.jobTushareNews import tushareNewsSpiderSchedulerTaskJob
from schedulerTask.newsSpider.jobKeywordCount import keywordCountSchedulerTaskJob

if __name__ == '__main__':
    
    # 进入主循环
    while True:
        print('-'*20)
        print('keyword count')
        print('-'*20)
        keywordCountSchedulerTaskJob()
        time.sleep(10)

        print('-'*20)
        print('download Rss News')
        print('-'*20)
        rssNewsSpiderSchedulerTaskJob()
        time.sleep(60)

        print('-'*20)
        print('download youtube video')
        print('-'*20)
        youtubeForVideoToAudioSchedulerTaskJob()
        time.sleep(120)

        print('-'*20)
        print('download Tushare News')
        print('-'*20)
        tushareNewsSpiderSchedulerTaskJob()
        time.sleep(120)