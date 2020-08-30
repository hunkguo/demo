
#coding:utf-8
#user
from flask import Blueprint, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, TextField, PasswordField, validators, DateField, StringField, SubmitField, FieldList, FormField
from flask import current_app
user_bp = Blueprint('user',__name__)
 
@user_bp.route('/index')
def index():
    return render_template('user/index.html')
@user_bp.route('/show')
def show():
    return 'user_show'





class ItemForm(FlaskForm):
    content = StringField("内容")
    delete = SubmitField("删除")

class FamilyMemberForm(FlaskForm):
    member_name = StringField("家庭成员姓名")
    member_id_card = StringField("家庭成员身份证号")
    family_relations = StringField("与户主关系")
    family_member_delete = SubmitField("删除")


#自定义表单类
class AddForm(FlaskForm):
    community_name = StringField("小区名称")
    item_list = FieldList(FormField(ItemForm),min_entries =0) #min_entries =3表示有三个同样的ItemForm
    family_member_list = FieldList(FormField(FamilyMemberForm),min_entries =0)
    family_member_add = SubmitField("添加家庭成员")
    submit = SubmitField("保存")

@user_bp.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()        
    if form.family_member_add.data:
        form.family_member_list.append_entry()
    elif form.submit.data:
        family_member_list = []
        for item in form.family_member_list:
            family_member = {}
            family_member['member_name'] = item.form.member_name.data
            family_member['member_id_card'] = item.form.member_id_card.data
            family_member['family_relations'] = item.form.family_relations.data
            family_member_list.append(family_member)
        bzb = {'community_name':form.community_name.data, 'family_member':family_member_list}
        mongo = current_app.mongo
        mongo.db.bzb.insert_one(bzb)
    elif form.family_member_list:
        for item in form.family_member_list:
            if item.form.family_member_delete.data:
                form.family_member_list.entries.remove(item)
                break
                
    
    return render_template('user/add.html',  form=form)
