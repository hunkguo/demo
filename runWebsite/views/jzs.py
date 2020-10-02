
#coding:utf-8
#user
from flask import Blueprint, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, TextField, PasswordField, validators, DateField, StringField, SubmitField, FieldList, FormField
from flask import current_app
jzs_bp = Blueprint('jzs',__name__)
 
@jzs_bp.route('/index')
def index():
    mongo = current_app.mongo
    jzs_list = mongo.db.jzs.find()
    return render_template('jzs/index.html', jzs_list=jzs_list)