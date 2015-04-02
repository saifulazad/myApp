from app import db





class Product(db.Model):

    id = db.Column(db.Integer , primary_key=True)

    product_name = db.Column(db.String(120), index=True , unique=True,nullable = False)

    price = db.Column(db.Integer,nullable = False)

    amount = db.Column(db.Integer, nullable = False)


    def __repr__(self):
        return '<product_name %r price %r amount  %r>' % (self.product_name, self.price,self.amount)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

