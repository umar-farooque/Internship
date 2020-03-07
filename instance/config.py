import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

SECRET_KEY = 'Sm9obiBTfdfdfsdsfgf5656776jhjjkhlhkljgY2hyb20ga2lja3MgYXNz'
STRIPE_API_KEY = ''
SQLALCHEMY_DATABASE_URI = "mysql://root@localhost/fledge?unix_socket=/var/run/mysqld/mysqld.sock"
# 
# 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DEBUG = True
SQLALCHEMY_ECHO = True

