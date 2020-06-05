from __future__ import unicode_literals
import youtube_dl
import requests 
class GetItem(object):

    def rename_hook(self,d):
        # 重命名下载的视频名称的钩子
        if d['status'] == 'finished':
            print(d)
            print('下载完成')

    def download(self,youtube_url):
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
            'outtmpl': '%(id)s.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            
            # 只下载视频
            # result = ydl.download([youtube_url])

            # 下载并获取视频信息
            info_dict = ydl.extract_info(youtube_url, download=True)
            video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            video_title = info_dict.get('title', None)

            r = requests.post('http://httpbin.org/post', json={"key": "value"})
>>> r.status_code
 print(video_title)
            print(video_id)


if __name__ == '__main__':
    # 
    # import requests module 
    response = requests.get('http://106.55.33.30:5000/api/nodownloadvideolist')
    videolist = response.json()

    getItem =  GetItem()
    for l in videolist:
        print(l['link'])
        getItem.download(l['link'])
        