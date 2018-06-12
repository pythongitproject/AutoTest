#/usr/bin/env python3
#coding=utf-8
from autotest.login import login_views
from flask import render_template,request

@login_views.route('/')
def loginController():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html')