import os
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Azad@localhost:9000/dbname'
SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


print basedir

print SQLALCHEMY_DATABASE_URI

print  SQLALCHEMY_MIGRATE_REPO
