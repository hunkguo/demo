# coding:utf-8
from flask_bootstrap import Bootstrap
from flask import Flask,render_template,request,url_for,redirect
from flask_nav import Nav
from flask_nav.elements import *
from views.keywordRank import keywordRank_bp
from views.youtubeVideoToAudio import youtubeVideoToAudio_bp
from flask_pymongo import PyMongo
from flask_apscheduler import APScheduler
from schedulerTask.newsSpider.jobTushareNews import *

class Config(object):
    JOBS = [
        {
            'id': 'tushareNewsData',
            'func': 'schedulerTask.newsSpider.jobTushareNews:tushareNewsSpiderSchedulerTaskJob',
            'args': '',
            'trigger': {
                'type': 'cron',
                'minute':'*/50'
            }
        },
        {
            'id': 'rssNewsData',
            'func': 'schedulerTask.newsSpider.jobRssNews:rssNewsSpiderSchedulerTaskJob',
            'args': '',
            'trigger': {
                'type': 'cron',
                'minute':'*/5'
            }
        },
        {
            'id': 'downloadYoutubeAndConvertAudio',
            'func': 'schedulerTask.jobYoutubeVideo2audio:youtubeForVideoToAudioSchedulerTaskJob',
            'args': '',
            'trigger': {
                'type': 'cron',
                'minute':'*/13'
            }
        },
    ]

app = Flask(__name__, static_url_path='/static', template_folder='templates'
            )
app.config["SECRET_KEY"] = "h63j6h36lkj37j3h74kj457h4k57h547h"  # 或者 app.secret_key = '123456'
Bootstrap(app)

nav=Nav()
nav.register_element('top',Navbar(u'Hunk\'s WebSite',
                                    View(u'主页','home'),
                                    Subgroup(u'新闻',
                                             View(u'新闻关键字排名','keywordRank.index'),
                                             Separator(),
                                             View(u'新闻列表','keywordRank.newslist'),
                                    ),
                                    Subgroup(u'听视频',
                                             View(u'列表','youtubeVideoToAudio.index'),
                                             Separator(),
                                             View(u'添加','youtubeVideoToAudio.addVideoLink'),
                                    ),
))
nav.init_app(app)


scheduler = APScheduler()
app.config.from_object(Config())
scheduler.init_app(app)
scheduler.start()

app.config["MONGO_URI"] = "mongodb://localhost:27017/db_run_website"
app.mongo = PyMongo(app)



@app.route('/')
def home():
    return render_template('home.html',title_name = 'welcome')



@app.template_test('current_link')
def is_current_link(link):
    return link == request.path


app.register_blueprint(keywordRank_bp, url_prefix='/keywordRank')
app.register_blueprint(youtubeVideoToAudio_bp, url_prefix='/v2a')

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)


