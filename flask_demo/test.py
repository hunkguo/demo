from __future__ import unicode_literals
import youtube_dl
import requests 
class GetVideoItem(object):

    def rename_hook(self,d):
        # 重命名下载的视频名称的钩子
        if d['status'] == 'finished':
            pass

    def download(self, youtube_url):
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
            
            # 只下载视频
            # result = ydl.download([youtube_url])

            # 下载并获取视频信息
            try:
                info_dict = ydl.extract_info(youtube_url, download=False)
                video_url = info_dict.get("url", None)
                video_id = info_dict.get("id", None)
                video_title = info_dict.get('title', None)
                # 作者
                video_uploader = info_dict.get('uploader', None)
                # 频道
                video_channel_url = info_dict.get('channel_url', None)
                # 上传时间
                video_upload_date = info_dict.get('upload_date', None)
                # 缩略图
                video_thumbnail = info_dict.get('thumbnail', None)
                # 简介
                video_description = info_dict.get('description', None)
                # 时长
                video_duration = info_dict.get('duration', None)
                # 播放量
                video_view_count = info_dict.get('view_count', None)
                # 点赞量
                video_like_count = info_dict.get('like_count', None)
                # 不喜欢数量
                video_dislike_count = info_dict.get('dislike_count', None)
                # 平均星级
                video_average_rating = info_dict.get('average_rating', None)

                print('标题：%s \t 作者：%s \t 频道：%s \t 上传时间：%s \t 缩略图：%s \t 简介：%s \t 时长：%s \t 播放量：%s \t 点赞：%s \t 不喜欢：%s \t 星级：%s \t'% (video_title,video_uploader,video_channel_url,video_upload_date,video_thumbnail,video_description,video_duration,video_view_count,video_like_count,video_dislike_count,video_average_rating) )

            except:
                pass


if __name__ == '__main__':
    getVideoItem =  GetVideoItem()
    getVideoItem.download('https://www.youtube.com/watch?v=xbasNprt4Zk')

        