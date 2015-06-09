
from app import app, csrf,login_manager
from flask import render_template, session,request
import random
from flask.ext.login import login_user , logout_user , current_user , login_required
from UploadQuestion import *
from models import *
from profile import *
@login_manager.user_loader
def load_user(id):
    return Registertable.query.get(int(id))
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

@csrf.error_handler
def csrf_error(reason):
    print 'OOOOOOOOOOOOO'
    return render_template('csrf_error.html', reason=reason), 400




@app.route('/')
def index():
    return render_template("base.html")

@app.route('/profile', methods=['GET'])
def profile():
#    form = UserProfile(request.form)
#   generating random numbers
    solved=random.sample(range(1, 100), 13)
    tried=random.sample(range(1, 100), 23)
    user = UserProfile('Tanvir','abcd',solved,tried)
    user=['Tanvir','abcd']
    session["user"]=user
    return render_template('profile.html', user=user,solved=solved,tried=tried)

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = QuestionForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():


        question = Questiontable(description =form.description.data, category = form.category.data,
                option1 = form.option1.data,    option2 = form.option2.data,
                option3 = form.option3.data,    option4 = form.option4.data,
                correctAnswer = form.correctAnswer.data)


        db.session.add(question)
        db.session.commit()
        # flash('Thanks for registering')
        # return redirect(url_for('login'))


    return render_template('upload.html', form=form)

@app.route('/submit', methods=['GET', 'POST'])
def Next():

    #session["question_list_point"]
    question_list = session["question_list"]
    qsn_head = session["question_list_point"]
    user_value = request.form.getlist('option1')
    question = Questiontable.query.filter_by(questionID=question_list[qsn_head]).first()

    session["question_cat_list"].append( question.category)
    # print user_value
    # print int(float(question.correctAnswer))
    # print  session["question_cat_list"]
    if( len(user_value)):
        if (int(user_value[0]) == int(float(question.correctAnswer))):
            print "well done"
            session["answerList"].append(1)
        else:
            session["answerList"].append(0)

    # print(session["answerList"])
    qsn_head +=1
    session["question_list_point"] =qsn_head
    if(len(session["question_list"])>qsn_head):


        question = Questiontable.query.filter_by(questionID=question_list[qsn_head]).first()
        return  render_template('question.html',question=question )

    else:
        # print  session["question_cat_list"]
        result = ComputeResult(session["question_cat_list"],session["answerList"])
        return render_template("result.html",result=result)

@app.route('/questions', methods=['GET', 'POST'])
def Question():

    questions = Questiontable.query.all()
    ln = len(questions)

    session["answerList"] = []
    session["question_cat_list"] = []
    question_list = random.sample(range(1, ln), 40)
    session["question_list"] = question_list
    question = Questiontable.query.filter_by(questionID=question_list[0]).first()
    category = question.category
    # print category
    session["question_list_point"] = 0
    return render_template('question.html', question=question)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login(request.form , "Aaas")
# #
    print request.method
    if request.method == 'POST' and form.validate_on_submit():
	login_user(form.user)
	print form.user.email
        return render_template('base.html')
        pass
    #print request.method
    return render_template('login.html' , form =form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("base.html")
#
# @app.route('/questions/<id>', methods=['GET', 'POST'])
# def QuestionID(id):
#
#     question = Questiontable.query.filter_by(questionID=id).first()
#
#     # root_path =  str(request.path).rsplit('/',1)[0]
#     #
#     # user_value = request.form.getlist('option1')
#     # if( len(user_value)):
#     #     print  user_value[0]
#     # print  question.correctAnswer
#     # ln = len(Questiontable.query.all())
#     # path = '/'.join([root_path,str(int(id)%ln+1)])
#     #
#     # print  path
#     # str(1)
#
#     return render_template('question.html',question=question )
@app.route('/questions/<questionsID>')
def user(questionsID):

    question = Questiontable.query.filter_by(questionID=questionsID).first()
    return render_template('question.html', question=question)



# route to register

@app.route('/reg', methods=['GET', 'POST'])
def Register():

    caps = Captcha.query.all()


    cap_img = [caps[random.randrange(0,2)] for x in range(3)]
    d = []
    for x in cap_img:
        d.append ((x.ID , x.src))
    cap_img =  d
    #return render_template("captcha.html",cap_img=d)


    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user_value = request.form.getlist('captcha')
        print user_value
        user = Registertable(name =form.Name.data, email = form.Email.data,
                userID = form.User_Id.data,    institute = form.Institute.data,
                password = form.Password.data)


        db.session.add(user)
        db.session.commit()

    return render_template('reg.html',form=form,cap_img=cap_img )















