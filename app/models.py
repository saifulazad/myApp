from app import db

#create Question model
class Questiontable (db.Model):
    questionID = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.String(300))
    category = db.Column(db.String(100))
    option1 = db.Column(db.String(100))
    option2 = db.Column(db.String(100))
    option3 = db.Column(db.String(100))
    option4 = db.Column(db.String(100))
    correctAnswer = db.Column(db.String(100))

class School(db.Model):
    schoolID = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(300))
    registertable = db.relationship('Registertable', backref='author', lazy='dynamic')

class Registertable (db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(300))
    schoolID = db.Column(db.Integer, db.ForeignKey('school.schoolID'))

    email = db.Column(db.String(100), unique=True)
    userID = db.Column(db.String(300),unique=True)
    password = db.Column(db.String(100))
    gender = db.Column(db.Boolean, unique=False)
    imgURL = db.Column(db.String(100), unique=True)
    solved = db.Column(db.Integer)
    unsolved = db.Column(db.Integer)
    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.ID

    # Required for administrative interface
    def __unicode__(self):
        return self.name
    def check_password(self, password):

	return password == self.password


class Captcha (db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    src = db.Column(db.String(300))
