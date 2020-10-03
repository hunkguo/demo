
#coding:utf-8
#user
from flask import Blueprint, render_template, redirect, request,url_for
from flask import current_app
import datetime
from flask_pymongo import PyMongo,DESCENDING,ASCENDING
from Object import YoutubeVideo
youtubeVideoToAudio_bp = Blueprint('youtubeVideoToAudio',__name__)

@youtubeVideoToAudio_bp.route('/index')
def index():
    mongo = current_app.mongo
    # 每页数据展示
    page = int(request.args.get('page', 1))        # 当前在第几页
    pageCount = 20
    per_page = int(request.args.get('per_page', pageCount))           # 每页几条数据

    # 总页数查询
    count = mongo.db.youtube_video_link.find({'isDownload': True}).count()
    if count%pageCount > 0:
        total_page = int(count/pageCount +1)
    else:
        total_page = int(count/pageCount)
    # 分页查询
    list = mongo.db.youtube_video_link.find({'isDownload': True}).sort([('_id', -1)]).skip(per_page*(page-1)).limit(pageCount)

    return render_template('youtubeVideoToAudio/index.html', title_name='播放列表', list=list, total_page=total_page)

@youtubeVideoToAudio_bp.route('/add', methods=['GET', 'POST'])
def addVideoLink():    
    if request.method == 'GET':
        return render_template('youtubeVideoToAudio/add.html', title_name='添加视频链接')
    else:
        video_link = request.form.get('InputVideoLink')
        mongo = current_app.mongo
        youtubeVideo = YoutubeVideo()
        youtubeVideo.link = video_link
        d = youtubeVideo.__dict__
        flt = {'link': youtubeVideo.link}
        mongo.db.youtube_video_link.replace_one(flt, d, True)
        
        return redirect(url_for('youtubeVideoToAudio.index'))
    

@youtubeVideoToAudio_bp.route('/palyer', methods=['GET'])
def playerVideo():
    video_id = request.args.get('id')
    flt = {'videoId': video_id}
    mongo = current_app.mongo
    videoTitle = ''
    videoFile = ''
    for row in mongo.db.youtube_video_link.find(flt):
        videoTitle = row['videoTitle']
        videoFile = row['downloadFile']

    

    return render_template('youtubeVideoToAudio/player.html', title_name=videoTitle, videofile=videoFile)


