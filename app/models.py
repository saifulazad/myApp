from app import db

class Product(db.Model):

    id = db.Column(db.Integer , primary_key=True)

    product_name = db.Column(db.String(120), index=True , unique=True,nullable = False)

    price = db.Column(db.Integer,nullable = False)

    amount = db.Column(db.Integer, nullable = False)


    def __repr__(self):
        return '<product_name %r price %r amount  %r>' % (self.product_name, self.price,self.amount)

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
