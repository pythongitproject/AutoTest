#/usr/bin/env python3
#coding=utf-8
from flask import Blueprint
home_views = Blueprint('home', __name__, url_prefix = '/')
from autotest.home import home_view