from main import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User {}>'.format(self.name)

    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class YoutubeVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256))
    videoTitle = db.Column(db.String(256))

    videoUploader = db.Column(db.String(256))
    videoChannelUrl = db.Column(db.String(256))
    videoUploadDate = db.Column(db.String(256))
    videoThumbnail = db.Column(db.String(256))
    videoDescription = db.Column(db.Text)
    videoDuration = db.Column(db.String(256))
    videoViewCount = db.Column(db.String(256))
    videoLikeCount = db.Column(db.String(256))
    videoDislikeCount = db.Column(db.String(256))
    videoAverageRating = db.Column(db.String(256))

    createDate = db.Column(db.DateTime, default=datetime.now)
    isDownload = db.Column(db.Boolean)
    downloadDate = db.Column(db.Time, default=datetime.now, onupdate=datetime.now)
    downloadFile = db.Column(db.String(256))
    __mapper_args__ = {
        "order_by":createDate.desc()
    }
    def __init__(self, link, isDownload):
        self.link = link
        self.isDownload = isDownload
    
    def to_dict(self):
        return {
            "id": self.id,
            "link": self.link,
            "videoFile": self.downloadFile,
            "videoTitle": self.videoTitle,
            "videoUploader": self.videoUploader,
            "videoUploadDate": self.videoUploadDate,
            "videoThumbnail": self.videoThumbnail,
            "videoDescription": self.videoDescription,
            "videoDuration": self.videoDuration,
            "videoViewCount": self.videoViewCount,
            "videoAverageRating": self.videoAverageRating,
        }