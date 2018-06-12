#/usr/bin/env python3
#coding=utf-8
from flask import Flask
from flask_cors import *
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456a@127.0.0.1/autotest?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
CORS(app, supports_credentials=True)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'


login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)
from autotest.models import UserInfo, InterfaceInfo, TestCase, Plan, Environment
db.init_app(app)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
