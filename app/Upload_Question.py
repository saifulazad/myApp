from app import db
from app.models import Question

__author__ = 'azad'



class Upload_Question():

    def __init__(self, user_id , request , form):

        self.user_id = user_id
        self.request = request
        self.form = form

 # questionID = db.Column(db.Integer,primary_key=True)
 #    description = db.Column(db.String(300))
 #    categoryID = db.Column(db.Integer, db.ForeignKey('category.ID'))
 #    userID = db.Column(db.Integer, db.ForeignKey('registertable.ID'))
 #    option1 = db.Column(db.String(100))
 #    option2 = db.Column(db.String(100))
 #    option3 = db.Column(db.String(100))
 #    option4 = db.Column(db.String(100))
 #    correctAnswer = db.Column(db.Integer)
 #    hint = db.Column(db.String(300))
 #    solvedUser = db.Column(db.Integer)
 #    failedUser = db.Column(db.Integer)
 #    imgURL = db.Column(db.String(300))
 #    dateUploaded = db.Column(db.DateTime)

    def save(self):

        question = Question(description =self.form.description.data, category = self.form.category.data,
                option1 = self.form.option1.data,    option2 = self.form.option2.data,
                option3 = self.form.option3.data,    option4 = self.form.option4.data,
                correctAnswer = self.form.correctAnswer.data)


        db.session.add(question)
        db.session.commit()
