
from app import app, csrf
from flask import render_template, session,request, url_for ,redirect
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
        print  y

        total  = len([x for x in str(assoc_answer) if x[0]==y])
        total_correct  = len([x for x in assoc_answer if x[0]==y] and x[1]==1)
        print total
        percent = total_correct/1 * 100.0
        result.append((y,percent))
    return result

@csrf.error_handler
def csrf_error(reason):
    print 'OOOOOOOOOOOOO'
    return render_template('csrf_error.html', reason=reason), 400




@app.route('/')
def index():
    return render_template("base.html")


@app.route('/submit', methods=['GET', 'POST'])
def Next():
    question_list = session["question_list"]
    question = Questiontable.query.filter_by(questionID=question_list[0]).first()
    user_value = request.form.getlist('option1')
    print question.correctAnswer
    if( len(user_value)):
        if (user_value[0] == question.correctAnswer):
            print "well done"
            session["answerList"].append(1)
        else:
            session["answerList"].append(0)

    print(session["answerList"])
    session["question_list_point"]+=1
    question_list = session["question_list"]
    if(len(session["question_list"])>session["question_list_point"]):

        question_no = question_list[session["question_list_point"]]
        question = Questiontable.query.filter_by(questionID=question_no).first()
        return  render_template('question.html',question=question )
        #return  redirect(url_for('/questions/'+ str(session["question_list_point"])))
    else:
        result = ComputeResult(session["question_cat_list"],session["answerList"])
        #session["result"] = [('Verb',20,'danger'),('Tense',60,'success'),('hello',80,'success'),('world',40,'danger'),('test',70,'success')]
        return render_template("result.html",result=result)

@app.route('/questions', methods=['GET', 'POST'])
def Question():

    questions = Questiontable.query.all()
    ln = len(questions)
    categories = [x.category for x in questions]
#    category =set(categories)
 #   for (cat in category):
    session["answerList"] = []
    question_list = random.sample(range(1, ln), 3)
    session["question_list"] = question_list
    question = Questiontable.query.filter_by(questionID=question_list[0]).first()
    category = question.category
    print(category)
    session["question_list_point"] = 0
    return render_template('question.html', question=question)

@app.route('/questions/<id>', methods=['GET', 'POST'])
def QuestionID(id):

    question = Questiontable.query.filter_by(questionID=id).first()

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
