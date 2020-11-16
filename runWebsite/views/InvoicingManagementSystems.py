#coding:utf-8
# Invoicing management systems
from flask import Blueprint, render_template, redirect, request,url_for
from flask import current_app
import datetime
from models import Product
from dbs import mysql_db

invoicingManagementSystems_bp = Blueprint('invoicingManagementSystems',__name__)

@invoicingManagementSystems_bp.route('/', methods=['GET'])
def index():
    list = Product.query.all()

    return render_template('ims/index.html', title_name='产品列表', list=list)


@invoicingManagementSystems_bp.route('/add', methods=['GET', 'POST'])
def addProduct():    
    if request.method == 'GET':
        return render_template('ims/add.html', title_name='添加产品')
    else:        
        ProductSKU = request.form.get('InputSKU')
        ProductName = request.form.get('InputProductName')    
        if (not Product.query.filter_by(productSku=ProductSKU).first()):
            print('222')   
            mysql_db.session.add(Product(ProductSKU,ProductName))
            mysql_db.session.commit()
        return redirect(url_for('invoicingManagementSystems.index'))
        
        '''
        if (list2):
            return redirect(url_for('invoicingManagementSystems.index'))
        else:
            Product = Product(product_sku=ProductSKU,product_name=ProductName)        
            mysql_db.session.add(Product)
            mysql_db.session.commit()
            return redirect(url_for('invoicingManagementSystems.index'))
        '''
