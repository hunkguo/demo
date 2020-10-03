# coding:utf-8
from flask_bootstrap import Bootstrap
from flask import Flask,render_template,request,url_for,redirect
from flask_nav import Nav
from flask_nav.elements import *
from flask_pymongo import PyMongo
import datetime
from collections import Counter

app = Flask(__name__, static_url_path='/static', template_folder='templates'
            )
app.config["SECRET_KEY"] = "h63j6h36lkj37j3h74kj457h4k57h547h"  # 或者 app.secret_key = '123456'
Bootstrap(app)

nav=Nav()
nav.register_element('top',Navbar(u'新闻关键词排名',
                                    View(u'主页','home'),
))

nav.init_app(app)



app.config["MONGO_URI"] = "mongodb://localhost:27017/rssdata"
app.mongo = PyMongo(app)



@app.route('/')
def home():
    # convert your date string to datetime object
    start = datetime.datetime.utcnow().isoformat()
    end = (datetime.datetime.utcnow()-datetime.timedelta(days=6)).isoformat()
    count_frq = Counter()
    useless_eyword = ['11','...']
    for row in app.mongo.db.news.find({'published': {'$lt': start, '$gte': end }}):
        #print(row['tags'])
        for keyword in row['tags']:
            #print(keyword)
            if keyword in useless_eyword:
                #print(keyword)
                row['tags'].remove(keyword)
        #print(row['tags'])
        count_frq.update(row['tags'])
    return render_template('home.html',title_name = '新闻关键词排名', list=count_frq.most_common(20))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)


