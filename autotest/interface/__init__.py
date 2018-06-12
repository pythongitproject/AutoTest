#/usr/bin/env python3
#coding=utf-8
from flask import Blueprint


if_view = Blueprint('interface', __name__, url_prefix = '/interface')
from autotest.interface import add_view, index_view, edit_view

