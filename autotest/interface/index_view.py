#/usr/bin/env python3
#coding=utf-8
from autotest.interface import if_view
from autotest import db
from autotest.models import InterfaceInfo
from autotest.common.utils import AlchemyEncoder
import json
from flask import render_template,jsonify,Response,redirect,request
from autotest.common.utils import AlchemyEncoder


@if_view.route('/list',methods = ['GET'])
def list():
    page = request.args.get('page',default = None)
    if not page:
        page = 1
    else:
        page = int(page)

    if_name = request.args.get('if_name',default = None)
    if if_name:
        scan = '%' + if_name + '%'
        paginate = InterfaceInfo.query\
            .filter(InterfaceInfo.if_name.like(scan)) \
            .order_by(InterfaceInfo.add_date.desc()) \
            .paginate(page=page, per_page=15)
    else:
        if page == 1:
            if_name = None
        paginate = InterfaceInfo.query\
            .order_by(InterfaceInfo.add_date.desc()).\
            paginate(page=page,per_page=15)

    object_list = paginate.items
    return render_template('interface/list.html',interfaceifno=object_list,pagination = paginate,scan =if_name)

