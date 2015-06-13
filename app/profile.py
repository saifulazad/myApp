from app.models import *

sx__author__ = 'Tanvir'

class User_profile:
    def __init__(self,userId):


        #    form = UserProfile(request.form)
#   generating random numbers

        user = Registertable.query.filter_by(ID = userId).first()

        user_school = School.query.filter_by(schoolID = user.schoolID).first()

        self.name = user.name

        self.school = user_school.name

        self.imgURL = user.imgURL

        self.solve_ans = SolveProblems.query.filter_by(userID = userId).first()

        print self.solve_ans
