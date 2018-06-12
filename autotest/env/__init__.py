#/usr/bin/env python3
#coding=utf-8
from flask import Blueprint

env_view = Blueprint('env', __name__, url_prefix = '/env')
from autotest.env import add_view
