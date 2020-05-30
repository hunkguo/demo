from app import db

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
    link = db.Column(db.String(150), unique=True)
    download_status = db.Column(db.Boolean)
    download_time = db.Column(db.Time)
    download_file = db.Column(db.String(256))

