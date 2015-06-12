from app.models import Questiontable

__author__ = 'azad'
import  random

NUM_OF_QUESTION = 10
class ExamQuestions():

    def __init__(self, userID=None, subject=None):

        self.head = 0
        self.userID = userID

        self.subject = subject
        self.randomQuestions = random.sample(range(1,40), NUM_OF_QUESTION)
       # print  self.randomQuestions
        self.questions = ( Questiontable.query.filter_by(questionID=x).first() for x in self.randomQuestions)

        self.useranswer = [0]*NUM_OF_QUESTION


        self.corrcetanswer =[int(float(x.correctAnswer)) for x in self.questions]

        print self.corrcetanswer
        print self.useranswer

    def getQuestion(self):

        question = self.questions[self.head]

        self.head+=1

        return  question

    def setAnswer(self, given_value):
        self.useranswer[self.head-1] = given_value

        
    def is_last_question(self):
        return self.head==NUM_OF_QUESTION

if __name__ == "__main__":
     ob  = ExamQuestions()