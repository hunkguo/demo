
#coding:utf-8
#user
from flask import Blueprint, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, TextField, PasswordField, validators, DateField, StringField, SubmitField, FieldList, FormField
from flask import current_app
import datetime
from collections import Counter
from flask_pymongo import PyMongo,DESCENDING,ASCENDING
keywordRank_bp = Blueprint('keywordRank',__name__)
 
@keywordRank_bp.route('/index')
def index():
    mongo = current_app.mongo
    # convert your date string to datetime object
    start = datetime.datetime.utcnow().isoformat()
    end = (datetime.datetime.utcnow()-datetime.timedelta(days=1)).isoformat()
    count_frq = Counter()
    useless_eyword = ['11','...','编辑','时间','来源','责任编辑','记者']
    for row in mongo.db.news_data.find({'published': {'$lt': start, '$gte': end }}):
        #print(row['tags'])
        for keyword in row['tags']:
            #print(keyword)
            if keyword in useless_eyword:
                #print(keyword)
                row['tags'].remove(keyword)
        #print(row['tags'])
        count_frq.update(row['tags'])
    return render_template('keywordRank/index.html', title_name='新闻关键字排名', list=count_frq.most_common(100))



@keywordRank_bp.route('/newslist')
def newslist():
    mongo = current_app.mongo
    # convert your date string to datetime object
    start = datetime.datetime.utcnow().isoformat()
    end = (datetime.datetime.utcnow()-datetime.timedelta(days=30)).isoformat()
    # 每页数据展示
    current_page = int(request.args.get('page', 1))        # 当前在第几页
    if(current_page==0):
        current_page=1
    pageCount = 9
    per_page = int(request.args.get('per_page', pageCount))           # 每页几条数据

    # 总页数查询
    count = mongo.db.news_data.find({'published': {'$lt': start, '$gte': end }}).count()
    if count%pageCount > 0:
        total_page = int(count/pageCount +1)
    else:
        total_page = int(count/pageCount)
    if(current_page > total_page):
        current_page = total_page
    # 分页查询
    newslist = mongo.db.news_data.find({'published': {'$lt': start, '$gte': end }}).sort([('published', -1)]).skip(per_page*(current_page-1)).limit(pageCount)

    return render_template('keywordRank/newslist.html', title_name='新闻列表', list=newslist, total_page=total_page, current_page=current_page)
