__author__ = 'root'
from wtforms import *
from flask.ext.wtf import Form


class Login(Form):
    email = StringField('email', [validators.Length( max=25)])
    password = PasswordField('password', [validators.Length( max=25)])

class QuestionForm(Form):\

    description = StringField('description', [validators.Length(min = 3, max=175)])

    category = StringField('category', [validators.Length( max=35)])

    option1 = StringField('option1', [validators.Length( max=25)])

    option2 = StringField('option2', [validators.Length( max=35)])

    option3 = StringField('option3', [validators.Length( max=35)])

    option4 = StringField('option4', [validators.Length( max=35)])

    correctAnswer = StringField('correctAnswer', [validators.Length( max=25)])
