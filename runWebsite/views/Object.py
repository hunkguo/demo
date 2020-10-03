########################################################################
from datetime import datetime
class BaseData(object):
    def __init__(self):
        """Constructor"""
        pass

 
class NewsData(BaseData):
    def __init__(self):
        """Constructor"""
        super(NewsData, self).__init__()
        self.title = ''       
        self.published = datetime.now()
        self.content = ''    
        self.tags = {}   


class YoutubeVideo(BaseData):
    def __init__(self):
        """Constructor"""
        super(YoutubeVideo, self).__init__()
        self.link = ''
        self.videoTitle = ''
        self.videoUploader = ''
        self.videoChannelUrl = ''
        self.videoUploadDate = ''
        self.videoThumbnail = ''
        self.videoDescription = ''
        self.videoDuration = ''
        self.videoViewCount = ''
        self.videoLikeCount = ''
        self.videoLikeCount = ''
        self.videoDislikeCount = ''
        self.videoAverageRating = ''
        self.createDate = datetime.now()
        self.isDownload = False
        self.downloadDate = datetime.now()
        self.downloadFile = ''