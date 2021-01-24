# coding:utf-8
from flask_bootstrap import Bootstrap
from flask import Flask,render_template,request,url_for,redirect
from flask_cors import CORS
from dbs import mysql_db
import datetime
from models.EconomicsHousingToCommercialHousing import EconomicsHousingToCommercialHousing
from models.User import User,Role
from views.EconomicsHousingToCommercialHousing import e2c_bp
from flask_login import login_required,LoginManager,login_user, logout_user
from flask import flash
from urllib.parse import urlparse, urljoin
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_security.utils import encrypt_password
from flask_security import  current_user

app = Flask(__name__, static_url_path='/static', template_folder='templates'
            )
app.config["SECRET_KEY"] = "h63j6h36lkj37j3h74kj457h4k57h547h"  # 或者 app.secret_key = '123456'
bootstrap = Bootstrap()
bootstrap.init_app(app)

DB_USER = "bzb_manage_system"
DB_NAME = "bzb_manage_system"
DB_PASSWORD ="ghlhj2891"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+ DB_USER +':'+ DB_PASSWORD +'@localhost/'+DB_NAME
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
mysql_db.init_app(app)


CORS(app)


@app.route('/')
@login_required
def home():
    if current_user.has_role('Admin'):
        names = current_user
        return render_template('home.html', title_name=names)
    else:
        names = current_user
        return render_template('home.html', title_name=names)
    #return render_template('home.html', title_name='Hunk\'s Website')

# flask-login
from models.User import User

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "main.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page."
login_manager.login_message_category = "info"

@login_manager.user_loader
def load_user(user_id):
    """Load the user's info."""
    from models.User import User
    return User.query.filter_by(id=user_id).first()



from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, validators, DateField, StringField, SubmitField, FormField

class LoginForm(FlaskForm):
    username = StringField('用户名', [validators.DataRequired(), validators.Length(max=255)],render_kw={"placeholder": "请输入用户名"})
    password = PasswordField('密码', [validators.DataRequired()],render_kw={"placeholder": "请输入密码"})
    submit = SubmitField("登录")

    def validate(self):
        """Validator for check the account information."""
        check_validata = super(LoginForm, self).validate()

        # If validator no pass
        if not check_validata:
            return False

        # Check the user whether exist.
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            #self.username.errors.append('Invalid username or password.')
            self.password.errors.append('用户名或密码错')
            return False

        # Check the password whether right.
        if not user.check_password(self.password.data):
            self.password.errors.append('用户名或密码错')
            return False
        return True

from flask import render_template, redirect, request, url_for

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc
           
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user)

        flash("You have been logged in.", category="success")

        flash('Logged in successfully.')

        next = request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return abort(400)

        return redirect(next or url_for('home'))
    return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))    

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for('login'))    

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(mysql_db, User, Role)
security = Security(app, user_datastore)
#SECURITY_PASSWORD_HASH = "bcrypt"
SECURITY_PASSWORD_HASH = "pbkdf2_sha256"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"
# Create a user to test with
@app.before_first_request
def create_user():
    # 创建管理员
    admin_user = user_datastore.create_user(username='admin',password='123456')
    bzb_user = user_datastore.create_user(username = "bzb",password = "123456")
    # 创建普通用户角色和Admin角色
    user_role = user_datastore.create_role(name='User', description='Generic user role')
    admin_role = user_datastore.create_role(name='Admin', description='Admin user role')
    # 为admin添加Admin角色(admin_role)
    user_datastore.add_role_to_user(admin_user, admin_role)
    user_datastore.add_role_to_user(bzb_user, user_role)
    mysql_db.session.commit()




app.register_blueprint(e2c_bp, url_prefix='/e2c')


    
if __name__ == '__main__':
    with app.app_context():
        '''
        '''
        mysql_db.drop_all()
        mysql_db.create_all()

        #导入测试数据

        import pandas as pd
        import numpy as np

        folderName = "./importData/"
        fileName = "longxiang.xlsx"

        #导入标题行
        cols = pd.read_excel(folderName+fileName, engine="openpyxl", usecols=[2,3,4,5,6,7,8,9,10,11,12], header=None,nrows=2).values[1] # read first row

        import_data = pd.read_excel(folderName+fileName, engine="openpyxl", usecols=[2,3,4,5,6,7,8,9,10,11,12],  header=None, skiprows=2) # skip 1 row

        #赋值标题
        import_data.columns = cols

        #删除NA数据
        import_data.dropna(inplace=True)

        e2c_data = []
        for index, row in import_data.iterrows():
            applicantNmae = row["申请人"]
            identityNumber = row["身份证号"]
            e2c = EconomicsHousingToCommercialHousing(applicantNmae,identityNumber)
            e2c.communityName = row["小区名称"]
            e2c.buildingNumber = row["楼栋号"]
            e2c.unitNumber = row["单元号"]
            e2c.floorNumber = row["楼层号"]
            e2c.roomNo = row["房号"]
            e2c.constructionArea = row["建筑面积"]
            e2c.approvedPrice = row["发改部门核定价格"]
            d = datetime.datetime.strptime(row["楼栋建成时间（质检部门）"], '%Y年%m月%d日')
            e2c.buildingCompletionDate = d.strftime("%Y-%m-%d")
            e2c.transferRatio = row["缴纳土地出让金百分比"]
            e2c.transferAmount = e2c.approvedPrice * e2c.transferRatio
            e2c_data.append(e2c)

        #print(e2c_data)
        #session.add(obj)
        #add_all 列表形式
        mysql_db.session.add_all(e2c_data)
        #提交
        mysql_db.session.commit()

        #print(e2c_data)
        #session.add(obj)
        #add_all 列表形式
        mysql_db.session.add_all(e2c_data)
        #提交
        mysql_db.session.commit()

        '''
        # 初始化用户表
        user1 = User(username = "admin",password = "123456")
        user2 = User(username = "bzb",password = "123456")
        mysql_db.session.add(user1)
        mysql_db.session.add(user2)
        # 事务
        mysql_db.session.commit()
        '''

        #user_datastore.create_user(username = "admin",password = "123456")
        #user_datastore.create_user(username = "bzb",password = "123456")



    app.run(host='0.0.0.0', port='5001', debug=True)


