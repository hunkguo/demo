
#coding:utf-8
#user
from flask import Blueprint, render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import BooleanField, FileField,TextField, SelectField, HiddenField, PasswordField, validators, DateField, StringField, SubmitField, FieldList, FormField, FloatField, DateField
from flask import current_app
from models.EconomicsHousingToCommercialHousing import EconomicsHousingToCommercialHousing
from flask import flash
import datetime
from dbs import mysql_db
from id_validator import validator
from decimal import *
from flask_security import  login_required, roles_required

e2c_bp = Blueprint('e2c',__name__)


@e2c_bp.route('/')
@login_required
@roles_required('View')
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
            
from wtforms_components import TimeField, read_only
#自定义表单类
class e2cForm(FlaskForm):
    id = HiddenField("id", default='0')
    applicantName = StringField("申请人",  validators=[validators.DataRequired(message="请输入申请人姓名"), validators.length(max=50)],render_kw={"placeholder": "请输入申请人姓名"})
    identityNumber = StringField("身份证号",  validators=[ ValidatorIdentityNumber(), validators.DataRequired(message="请输入身份证"),validators.length(max=30)],render_kw={"placeholder": "请输入二代身份证号"})
    #communityName = StringField("小区名称", validators=[validators.DataRequired(message="请输入小区名称"), validators.length(max=100)],render_kw={"placeholder": "请输入小区名称"})
    communityName = SelectField(
        '小区名称',
        choices=[
            ('航天居住小区'),
            ('大屯经济房（阳光新城）'),
            ('瑶春居'),
            ('明伦尚书房（淯水花园）'),
            ('北京安居新村'),
            ('风帆小区A区'),
            ('风帆小区B区'),
            ('滨河馨苑'),
            ('地方铁路局一期'),
            ('卧龙区经济房（龙翔世纪家园）一期'),
            ('铁东小区'),
            ('龙港花园'),
            ('南铁嘉园二期'),
            ('西华小区'),
            ('南阳教师小区一期'),
            ('南阳教师小区三期'),
            ('龙城福邸'),
            ('南阳教师小区二期')
        ],
        validators=[validators.DataRequired(message="请输入小区名称"), validators.length(max=100)],render_kw={"placeholder": "请输入小区名称"}
    )
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
@login_required
@roles_required('Input')
@roles_required('Edit')
def edit():
    if request.method == 'GET':
        form = e2cForm()
        uuid = request.args.get('uuid')
        identity_id_card_obj = mysql_db.session.query(identityIdCard).filter(identityIdCard.uuid == uuid).first()
        if(identity_id_card_obj):
            form.applicantName.render_kw = {'readonly': True}
            form.identityNumber.render_kw = {'readonly': True}
            
            
            form.applicantName.data = identity_id_card_obj.identityName
            form.identityNumber.data = identity_id_card_obj.identityNumber


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



class UploadForm(FlaskForm):
    #fileUpload = FileField()
    uploadFileData = HiddenField()

import io
import PIL
from PIL import Image

def size(b64string):
    return  (len(b64string) * 3) / 4 - b64string.count('=', -2)
    #file_size = (len(b64string) * 6 - b64string.count('=') * 8) / 8
    #file_size = len(b64string) * 3 / 4 - b64string.count('=')
    

from werkzeug.utils import secure_filename
from uuid import uuid4
import base64
from werkzeug.datastructures import FileStorage
import requests
from io import BufferedReader
import os
from models.identityIdCard import identityIdCard
@e2c_bp.route('/ocridcrad', methods=['GET', 'POST'])
@login_required
@roles_required('Input')
@roles_required('Edit')
def ocrIdcrad():
    form = UploadForm()
    
    if form.validate_on_submit():
        #print(size(form.uploadFileData.data))
        '''
        filename = str(uuid4())
        form.uploadFileData.data.save('uploads/' + filename)
        print(f'File Size in MegaBytes is {os.path.getsize("uploads/" + filename) / (1024 * 1024)} MB')
        with open('uploads/' + filename, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        '''    
        #print('file_encoded_string:', encoded_string)
        ocrResult = baiduOcr(form.uploadFileData.data)
        #print(ocrResult)
        if(ocrResult['words_result_num'] !=0):
            if( ocrResult['words_result']['姓名']['words']!='' and ocrResult['words_result']['公民身份号码']['words']!=''):
                identityName = ocrResult['words_result']['姓名']['words']
                identityNumber = ocrResult['words_result']['公民身份号码']['words']
                identity_id_card = identityIdCard(identityName,identityNumber)
                identity_id_card.dateOfBirth = ocrResult['words_result']['出生']['words']
                identity_id_card.address = ocrResult['words_result']['住址']['words']
                identity_id_card.gender = ocrResult['words_result']['性别']['words']
                identity_id_card.nation = ocrResult['words_result']['民族']['words']

                identity_id_card_obj = mysql_db.session.query(identityIdCard).filter(identityIdCard.identityName == identityName and identityIdCard.identityNumber==identityNumber).first()

                if(identity_id_card_obj):
                    #identity_id_card_obj.identityNumber = identity_id_card.identityNumber
                    #identity_id_card_obj.identityName = identity_id_card.identityName 
                    identity_id_card_obj.dateOfBirth = identity_id_card.dateOfBirth
                    identity_id_card_obj.address = identity_id_card.address
                    identity_id_card_obj.gender = identity_id_card.gender
                    identity_id_card_obj.nation = identity_id_card.nation
                    mysql_db.session.commit()
                    #print('更新Return identityIdCard uuid %s\n' % identity_id_card_obj.uuid) 
                    identity_id_card_uuid = identity_id_card_obj.uuid
                else:
                    mysql_db.session.add(identity_id_card)
                    mysql_db.session.commit()
                    #print('插入Return identityIdCard uuid %s\n' % identity_id_card.uuid)
                    identity_id_card_uuid = identity_id_card.uuid
                return redirect(url_for('e2c.edit', uuid= identity_id_card_uuid ))
            else:
                return redirect(url_for('e2c.edit' ))


        #print(identityIdCard.query(identity_id_card.identityName==identityName, identityIdCard.identityNumber==identityNumber).first())

        '''




        {'idcard_number_type': 0, 'image_status': 'unknown', 'log_id': 1354278846609752064, 'words_result': {'住址': {'location': {'height': 53, 'left': 112, 'top': 198, 'width': 248}, 'words': '国加利福尼亚州圣芭芭拉市郊Los01ivos镇Neverland'}, '公民身份号码': {'location': {'height': 0, 'left': 0, 'top': 0, 'width': 0}, 'words': ''}, '出生': {'location': {'height': 23, 'left': 122, 'top': 152, 'width': 179}, 'words': '19580829'}, '姓名': {'location': {'height': 24, 'left': 123, 'top': 67, 'width': 147}, 'words': '迈克尔·杰克逊'}, '性别': {'location': {'height': 23, 'left': 131, 'top': 110, 'width': 21}, 'words': '男'}, '民族': {'location': {'height': 0, 'left': 0, 'top': 0, 'width': 0}, 'words': '汉'}}, 'words_result_num': 6}
        '''
        return redirect(url_for('e2c.ocrIdcrad'))
        #return render_template('e2c/ocr.html', form=form)

    return render_template('e2c/ocrIdcrad.html', form=form)



def baiduOcr(b64image):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=UaVDdsMRdASOEL4FEUwDlFyD&client_secret=17u8kCWAQ4YzTAx7eG2lyxIiFtiO2eRd'
    response = requests.get(host)
    if response:
        #print(response.json())
        access_token = (response.json())['access_token']
        '''
        身份证识别
        '''
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
        params = {"id_card_side":"front","image":b64image}
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            return (response.json())










