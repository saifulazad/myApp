import os
from app import ALLOWED_EXTENSIONS, app

__author__ = 'azad'
class Photo():

    def __init__(self,file=None):
        self.file = file



    def __is_allowed_file(self):
         return '.' in self.file.filename and \
             self.file.filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


    def  save(self, name):

        if self.__is_allowed_file():
           # self.name = os.path.join(app.config['UPLOAD_FOLDER'] )+'/'+name+'.'+self.file.filename.rsplit('.', 1)[1]
            self.name = name
            self.file.save(os.path.join(app.config['UPLOAD_FOLDER'], name))



            return self.name
        else : return None


if __name__ == "__main__":

    photo= Photo()

