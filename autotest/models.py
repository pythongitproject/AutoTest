#/usr/bin/env python3
#coding=utf-8
import datetime
from autotest import db


class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    telno = db.Column(db.String(11),nullable=False,unique=True)
    type = db.Column(db.String(10),default=0)
    error_count = db.Column(db.Integer,default=0)
    status = db.Column(db.String(10),default=0)
    add_date = db.Column(db.DateTime,default=datetime.datetime.now())


class InterfaceInfo(db.Model):
    __tablename__ = 'interfaceinfo'
    id = db.Column(db.String(100), primary_key=True)
    if_name = db.Column(db.String(100), nullable=False)
    if_url = db.Column(db.String(100), nullable=False)
    if_method = db.Column(db.String(10), nullable=False)
    if_type = db.Column(db.String(10), nullable=False)
    request_header_data = db.Column(db.Text,nullable=True)
    request_body_data = db.Column(db.Text, nullable=True)
    # body_type = db.Column(db.String(10), nullable=True,default="")
    group_id = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.String(100), nullable=True)
    add_date = db.Column(db.DateTime,default=datetime.datetime.now(),nullable=True)


class TestCase(db.Model):
    __tablename__ = 'testcase'
    id = db.Column(db.String(100), primary_key=True)
    case_name = db.Column(db.String(100), nullable=True)
    case_dec = db.Column(db.Text, nullable=True)
    case_content = db.Column(db.Text, nullable=False)
    case_status = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(100), nullable=True)
    add_date = db.Column(db.DateTime, nullable=False)

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.String(100), primary_key=True)
    task_name = db.Column(db.String(100), nullable=True)
    task_type = db.Column(db.Text, nullable=False)
    task_time = db.Column(db.DateTime, nullable=False)
    task_status = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(100), nullable=True)
    add_date = db.Column(db.DateTime, nullable=False)

class Plan(db.Model):
    __tablename__ = 'plan'
    id = db.Column(db.String(100), primary_key=True)
    env_id = db.Column(db.String(100), nullable=False)
    plan_dec = db.Column(db.Text, nullable=True)
    plan_content = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.String(100), nullable=True)
    add_date = db.Column(db.DateTime, default=datetime.datetime.now())

class PlanDetail(db.Model):
    __tablename__ = 'plan_detail'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    plan_id = db.Column(db.String(100),nullable=True)
    status = db.Column(db.String(10), nullable=False)
    add_date = db.Column(db.DateTime, default=datetime.datetime.now())
    update_date = db.Column(db.DateTime, default=datetime.datetime.now())

class Master(db.Model):
    __tablename__ = 'master'
    id = db.Column(db.String(100), primary_key=True)
    ms_name = db.Column(db.String(50), nullable=True)
    ms = db.Column(db.String(50), nullable=True)
    add_date = db.Column(db.DateTime)

class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.String(100), primary_key=True)
    group_name = db.Column(db.String(50), nullable=True)
    add_date = db.Column(db.DateTime)

class Environment(db.Model):
    __tablename__ = 'environment'
    id = db.Column(db.String(100), primary_key=True)
    env_name = db.Column(db.String(100), nullable=True)
    env_dec = db.Column(db.Text, nullable=True)
    env_ip = db.Column(db.String(100), nullable=False)
    env_port = db.Column(db.String(10), nullable=False)
    env_sec = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.String(100), nullable=True)
    add_date = db.Column(db.DateTime, default=datetime.datetime.now())
