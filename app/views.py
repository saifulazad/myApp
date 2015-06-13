from flask.helpers import url_for
from app import app, csrf,login_manager
from flask import render_template, session,request ,redirect
import random
from flask.ext.login import login_user , logout_user ,  login_required
from UploadQuestion import *
from app.PhotoHandler import Photo
from app.ResultProcessor import ResultProcessor
from profile import *
from datetime import datetime
from ExamQuestions import *
from  DropDown import *
@login_manager.user_loader
def load_user(id):
    return Registertable.query.get(int(id))


@csrf.error_handler
def csrf_error(reason):
    print 'OOOOOOOOOOOOO'
    return render_template('csrf_error.html', reason=reason), 400

@login_manager.unauthorized_handler
def unauthorized():

    return redirect(url_for('login'))


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
    category = CategorieDropdown()
    correctanswer = CorrctAnswerDropdown()
    if request.method == 'POST' and form.validate_on_submit():
        print request.method
#     questionID = db.Column(db.Integer,primary_key=True)
#     description = db.Column(db.String(300))
#     categoryID = db.Column(db.Integer, db.ForeignKey('category.ID'))
#     userID = db.Column(db.Integer, db.ForeignKey('registertable.ID'))
#     option1 = db.Column(db.String(100))
#     option2 = db.Column(db.String(100))
#     option3 = db.Column(db.String(100))
#     option4 = db.Column(db.String(100))
#     correctAnswer = db.Column(db.Integer)
#     hint = db.Column(db.String(300))
#     solvedUser = db.Column(db.Integer)
#     failedUser = db.Column(db.Integer)
#     imgURL = db.Column(db.String(300))
#     dateUploaded = db.Column(db.DateTime)
        print request.form[category.select_liertal]
        question = Question(description =form.description.data,
                option1 = form.option1.data,    option2 = form.option2.data,
                option3 = form.option3.data,    option4 = form.option4.data,
                correctAnswer = request.form[correctanswer.select_liertal], categoryID = request.form[category.select_liertal],

                userID = session['user_id'], hint = "None" ,solvedUser =0,
                failedUser =0 ,dateUploaded = datetime.now(),
                imgURL = '/'   )


        db.session.add(question)
        db.session.commit()

        return redirect(url_for('upload'))
    return render_template('upload.html', form=form , categories = category, correctanswer = correctanswer )

@app.route('/submit', methods=['GET', 'POST'])
@login_required
def Next():

    user_value = request.form.getlist('option1')
    if len(user_value):
        pair = (request.form['questionID'],user_value[0] )
    else:
        pair = (request.form['questionID'],0 )

    try:
        val = session['tmpquestionsID'].pop(0)

        print session['tmpquestionsID']
        session['useranswer'].append( pair)

        return redirect(url_for('QuestionID',id =val))
    except:
        session['useranswer'].append( pair)
        print session['useranswer']
        return redirect(url_for('Result'))
    # else:
    #
@app.route('/result', methods=['GET'])
@login_required
def Result():

    ob =ResultProcessor(session['user_id'])

    result =ob.get_user_answer(session['useranswer'])
    session.pop('useranswer', None)
    session.pop('tmpquestionsID', None)
    session.pop('questionsID', None)
    return render_template("result.html", result =result)
@app.route('/category', methods=['GET'])
@login_required
def category():

    english_categories = CategorieDropdown()

    print english_categories.select_liertal
    print  english_categories.pair
    return render_template('category.html', english_categories=english_categories)
@app.route('/exam', methods=['GET', 'POST'])
@login_required
def Exam():


     english_categories = CategorieDropdown()

     session['questionsID'] = ExamQuestions().get_all()
     session['tmpquestionsID'] = session['questionsID']
     session['useranswer']= []
     return redirect(url_for('QuestionID',id =session['tmpquestionsID'].pop(0)))

@app.route('/', methods=['GET', 'POST'])
def login():
    form = Login()
    if request.method == 'POST' and form.validate_on_submit():

        login_user(form.user)
        print form.user.email
        return redirect(url_for('upload'))

    return render_template('login.html' , form =form)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
#
@app.route('/questions/<id>', methods=['GET'])
def QuestionID(id):

    question = Question.query.filter_by(questionID=id).first()

    # root_path =  str(request.path).rsplit('/',1)[0]
    #
    # user_value = request.form.getlist('option1')
    # if( len(user_value)):
    #     print  user_value[0]
    # print  question.correctAnswer
    # ln = len(Questiontable.query.all())
    # path = '/'.join([root_path,str(int(id)%ln+1)])
    #
    # print  path
    # str(1)

    return render_template('question.html',question=question )




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
    schools = SchoolDropdown()

    form = RegisterForm(request.form)


    if request.method == 'POST' and form.validate_on_submit():
        file = request.files['file']

        photo = Photo(file)
        url = photo.save(form.User_Id.data)

        user = Registertable(name =form.Name.data, email = form.Email.data,
                userID = form.User_Id.data, schoolID = request.form[schools.select_liertal],
                password = form.Password.data , gender = form.gender.data,imgURL = url,
                unsolved = 0 , solved =0 )

        db.session.add(user)
        db.session.commit()
        return render_template(redirect(url_for("login")))
   # print schools.select_liertal
    return render_template('reg.html',form=form,schools=schools )

# from werkzeug import secure_filename
# from flask_wtf.file import FileField
# @app.route('/up', methods=['GET', 'POST'])
# def upload_file():
#     WTF_CSRF_ENABLED = False
#     if request.method == 'POST':
#         file = request.files['file']
#         print file
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return render_template('up.html')














