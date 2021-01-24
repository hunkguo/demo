
#coding:utf-8
#user
from flask import Blueprint, render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import BooleanField, TextField, HiddenField, PasswordField, validators, DateField, StringField, SubmitField, FieldList, FormField, FloatField, DateField
from flask import current_app
from models import EconomicsHousingToCommercialHousing
from flask import flash
import datetime
from dbs import mysql_db
from id_validator import validator
from decimal import *

e2c_bp = Blueprint('e2c',__name__)
 
@e2c_bp.route('/')
def index():
    #e2c_data = e2c.query.all()
    e2c_data = EconomicsHousingToCommercialHousing.query.order_by(EconomicsHousingToCommercialHousing.id.desc())
    return render_template('e2c/list.html', list = e2c_data)
    




from wtforms import Form, BooleanField, TextField, PasswordField, ValidationError

class ValidatorIdentityNumber(Form):
    #__call__函数创建对象之后，系统自动调用,变量from(校验器)和field(字段)分别由wtforms的From自动提供！
    def __call__(self,form, field):
        if not validator.is_valid(field.data):
            raise ValidationError('身份证有误，请重新输入！')
            
#自定义表单类
class e2cForm(FlaskForm):
    id = HiddenField("id", default='0')
    applicantName = StringField("申请人",  validators=[validators.DataRequired(message="请输入申请人姓名"), validators.length(max=50)],render_kw={"placeholder": "请输入申请人姓名"})
    identityNumber = StringField("身份证号",  validators=[ ValidatorIdentityNumber(), validators.DataRequired(message="请输入身份证"),validators.length(max=30)],render_kw={"placeholder": "请输入二代身份证号"})
    communityName = StringField("小区名称", validators=[validators.DataRequired(message="请输入小区名称"), validators.length(max=100)],render_kw={"placeholder": "请输入小区名称"})
    buildingNumber = StringField("楼栋号", validators=[validators.DataRequired(message="请输入楼栋号，必须为数字"), validators.length(max=20)],render_kw={"placeholder": "请输入所在楼栋号"})
    unitNumber = StringField("单元号", validators=[validators.DataRequired(message="请输入单元号，必须为数字"), validators.length(max=20)],render_kw={"placeholder": "请输入所在单元"})
    floorNumber = StringField("楼层号", validators=[validators.DataRequired(message="请输入楼层，必须为数字"), validators.length(max=20)],render_kw={"placeholder": "请输入所在楼层"})
    roomNo = StringField("房号", validators=[validators.DataRequired(message="请输入房号，必须为数字"), validators.length(max=20)],render_kw={"placeholder": "请输入房号"})
    constructionArea = StringField("建筑面积", validators=[validators.DataRequired(message="请输入建筑面积，必须为数字")], default='0',render_kw={"placeholder": "请输入建筑面积"})
    approvedPrice = FloatField("房屋价格", default='0', render_kw={"placeholder": "请输入房价"})
    buildingCompletionDate = DateField("楼栋建成时间", format='%Y-%m-%d', validators=[
            validators.DataRequired(message="日期格式2020-12-7")
        ],
        render_kw={
               "placeholder": "例：2020-12-7"}
        )
    transferRatio = FloatField(label="缴纳土地出让金百分比", default='0.35',render_kw={"placeholder": "请输入申请人姓名"})
    #transferAmount = FloatField("缴纳土地出让金金额")



    submit = SubmitField("保存")

@e2c_bp.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        form = e2cForm()
        id = request.args.get('id', 0, type=int)
        if id!=0:
            e2c_data = EconomicsHousingToCommercialHousing.query.get(id)
            form.id.data = id
            form.applicantName.data = e2c_data.applicantName
            form.identityNumber.data = e2c_data.identityNumber
            form.communityName.data = e2c_data.communityName
            form.buildingNumber.data = e2c_data.buildingNumber
            form.unitNumber.data = e2c_data.unitNumber
            form.floorNumber.data = e2c_data.floorNumber
            form.roomNo.data = e2c_data.roomNo
            form.constructionArea.data = e2c_data.constructionArea
            form.approvedPrice.data = e2c_data.approvedPrice
            form.buildingCompletionDate.data = e2c_data.buildingCompletionDate
            form.transferRatio.data = e2c_data.transferRatio
        return render_template('e2c/edit.html', title_name='添加', form=form)
    else:
        form = e2cForm(formdata=request.form)
        if form.validate():
            if(form.id.data != "0"):
                id = int(form.id.data)
                e2c_data = EconomicsHousingToCommercialHousing.query.get(id)
                e2c_data.applicantName = form.applicantName.data
                e2c_data.identityNumber = form.identityNumber.data
                e2c_data.communityName = form.communityName.data
                e2c_data.buildingNumber = form.buildingNumber.data
                e2c_data.unitNumber = form.unitNumber.data
                e2c_data.floorNumber = form.floorNumber.data
                e2c_data.roomNo = form.roomNo.data
                e2c_data.constructionArea = form.constructionArea.data
                e2c_data.approvedPrice = form.approvedPrice.data
                
                e2c_data.buildingCompletionDate = datetime.datetime.strptime(request.form.get('buildingCompletionDate'), '%Y-%m-%d')
                e2c_data.transferRatio = form.transferRatio.data
                e2c_data.transferAmount = Decimal(e2c_data.approvedPrice) * Decimal(e2c_data.transferRatio)
                mysql_db.session.commit()
            else:
                applicantName = form.applicantName.data
                identityNumber = form.identityNumber.data
                e2c = EconomicsHousingToCommercialHousing(applicantName,identityNumber)
                e2c.communityName = form.communityName.data
                e2c.buildingNumber = form.buildingNumber.data
                e2c.unitNumber = form.unitNumber.data
                e2c.floorNumber = form.floorNumber.data
                e2c.roomNo = form.roomNo.data
                e2c.constructionArea = form.constructionArea.data
                e2c.approvedPrice = form.approvedPrice.data
                
                e2c.buildingCompletionDate = datetime.datetime.strptime(request.form.get('buildingCompletionDate'), '%Y-%m-%d')
                e2c.transferRatio = form.transferRatio.data
                e2c.transferAmount = Decimal(e2c.approvedPrice) * Decimal(e2c.transferRatio)
                mysql_db.session.add(e2c)
                mysql_db.session.commit()

            return redirect(url_for('e2c.index'))
        else:
            flash(form.errors, 'danger')
        return render_template('e2c/edit.html', title_name='添加', form=form)




        
        



