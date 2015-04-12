from app import app
from flask import render_template, request


from UploadQuestion import *
from  models import *

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/questions', methods=['GET', 'POST'])
def Question():

    question = Questions.query.all()
    question = question[0]


    return render_template('question.html', question=question)

@app.route('/questions/<id>')
def QuestionID(id):


    question = Questions.query.filter_by(questionID=id).first()



    return render_template('question.html', question=question)
# @app.route('/questions/<questionsID>')
# def user(questionsID):
#     product = Product.query.filter_by(product_name=questionsID).first()
#     return render_template('info_of_product.html', prduc=product)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = QuestionForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():


        question = Questions(description =form.description.data, category = form.category.data,
                option1 = form.option1.data,    option2 = form.option2.data,
                option3 = form.option3.data,    option4 = form.option4.data,
                correctAnswer = form.correctAnswer.data)


        db.session.add(question)
        db.session.commit()
        # flash('Thanks for registering')
        # return redirect(url_for('login'))


    return render_template('upload.html', form=form)
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