from flask import *
from app import app, user_info
from app import db, models
from regForm import RegistrationForm, LoginForm
from db_reg_user import RegUser
from flask import render_template, flash, redirect, session, url_for, request, g
from user_info import *
# from user_info import Userinfo

from functools import wraps

current_user = None


@app.before_request
def before_request():
    g.user = current_user


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            error = 'No'
            form = None
            return redirect(url_for('login', error=error))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/secret_page')
@login_required
def secret_page():
    form = None
    error = None
    return render_template('reg.html', form=form, error=error)


@app.route('/')
@app.route('/index')
def store():
    return render_template("base.html")


@app.route('/store')
def index():
    return render_template("store.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    error = None
    if request.method == 'POST' and form.validate():
        user = Userinfo(email=form.email.data)

        if user.is_matched(form.email.data, form.password.data):
            session['email'] = form.email.data
            flash('Thanks for Login')
            g.user = session['email']
            print g.user
            return redirect(url_for('index'))
        else:
            error = 'Invalid email or password'
            return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form, error=error)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    error = None
    if request.method == 'POST' and form.validate():
        new_user = RegUser()

        is_contain = new_user.already_exist(email=form.email.data, \
                                            user_name=form.username.data, password=form.password.data)
        if (is_contain == True):
            error = 'User name or email already exist'
            return render_template('reg.html', form=form, error=error)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('reg.html', form=form, error=error)

'''
@app.route('/product/<productname>')
def user(productname):



    user = User.query.filter_by(productname=productname).first()
    if user == None:
        flash('User %s not found.' % productname)
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                           user=user,
                           posts=post)

'''