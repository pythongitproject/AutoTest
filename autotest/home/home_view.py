#/usr/bin/env python3
#coding=utf-8
from autotest.home import home_views
from flask import render_template

@home_views.route('/')
def add():
    return render_template('login.html')

@home_views.route('/login')
def login():
    return render_template('login.html')

@home_views.route('/edit')
def edit():
    return render_template('edit.html')

@home_views.route('/index')
def index():
    return render_template('index.html')

@home_views.route('/test')
def test():
    return render_template('test.html')


@home_views.route('/test1')
def test1():
    while True:
        import datetime, time
        str1 = str(datetime.datetime.now())
        time.sleep(3)
        return str1


