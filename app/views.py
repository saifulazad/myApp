
from app import app, csrf
from flask import render_template, session,request
import  random
from UploadQuestion import *
from  models import *
def ComputeResult(categories , booleanAns):
    result = []
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
        result.append((y,percent))
    return result

@csrf.error_handler
def csrf_error(reason):
    print 'OOOOOOOOOOOOO'
    return render_template('csrf_error.html', reason=reason), 400




@app.route('/')
def index():
    return render_template("base.html")


@app.route('/upload', methods=['GET', 'POST'])
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
    question_list = random.sample(range(1, ln), 3)
    session["question_list"] = question_list
    question = Questiontable.query.filter_by(questionID=question_list[0]).first()
    category = question.category
    # print category
    session["question_list_point"] = 0
    return render_template('question.html', question=question)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login(request.form)
# #
    print request.method
    if request.method == 'POST' and form.validate_on_submit():
        return render_template('base.html')
        pass
    #print request.method
    return render_template('login.html' , form =form)


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
# @app.route('/questions/<questionsID>')
# def user(questionsID):
#     product = Product.query.filter_by(product_name=questionsID).first()
#     return render_template('info_of_product.html', prduc=product)



#
# def register():
#     form = RegistrationForm(request.form)
#
#     if request.method == 'POST' and form.validate_on_submit():
#
#
#         print form.catalogue_name.data
#         print form.price.data
#         print form.dressid.data
#         print form.catalogue_company.data
#
#         new_product = Product_details(dressid= form.dressid.data, catalogue =form.catalogue.data,
#                 catalogue_name=form.catalogue_name.data,price= form.price.data,
#                 quantity=form.quantity.data, catalogue_company=form.catalogue_company.data,
#                 color=form.color.data,category= form.category.data
#                 )
#
#         db.session.add(new_product)
#         db.session.commit()
#         # flash('Thanks for registering')
#         # return redirect(url_for('login'))
#
#
#     return render_template('reg.html', form=form)












