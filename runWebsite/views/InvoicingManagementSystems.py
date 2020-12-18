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
            mysql_db.session.add(Product(ProductSKU,ProductName,0))
            mysql_db.session.commit()
        return redirect(url_for('invoicingManagementSystems.index'))
        


@invoicingManagementSystems_bp.route('/edit', methods=['GET', 'POST'])
def editProduct():    
    if request.method == 'GET':
        product = Product.query.get(request.args.get('id'))
        return render_template('ims/edit.html', title_name='编辑产品', product=product)
    else:        
        ProductSKU = request.form.get('InputSKU')
        ProductName = request.form.get('InputProductName')
        product = Product.query.get(request.form.get('ProductId'))
        product.productSKU = ProductSKU
        product.productName = ProductName
        mysql_db.session.commit()
        return redirect(url_for('invoicingManagementSystems.index'))


@invoicingManagementSystems_bp.route('/purchase', methods=['GET', 'POST'])
def purchaseProduct(): 
    if request.method == 'GET':
        product = Product.query.get(request.args.get('id'))
        return render_template('ims/purchase.html', title_name='进货', product=product)
    else:       
        ProductInstock = request.form.get('InputProductInstock')
        product = Product.query.get(request.form.get('ProductId'))
        product.productInstock = product.productInstock+ int(ProductInstock)
        mysql_db.session.commit()
        return redirect(url_for('invoicingManagementSystems.index'))

@invoicingManagementSystems_bp.route('/sales', methods=['GET', 'POST'])
def salesProduct(): 
    if request.method == 'GET':
        product = Product.query.get(request.args.get('id'))
        return render_template('ims/sales.html', title_name='销货', product=product)
    else:   
        ProductInstock = request.form.get('InputProductInstock')
        product = Product.query.get(request.form.get('ProductId'))
        product.productInstock = product.productInstock - int(ProductInstock)
        mysql_db.session.commit()
        return redirect(url_for('invoicingManagementSystems.index'))

        