import os
from flask.helpers import url_for
from werkzeug.utils import secure_filename
from app import app, csrf,login_manager, ALLOWED_EXTENSIONS
from flask import render_template, session,request ,redirect
import random
from flask.ext.login import login_user , logout_user , current_user , login_required
from UploadQuestion import *
from app.PhotoHandler import Photo
from models import *
from profile import *
from werkzeug import secure_filename

class PhotoForm(Form):

    photo = FileField("Your photo")
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

@login_manager.unauthorized_handler
def unauthorized():

    return redirect(url_for('login'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



@app.route('/profile', methods=['GET'])
@login_required
def profile():
#    form = UserProfile(request.form)
#   generating random numbers
    solved=random.sample(range(1, 100), 13)
    tried=random.sample(range(1, 100), 23)
    user = User_profile(session['user_id'])
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
@login_required
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
@login_required
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

@app.route('/', methods=['GET', 'POST'])
def login():
    form = Login()
    if request.method == 'POST' and form.validate_on_submit():

        login_user(form.user)
        print form.user.email
        return redirect(url_for('Question'))

    return render_template('login.html' , form =form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
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
def ExamQuestion(questionsID):

    question = Questiontable.query.filter_by(questionID=questionsID).first()
    return render_template('question.html', question=question)



# route to register

@app.route('/reg', methods=['GET', 'POST'])
def Register():

    # caps = Captcha.query.all()
    #
    #
    # cap_img = [caps[random.randrange(0,2)] for x in range(3)]
    # d = []
    # for x in cap_img:
    #     d.append ((x.ID , x.src))
    # cap_img =  d
    # return render_template("captcha.html",cap_img=d)

    schools = School.query.all()
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():

        file = request.files['file']

        photo = Photo(file)

        url = photo.save(form.User_Id.data)

        user = Registertable(name =form.Name.data, email = form.Email.data,
                userID = form.User_Id.data, schoolID = request.form['select'],
                password = form.Password.data , imgURL = url)


        db.session.add(user)
        db.session.commit()

    return render_template('reg.html',form=form,schools=schools )

from werkzeug import secure_filename
from flask_wtf.file import FileField
@app.route('/up', methods=['GET', 'POST'])
def upload_file():
    WTF_CSRF_ENABLED = False
    if request.method == 'POST':
        file = request.files['file']
        print file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('up.html')














