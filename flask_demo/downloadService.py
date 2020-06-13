from __future__ import unicode_literals
import youtube_dl
import requests 
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
            
            # 只下载视频
            # result = ydl.download([youtube_url])

            # 下载并获取视频信息
            try:
                info_dict = ydl.extract_info(youtube_url, download=True)
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

                r = requests.post('http://10.8.0.6/api/savedownloadvideo', json={"id": id,"title": video_title,"file":video_id+".mp3", "uploader": video_uploader, "channel_url":video_channel_url, "upload_date":video_upload_date, "thumbnail":video_thumbnail, "desc":video_description, "duration":video_duration,"view_count":video_view_count, "like_count":video_like_count, "dislike_count":video_dislike_count, "average_rating":video_average_rating})
            except:
                pass
            #if(r.status_code):
            #    print("success")
            #print(info_dict)


if __name__ == '__main__':
    # 
    # import requests module 
    response = requests.get('http://10.8.0.6/api/nodownloadvideolist')
    videolist = response.json()

    getVideoItem =  GetVideoItem()
    for l in videolist:
        #print(l['id'])
        getVideoItem.download(l['id'], l['link'])

        