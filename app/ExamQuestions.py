from app.models import Question
import json
__author__ = 'azad'
import  random

NUM_OF_QUESTION = 10
# def ComputeResult(categories , booleanAns):
#     result = []
#     color = []
#     category = list(set(categories))
#     print category
#     assoc_answer=zip(categories,booleanAns)
#     print assoc_answer
#     for y in category:
#      #   print  y
#       #  print  y==assoc_answer[0][0]
#         total  = len([x for x in assoc_answer if x[0]==y])
#         # total  = len([x for x in str(assoc_answer) if x[0]==y])
#         total_correct  = len([x for x in assoc_answer if x[0]==y and x[1]==1] )
#        # print total
#         percent = total_correct* 100.0/float(total)
#         if (percent > 50):
#             color='success'
#         else:
#             color='danger'
#         result.append((y,percent,color))
#     return result
# from app.models import Question
#
# __author__ = 'azad'
# import  redis
#
#
# redis_obj = redis.Redis(host='localhost', port=6379, db=0)
#
# class ExamController():
#
#     def __init__(self, user_id= None):
#
#        self.user_id = user_id
#        pass
#
#
#     def getquestion(self):
#
#         val = redis_obj.lpop(self.user_id+'questions')
#
#         return Question.query.filter_by(questionID = val).first()
#
#     def setquestions(self):
#         questions = Question.query.all()
#
#         q_id = [qsn.questionID for qsn in questions]
#
#         if redis_obj.exists(self.user_id+'questions') is False:
#
#             for x in q_id:
#
#                 print  redis_obj.lpush(self.user_id+'questions',x)
#
#     def setanswer(self):
#
#         if redis_obj.exists(self.user_id+'useranswer') is False:
#
#             pass
#
#
#
class ExamQuestions():

    def __init__(self, userID=None, subject=None , categories=None):

        self.userID = userID
        self.categories = categories
        self.subject = subject

        self.questions = Question.query.all()


        self.id = [int(float(x.questionID)) for x in self.questions]

    def get_all(self):

        return  self.id

class Hi():

    def __init__(self):
        self.ok = 'OK'
if __name__ == "__main__":
     ob  = Hi()
     ob.ok = 'as'

     print ob.ok