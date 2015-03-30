import psycopg2

__author__ = 'Azad'

class Product:

     def __init__(self, name , amount , price):
        self.name = name.strip()
        self.amount = amount
        self.price = price


class Product_information:

    def __init__(self):
        self.conn = psycopg2.connect(database="dbname", user="postgres",\
                                password="Azad", host="127.0.0.1", port="9000")

        print "Opened database successfully"
        self.id = None
        self.name = None
        self.price = None
        self.amount = None

    def getPrductAllinfo(self):

        cur = self.conn.cursor()
        productlist= []

        #stmt = 'SELECT * FROM product WHERE productname IN (%s)' % ','.join('%s' for i in productnam)
        stmt = 'SELECT * FROM product'

        #cur.execute(stmt, productnam)
        cur.execute(stmt)
        rows = cur.fetchall()
        for row in rows:
            pro = Product(name = row[1], amount = row[2],price = row[3])

            productlist.append(pro)





        self.conn.close()

        return  productlist





ob = Product_information()

l =ob.getPrductAllinfo()

for x in l:

    print  x.__dict__






