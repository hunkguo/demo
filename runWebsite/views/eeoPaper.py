
#coding:utf-8
import os, sys
from flask import Blueprint, render_template, redirect, request,url_for
from flask import current_app
import datetime
from flask_pymongo import PyMongo,DESCENDING,ASCENDING
from Object import YoutubeVideo
eeoPaper_bp = Blueprint('eeoPaper',__name__)

@eeoPaper_bp.route('/')
def index():
    mongo = current_app.mongo
    # 每页数据展示
    current_page = int(request.args.get('page', 1))        # 当前在第几页
    if(current_page==0):
        current_page=1
    pageCount = 6
    per_page = int(request.args.get('per_page', pageCount))           # 每页几条数据

    # 总页数查询
    count = mongo.db.eeo_paper.find().count()
    if count%pageCount > 0:
        total_page = int(count/pageCount +1)
    else:
        total_page = int(count/pageCount)
    if(current_page > total_page):
        current_page = total_page

    # 分页查询
    list = mongo.db.eeo_paper.find().sort([('_id', -1)]).skip(per_page*(current_page-1)).limit(pageCount)

    return render_template('eeoPaper/index.html', title_name='经济观察报', list=list, total_page=total_page, current_page=current_page)


@eeoPaper_bp.route('/view', methods=['GET'])
def view():
    pdfId = request.args.get('id')
    print(pdfId)
    flt = {'pdfId': int(pdfId)}
    mongo = current_app.mongo
    for row in mongo.db.eeo_paper.find(flt):
        pdfFile = row['pdfFile']
    return render_template('eeoPaper/view.html', pdfFile=pdfFile)
    #return redirect(url_for('eeoPaper.index'))

@eeoPaper_bp.route('/delete', methods=['GET'])
def delete():

    pdfId = request.args.get('id')
    flt = {'pdfId': int(pdfId)}
    mongo = current_app.mongo
    pdfFile = ''
    for row in mongo.db.eeo_paper.find(flt):
        pdfFile = row['pdfFile']
    try:
        mediaDir = current_app.root_path+current_app.static_url_path+"/eeo_paper/"
        print(pdfFile)
        for root, dirs, files in os.walk(mediaDir):
            for filename in files:
                if(filename == pdfFile):
                    os.remove(os.path.join(root, filename))
        mongo.db.eeo_paper.remove(flt)
    except(FileNotFoundError):
        print("文件不存在")
    
    return redirect(url_for('eeoPaper.index'))



