from app.models import *

__author__ = 'azad'

from  SelectDropdown import *

class SchoolDropdown(Select_DropDowm):

    def __init__(self):

        Select_DropDowm.__init__(self , 'schoolselect')


        self.schools  =  School.query.all()

        self.id = [school.schoolID for school in self.schools ]
        self.name = [school.name for school in self.schools ]

        self.pair = zip(self.id, self.name)


class CategorieDropdown(Select_DropDowm):

    def __init__(self):

        Select_DropDowm.__init__(self , 'categoryselect')

        self.categories  =  Category.query.all()

        self.id = [ x.ID for x in self.categories]
        self.name = [ x.category for x in self.categories]
        self.pair = zip(self.id, self.name)

class CorrctAnswerDropdown(Select_DropDowm):

    def __init__(self):

        Select_DropDowm.__init__(self , 'correctanswerselect')


        self.pair = zip(range(0,5), range(0,5))

if __name__ == "__main__":

    cate = SchoolDropdown()

    for x in cate.id:
        print  x