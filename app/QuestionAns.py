__author__ = 'root'
from wtforms import *
from flask.ext.wtf import Form
class TestForm(Form):
    option1 = RadioField(
        'Choice?',
        [validators.Required()],
        choices=[('choice1', 'Choice One'), ('choice2', 'Choice Two')], default='choice1'
    )
# class TestForm(Form):
#
#
#
#    def __init__(self, choices):
#
#         self.option1 = RadioField(
#             'Choice?',
#             [validators.Required()],
#             choices=choices
#         )

class QuestionAnsForm(Form):\

    pass
