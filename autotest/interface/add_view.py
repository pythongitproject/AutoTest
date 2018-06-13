#/usr/bin/env python3
#coding=utf-8
import uuid

from autotest import db
from flask import render_template, request, jsonify
from autotest.common import Methods
from autotest.common.execute import Execute
from autotest.interface import if_view
from autotest.models import InterfaceInfo,Group


@if_view.route('/add',methods = ['GET','POST'])
def add():
    if request.method == 'GET':
        group = Group.query.order_by(Group.add_date.desc()).all()
        return render_template('interface/add.html',group=group)
    elif request.method == 'POST':
        sb_type = request.form.get('sb_type')
        if_name = request.form.get('if_name',type=str, default=None)
        group_id = request.form.get('group_id',type=str, default=None)
        if_url = request.form.get('if_url',type=str, default=None)
        if_method = request.form.get('if_method',type=str, default=None)
        if_type = request.form.get('if_type',type=str ,default=None)
        request_header_data = Methods.tojson(request.form.get('request_header_data'))
        request_body_data = Methods.tojson(request.form.get('request_body_data'))

        print(if_name,group_id,if_url,if_method,if_type,request_header_data,request_body_data)

        if if_url and if_method:
            execute = Execute('','')
            print('start')
            status_code, result_text = execute.call_interface( if_method, if_url, request_header_data,
                                                              request_body_data, if_type)
            print(status_code,result_text)
            if status_code == 200:
                if sb_type == '0':
                    try:
                        if_info = InterfaceInfo(id=str(uuid.uuid1()),if_name=if_name,if_url=if_url,
                                                if_method=if_method,if_type=if_type,
                                                request_header_data=Methods.tostr(request_header_data),
                                                request_body_data=Methods.tostr(request_body_data),
                                                group_id=group_id,user_id='123')
                        db.session.add(if_info)
                        db.session.commit()
                        print('接口请求成功,写入数据成功')
                        return jsonify({'code': status_code, 'msg': '接口请求成功', 'data': result_text})
                    except:
                        print('接口请求成功,写入数据失败')
                        return jsonify({'code': status_code, 'msg': '接口请求成功,写入数据失败', 'data': result_text})
                else:
                    print('测试接口成功,不保存数据')
                    return jsonify({'code': status_code, 'msg': '接口请求成功', 'data': result_text})
            else:
                print('接口请求异常')
                return jsonify({'code': status_code, 'msg': '接口请求异常', 'data': result_text})
        else:
            print('请求url及请求方式不能为空')
            return jsonify({'code': 201, 'msg': '接口请求失败', 'data': '请求url及请求方式不能为空'})

