from app import app
from flask import render_template, request


from  models import *


@app.route('/store')
def index():
    prducts = Product.query.all()
    print  prducts
    return render_template("store.html",products = prducts)


@app.route('/store/<productname>')
def user(productname):
    product = Product.query.filter_by(product_name=productname).first()


    return render_template('info_of_product.html', prduc=product)
