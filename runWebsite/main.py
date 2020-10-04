# coding:utf-8
from flask_bootstrap import Bootstrap
from flask import Flask,render_template,request,url_for,redirect
from views.keywordRank import keywordRank_bp
from views.youtubeVideoToAudio import youtubeVideoToAudio_bp
from flask_pymongo import PyMongo
from schedulerTask.newsSpider.jobTushareNews import *


app = Flask(__name__, static_url_path='/static', template_folder='templates'
            )
app.config["SECRET_KEY"] = "h63j6h36lkj37j3h74kj457h4k57h547h"  # 或者 app.secret_key = '123456'
bootstrap = Bootstrap()
bootstrap.init_app(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/db_run_website"
app.mongo = PyMongo(app)



@app.route('/')
def home():
    return render_template('home.html', title_name='Hunk\'s Website')



@app.template_test('current_link')
def is_current_link(link):
    return link == request.path


app.register_blueprint(keywordRank_bp, url_prefix='/keywordRank')
app.register_blueprint(youtubeVideoToAudio_bp, url_prefix='/v2a')

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)


