from app.models import Question

__author__ = 'azad'
import  redis


redis_obj = redis.Redis(host='localhost', port=6379, db=0)

class ExamController():

    def __init__(self, user_id= None):

       self.user_id = user_id
       pass


    def getquestion(self):

        return redis_obj.lpop(self.user_id+'questions')

    def setquestions(self):
        questions = Question.query.all()

        q_id = [qsn.questionID for qsn in questions]

        if redis_obj.exists(self.user_id+'questions') is False:

            for x in q_id:

                print  redis_obj.lpush(self.user_id+'questions',x)

    def setanswer(self):

        if redis_obj.exists(self.user_id+'useranswer') is False:

            pass

if __name__ == "__main__":

    ob = ExamController('OK')

    ob.setquestions()
    ob.getquestion()
