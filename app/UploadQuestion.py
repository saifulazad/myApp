from wtforms.validators import Required

__author__ = 'root'
from wtforms import *
from wtforms.fields.html5 import EmailField
from models import *
# from flask_uploads import UploadSet, IMAGES
from flask_wtf import Form


# images = UploadSet('images', IMAGES)

class Login(Form):
    email = StringField('email', [validators.Length(min=2, max=25)])
    password = PasswordField('password', [validators.Length(max=25)])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):

        rv = Form.validate(self)
        if not rv:
            return False

        user = Registertable.query.filter_by(
            email=self.email.data).first()

        if user is None:
            self.email.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user

        return True

    # class LoginForm(Form):


# username = TextField('Username', [validators.Required()])
#     password = PasswordField('Password', [validators.Required()])
#
#     def __init__(self, *args, **kwargs):
#         Form.__init__(self, *args, **kwargs)
#         self.user = None
#
#     def validate(self):
#         rv = Form.validate(self)
#         if not rv:
#             return False
#
#         user = User.query.filter_by(
#             username=self.username.data).first()
#         if user is None:
#             self.username.errors.append('Unknown username')
#             return False
#
#         if not user.check_password(self.password.data):
#             self.password.errors.append('Invalid password')
#             return False
#
#         self.user = user
#         return True

class QuestionForm(Form): \
        description = StringField('description', [validators.Length(min=3, max=175)],
                                  description={'placeholder': 'Description'})
        category = StringField('category', [validators.Length(max=35)], description={'placeholder': 'Category'})
        option1 = StringField('option1', [validators.Length(max=25)], description={'placeholder': 'Option 1'})
        option2 = StringField('option2', [validators.Length(max=35)], description={'placeholder': 'Option 2'})
        option3 = StringField('option3', [validators.Length(max=35)], description={'placeholder': 'Option 3'})
        option4 = StringField('option4', [validators.Length(max=35)], description={'placeholder': 'Option 4'})
        correctAnswer = IntegerField('correctAnswer', description={'placeholder': 'CorrectAnswer'})


class UserProfile(Form):
    Name = StringField('Name', [validators.Length(min=3, max=175)])
    User_Id = StringField('User_Id', [validators.Length(min=4, max=25)])
    School = StringField('School', [validators.Length(min=3, max=175)])
    Class = IntegerField('Class')

    def __init__(self, name, school, solved, tried):
        self.Name = name
        self.School = school
        self.solved = solved
        self.tried = tried


class RegisterForm(Form): \
        Name = StringField('Name', [validators.Length(min=3, max=175)], description={'placeholder': 'Name'})

        Email = EmailField('Email', [validators.Length(max=35), validators.Email()],
                           description={'placeholder': 'Email'})

        User_Id = StringField('User_Id', [validators.Length(min=4, max=25)], description={'placeholder': 'User ID'})

        Institute = IntegerField('Institute', description={'placeholder': 'Institute'})

        Password = PasswordField('Password', [validators.Length(min=1, max=35),
                                              validators.EqualTo('Confirm', message='Passwords must match')]
                                 , description={'placeholder': 'Password'})

        Confirm = PasswordField('Confirm Password', description={'placeholder': 'Confirm Password'})

        gender = RadioField('Gender', choices=[('1', 'Male'), ('0', 'Female')], validators=[Required()])

        # upload = FileField('image', validators=[ FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
        def __init__(self, *args, **kwargs):
            Form.__init__(self, *args, **kwargs)
            print  args
            print kwargs
            self.user = None

        def validate(self):

            rv = Form.validate(self)
            if not rv:
                return False

            user_email = Registertable.query.filter_by(
                email=self.Email.data).first()
            user_ID = Registertable.query.filter_by(
                userID=self.User_Id.data).first()
            if user_email is not None:
                self.Email.errors.append('This Email already Consist')
                return False

            if user_ID is not None:
                self.User_Id.errors.append('This UserID already Consist')
                return False

            print  self.gender.data
            return True
