__author__ = 'azad'

__author__ = 'azad'
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
from  app.models import School
UPLOAD_FOLDER = '/home/azad/myApp/app/static/img'
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    schools = School.query.all()
    for school in schools:
        print school.name

    return render_template('te.html',values=schools)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)