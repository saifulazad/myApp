from app import app
from flask import render_template

import os
from flask import Flask, url_for, redirect, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from wtforms import form, fields, validators
# import flask_admin as admin
# import flask_login as login
# from flask_admin.contrib import sqla
# from flask_admin import helpers, expose
# from werkzeug.security import generate_password_hash, check_password_hash
from  models import *


# current_user = None
#
#
# @app.before_request
# def before_request():
#     g.user = current_user
#
#
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if g.user is None:
#             error = 'No'
#             form = None
#             return redirect(url_for('login', error=error))
#         return f(*args, **kwargs)
#
#     return decorated_function
#
#
# @app.route('/secret_page')
# @login_required
# def secret_page():
#     print  'Hi' + g.user
#     form = None
#     error = None
#     return render_template('reg.html', form=form, error=error)
#
@app.route('/in')
def AJS():
    return render_template("Ajs.html")
@app.route('/')
def store():
    return render_template("store.html")


@app.route('/store')
def index():
    prducts = Product.query.all()


    return render_template("store.html",products = prducts)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm(request.form)
#     error = None
#     if request.method == 'POST' and form.validate():
#         user = Userinfo(email=form.email.data)
#
#         if user.is_matched(form.email.data, form.password.data):
#             session['email'] = form.email.data
#             flash('Thanks for Login')
#             g.user = session['email']
#             print g.user
#             return redirect(url_for('index'))
#         else:
#             error = 'Invalid email or password'
#             return render_template('login.html', form=form, error=error)
#     return render_template('login.html', form=form, error=error)

#
# @app.route('/form')
# def form():
#     return render_template('form.html')
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm(request.form)
#     error = None
#     if request.method == 'POST' and form.validate():
#         new_user = RegUser()
#
#         is_contain = new_user.already_exist(email=form.email.data, \
#                                             user_name=form.username.data, password=form.password.data)
#         if (is_contain == True):
#             error = 'User name or email already exist'
#             return render_template('reg.html', form=form, error=error)
#         flash('Thanks for registering')
#         return redirect(url_for('login'))
#     return render_template('reg.html', form=form, error=error)

@app.route('/store/<productname>')
def user(productname):
    product = Product.query.filter_by(product_name=productname).first()


    return render_template('info_of_product.html', prduc=product)
