
#coding:utf-8
import os, sys
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
    current_page = int(request.args.get('page', 1))        # 当前在第几页
    if(current_page==0):
        current_page=1
    pageCount = 6
    per_page = int(request.args.get('per_page', pageCount))           # 每页几条数据

    # 总页数查询
    count = mongo.db.youtube_video_link.find({'isDownload': True}).count()
    if count%pageCount > 0:
        total_page = int(count/pageCount +1)
    else:
        total_page = int(count/pageCount)
    if(current_page > total_page):
        current_page = total_page

    # 分页查询
    list = mongo.db.youtube_video_link.find({'isDownload': True}).sort([('_id', -1)]).skip(per_page*(current_page-1)).limit(pageCount)

    return render_template('youtubeVideoToAudio/index.html', title_name='播放列表', list=list, total_page=total_page, current_page=current_page)

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
        videoId = row['videoId']
        videoLink = row['link']

    

    return render_template('youtubeVideoToAudio/player.html', title_name=videoTitle, videofile=videoFile, videoId=videoId, videoLink=videoLink)

@youtubeVideoToAudio_bp.route('/delete', methods=['GET'])
def deleteVideo():
    video_id = request.args.get('id')
    flt = {'videoId': video_id}
    mongo = current_app.mongo
    videoId = ''
    videoFile = ''
    for row in mongo.db.youtube_video_link.find(flt):
        videoFile = row['downloadFile']
        videoId = row['videoId']
    try:
        mediaDir = current_app.root_path+current_app.static_url_path+"/media/"
        for root, dirs, files in os.walk(mediaDir):
            for filename in files:
                name = os.path.splitext(filename)[0]
                if(name == videoId):
                    os.remove(os.path.join(root, filename))
        mongo.db.youtube_video_link.remove(flt)
    except(FileNotFoundError):
        print("文件不存在")
    
    return redirect(url_for('youtubeVideoToAudio.index'))


