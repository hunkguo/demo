# -*- coding:utf-8 -*-
from pymongo import MongoClient, ASCENDING
from Object import YoutubeVideo
import json,youtube_dl
from datetime import datetime

# 加载配置
config = open('./schedulerTask/config.json')
#config = open('config.json')
setting = json.load(config)

MONGO_HOST = setting['MONGO_HOST']
MONGO_PORT = setting['MONGO_PORT']
News_DB_NAME = setting['News_DB_NAME']
RSS_SOURCE = setting["RSS_SOURCE"]
RSS_HOTS = setting["RSS_HOTS"]

mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
db = mc[News_DB_NAME]                         # 数据库


class GetVideoItem(object):

    def rename_hook(self,d):
        # 重命名下载的视频名称的钩子
        if d['status'] == 'finished':
            pass

    def download(self, id, youtube_url):
        # 定义某些下载参数
        ydl_opts = {
            'progress_hooks': [self.rename_hook],
            # 格式化下载后的文件名，避免默认文件名太长无法保存
            
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'postprocessor_args': [
                '-ar', '16000'
            ],
            'prefer_ffmpeg': True,
            'keepvideo': True,
            'outtmpl': './static/media/%(id)s.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:      
            info_dict = ydl.extract_info(youtube_url, download=True)                
            youtubeVideo = YoutubeVideo()                
            video_id = info_dict.get("id", None)
            youtubeVideo.link = youtube_url
            youtubeVideo.videoId = info_dict.get("id", None)
            youtubeVideo.videoTitle = info_dict.get('title', None)
            # 作者
            youtubeVideo.videoUploader = info_dict.get('uploader', None)
            # 频道
            youtubeVideo.videoChannelUrl = info_dict.get('channel_url', None)
            # 上传时间
            youtubeVideo.videoUploadDate = info_dict.get('upload_date', None)
            # 缩略图
            youtubeVideo.videoThumbnail = info_dict.get('thumbnail', None)
            # 简介
            youtubeVideo.videoDescription = info_dict.get('description', None)
            # 时长
            youtubeVideo.videoDuration = info_dict.get('duration', None)
            # 播放量
            youtubeVideo.videoViewCount = info_dict.get('view_count', None)
            # 点赞量
            youtubeVideo.videoLikeCount = info_dict.get('like_count', None)
            # 不喜欢数量
            youtubeVideo.videoDislikeCount = info_dict.get('dislike_count', None)
            # 平均星级
            youtubeVideo.videoAverageRating = info_dict.get('average_rating', None)


            youtubeVideo.isDownload = True
            youtubeVideo.downloadDate = datetime.now()
            youtubeVideo.downloadFile = video_id+".mp3"
            


            
            cl = db["youtube_video_link"]
            d = youtubeVideo.__dict__
            flt = {'_id': id}
            cl.replace_one(flt, d, True)

     
def youtubeForVideoToAudioSchedulerTaskJob():
    cl = db["youtube_video_link"]
    video_list =cl.find({'isDownload': False})
    getVideoItem =  GetVideoItem()
    for l in video_list:
        getVideoItem.download(l['_id'], l['link'])
        break


if __name__ == "__main__":
    youtubeForVideoToAudioSchedulerTaskJob()
'''
https://www.youtube.com/watch?v=QxXLu56I_Ag
https://www.youtube.com/watch?v=ZJTvCeLrz8w
https://www.youtube.com/watch?v=zlUY-KwDM-U
https://www.youtube.com/watch?v=eETdszLXCGo
https://www.youtube.com/watch?v=F43TsaGho7Y
https://www.youtube.com/watch?v=OK0-5KKWkSE
'''


