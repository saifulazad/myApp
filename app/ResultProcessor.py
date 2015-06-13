__author__ = 'azad'
def ComputeResult(categories , booleanAns):
    result = []
    color = []
    category = list(set(categories))
    print category
    assoc_answer=zip(categories,booleanAns)
    print assoc_answer
    for y in category:
     #   print  y
      #  print  y==assoc_answer[0][0]
        total  = len([x for x in assoc_answer if x[0]==y])
        # total  = len([x for x in str(assoc_answer) if x[0]==y])
        total_correct  = len([x for x in assoc_answer if x[0]==y and x[1]==1] )
       # print total
        percent = total_correct* 100.0/float(total)
        if (percent > 50):
            color='success'
        else:
            color='danger'
        result.append((y,percent,color))
    return result
from app.models import *
class ResultProcessor():

    def __init__(self, userId ):
        self.userID = userId



    def get_user_answer(self, answer_list):

        self.answer_list =answer_list

        self.ids = [x[0]  for x in answer_list]

        self.user_ans = [int(x[1])  for x in answer_list]

        self.correct_ans = [Question.query.filter_by(questionID=x).first().correctAnswer for x in self.ids ]

        self.categoriesID = [Question.query.filter_by(questionID=x).first().categoryID for x in self.ids ]

        self.cmpans = [ x[0] == x[1] for x in zip(self.correct_ans,self.user_ans)]

        self.categoriesname = [Category.query.filter_by(ID=x).first().category for x in self.categoriesID ]

        # print self.correct_ans
        #
        # print self.user_ans
        #
        # print  self.cmpans

        return ComputeResult(self.categoriesname , self.cmpans)

    def update_database(self):

         self.solve_ans = [SolveProblems.query.filter_by(userID=self.userID).first().correctAnswer for x in self.ids ]


