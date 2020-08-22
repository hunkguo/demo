
#coding:utf-8
#user
from flask import Blueprint, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, TextField, PasswordField, validators, DateField, StringField, SubmitField, FieldList, FormField
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
 
#自定义表单类
class AddForm(FlaskForm):
    item_list = FieldList(FormField(ItemForm),min_entries =0) #min_entries =3表示有三个同样的ItemForm
    submit = SubmitField("添加")

@user_bp.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()        
    if form.submit.data:
        form.item_list.append_entry()
    elif form.item_list:
        for item in form.item_list:
            if not(item.form.delete.data):
                form.item_list.entries.remove(item)
                break
    return render_template('user/add.html',  form=form)
