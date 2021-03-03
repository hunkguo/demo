# coding:utf-8
from flask_bootstrap import Bootstrap
from flask import Flask,render_template,request,url_for,redirect
from views.keywordRank import keywordRank_bp
from views.youtubeVideoToAudio import youtubeVideoToAudio_bp
from views.eeoPaper import eeoPaper_bp
from flask_pymongo import PyMongo
from flask_apscheduler import APScheduler
import atexit
import fcntl
from flask_cors import CORS
from views.InvoicingManagementSystems import invoicingManagementSystems_bp
from dbs import mysql_db
from pymongo import MongoClient, ASCENDING


class Config(object):
    JOBS = [
        {
            'id': 'tushareNewsData',
            'func': 'schedulerTask.newsSpider.jobTushareNews:tushareNewsSpiderSchedulerTaskJob',
            'args': '',
            'trigger': 'interval',
            'minutes': 68
        },
        {
            'id': 'rssNewsData',
            'func': 'schedulerTask.newsSpider.jobRssNews:rssNewsSpiderSchedulerTaskJob',
            'args': '',
            'trigger': 'interval',
            'minutes': 18
        },
        {
            'id': 'downloadYoutubeAndConvertAudio',
            'func': 'schedulerTask.jobYoutubeVideo2audio:youtubeForVideoToAudioSchedulerTaskJob',
            'args': '',
            'trigger': 'interval',
            'minutes': 28
        },
        {
            'id': 'downloadEeoSchedulerTaskJob',
            'func': 'schedulerTask.jobDownloadEeo:downloadEeoSchedulerTaskJob',
            'args': '',
            'trigger': {
                'type': 'cron',
                'day_of_week':"sun",
                'hour':'8',
                'minute':'32',
                'second': '0'
            }
        },
    ]

app = Flask(__name__, static_url_path='/static', template_folder='templates'
            )
app.config["SECRET_KEY"] = "h63j6h36lkj37j3h74kj457h4k57h547h"  # 或者 app.secret_key = '123456'
bootstrap = Bootstrap()
bootstrap.init_app(app)


def initAPScheduler(app):
    f = open("scheduler.lock", "wb")
    try:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        scheduler = APScheduler()
        scheduler.init_app(app)
        scheduler.start()
    except:
        pass
    def unlock():
        fcntl.flock(f, fcntl.LOCK_UN)
        f.close()
    atexit.register(unlock)

scheduler = APScheduler()
app.config.from_object(Config())
initAPScheduler(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/db_run_website"
app.mongo = PyMongo(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ims:ghlhj2891@localhost/ims'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
mysql_db.init_app(app)


CORS(app)



Client = MongoClient()
MONGO_HOST = "localhost"
MONGO_PORT = 27017
News_DB_NAME = "db_gaokao"

mc = MongoClient(MONGO_HOST, MONGO_PORT)        # Mongo连接
db = mc[News_DB_NAME]                         # 数据库



 
def str_of_num(num):
    '''
    递归实现，精确为最大单位值 + 小数点后三位
    '''
    def strofsize(num, level):
        if level >= 2:
            return num, level
        elif num >= 10000:
            num /= 10000
            level += 1
            return strofsize(num, level)
        else:
            return num, level
    units = ['', '万', '亿']
    num, level = strofsize(num, 0)
    if level > len(units):
        level -= 1
    return '{}{}'.format(round(num, 3), units[level])



@app.route('/')
def home():
    # 学校分数线
    cl_school_score = db["school_score_data"]
    school_score_data_count = str_of_num(cl_school_score.estimated_document_count())

    # 专业分数线
    cl_major_score_data = db["major_score_data"]
    major_score_data_count = str_of_num(cl_major_score_data.estimated_document_count())

    # 招生计划
    cl_enroll_plan_data = db["enroll_plan_data"]
    enroll_plan_data_count = str_of_num(cl_enroll_plan_data.estimated_document_count())

    # 学校分数线链接
    cl_school_score_link_data = db["school_score_link_data"]
    school_score_link_data_count = str_of_num(cl_school_score_link_data.estimated_document_count())

    # 专业分数线链接
    cl_major_score_link_data = db["major_score_link_data"]
    major_score_link_data_count = str_of_num(cl_major_score_link_data.estimated_document_count())

    # 招生计划链接
    cl_enroll_plan_link_data = db["enroll_plan_link_data"]
    cl_enroll_plan_link_data_count = str_of_num(cl_enroll_plan_link_data.estimated_document_count())

    
    school_score_link_data_new = list(cl_school_score_link_data.find({}).sort('check_at', -1).limit(10))
    
    return render_template('home.html', title_name='Hunk\'s Website', data = {'school_score_data_count':school_score_data_count, 'major_score_data_count':major_score_data_count, 'enroll_plan_data_count':enroll_plan_data_count, 'school_score_link_data_count':school_score_link_data_count, 'major_score_link_data_count':major_score_link_data_count, 'cl_enroll_plan_link_data_count':cl_enroll_plan_link_data_count, 'school_score_link_data_new':school_score_link_data_new})



@app.template_test('current_link')
def is_current_link(link):
    return link == request.path


app.register_blueprint(keywordRank_bp, url_prefix='/keywordRank')
app.register_blueprint(youtubeVideoToAudio_bp, url_prefix='/v2a')
app.register_blueprint(eeoPaper_bp, url_prefix='/eeo')
app.register_blueprint(invoicingManagementSystems_bp, url_prefix='/ims')

    
if __name__ == '__main__':
    with app.app_context():
        #mysql_db.drop_all()
        mysql_db.create_all()
    app.run(host='0.0.0.0', port='5000', debug=True)


