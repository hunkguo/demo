from dbs import mysql_db
from datetime import datetime

class Product(mysql_db.Model):
    id = mysql_db.Column(mysql_db.Integer, autoincrement=True, primary_key=True)
    productSku = mysql_db.Column(mysql_db.String(20), unique=True, nullable=True)
    productName = mysql_db.Column(mysql_db.String(64), nullable=True)
    productInstock = mysql_db.Column(mysql_db.Integer, default=0)

    def __init__(self, productSku, productName, productInstock):
        self.productSku = productSku
        self.productName = productName
        self.productInstock = productInstock

    def __repr__(self):
        return '<Product {}>'.format(self.productSku, self.productName,self.productInstock)

    
    def to_dict(self):
        return {
            "id": self.id,
            "productSku": self.productSku,
            "productName": self.productName,
            "productInstock": self.productInstock,
        }