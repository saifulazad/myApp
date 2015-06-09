from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username
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


class Registertable (db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(300))
    email = db.Column(db.String(100), unique=True)
    userID = db.Column(db.String(300),unique=True)
    institute = db.Column(db.String(100))
    password = db.Column(db.String(100))
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
