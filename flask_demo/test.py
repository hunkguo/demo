from __future__ import unicode_literals
import youtube_dl
class GetItem(object):

    def rename_hook(self,d):
        # 重命名下载的视频名称的钩子
        if d['status'] == 'finished':
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
            'outtmpl': 'foo_%(title)s-%(id)s.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # 下载给定的URL列表
            result = ydl.download([youtube_url])

if __name__ == '__main__':
    getItem =  GetItem()
    getItem.download('https://www.youtube.com/watch?v=1MjRXish6OA')