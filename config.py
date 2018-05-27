#encoding: utf-8
#配置文件
import os
import pymysql
pymysql.install_as_MySQLdb()


DEBUG=True
SECRET_KEY=os.urandom(24)

DIALECT='mysql'
DRIVER='mysqldb'
USERNAME='root'
PASSWORD='root'
HOST='127.0.0.1'
PORT='3306'
DATABASE='zlktqa_demo'

DB_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,
                                             DRIVER,
                                             USERNAME,
                                             PASSWORD,
                                             HOST,
                                             PORT,
                                             DATABASE)
SQLALCHEMY_DATABASE_URI=DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS=False