# coding:utf-8
from flask_bootstrap import Bootstrap
from flask import Flask,render_template,request,url_for,redirect
from flask_nav import Nav
from flask_nav.elements import *
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from views.user import user_bp
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path='/static', template_folder='templates'
            )
app.config["SECRET_KEY"] = "h63j6h36lkj37j3h74kj457h4k57h547h"  # 或者 app.secret_key = '123456'
Bootstrap(app)

nav=Nav()
nav.register_element('top',Navbar(u'Flask入门',
                                    View(u'主页','home'),
                                    View(u'关于','about'),                                    
                                    Subgroup(u'用户',
                                             View(u'管理','user.index'),
                                             Separator(),
                                             View(u'添加', 'user.add'),
                                    ),
                                    Subgroup(u'项目',
                                             View(u'项目一','about'),
                                             Separator(),
                                             View(u'项目二', 'service'),
                                    ),
))

nav.init_app(app)



app.config["MONGO_URI"] = "mongodb://localhost:27017/bzb"
app.mongo = PyMongo(app)



@app.route('/')
def home():
    return render_template('home.html',title_name = 'welcome')

@app.route('/service')
def service():
    return 'service'

@app.route('/about')
def about():
    return 'about'

@app.template_test('current_link')
def is_current_link(link):
    return link == request.path

class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])

@app.route('/login', methods=['GET', 'POST'])
def register():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.data)
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


app.register_blueprint(user_bp, url_prefix='/user')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)


