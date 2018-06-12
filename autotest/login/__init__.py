#/usr/bin/env python3
#coding=utf-8
from flask import Blueprint

login_views = Blueprint('login', __name__, url_prefix = '/login')

from autotest.login import login_view


