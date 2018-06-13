#/usr/bin/env python3
#coding=utf-8
import uuid, json
from autotest import db
from flask import render_template, request, jsonify, redirect
from autotest.common.execute import Execute
from autotest.common.utils import Methods
from autotest.interface import if_view
from autotest.models import InterfaceInfo,Group



@if_view.route('/del/<if_id>')
def delete(if_id):
    InterfaceInfo.query.filter_by(id = if_id).delete()
    db.session.commit()
    return redirect('/interface/list')

@if_view.route('/edit/<if_id>',methods = ['GET','POST'])
def edit(if_id):
    if request.method == 'GET':
        object_list = InterfaceInfo.query.filter_by(id=if_id).first()
        header = Methods.change(object_list.request_header_data)
        body = Methods.change(object_list.request_body_data)
        group = Group.query.order_by(Group.add_date.desc()).all()
        return render_template('interface/edit.html',
                               interfaceifno=object_list,
                               header=header,
                               body=body,
                               group=group)
    elif request.method == 'POST':
        sb_type = request.form.get('sb_type')
        if_name = request.form.get('if_name',type=str, default=None)
        if_url = request.form.get('if_url',type=str, default=None)
        if_method = request.form.get('if_method',type=str, default=None)
        if_type = request.form.get('if_type',type=str ,default=None)
        group_id = request.form.get('group_id', default=None)
        request_header_data = Methods.tojson(request.form.get('request_header_data'))
        request_body_data = Methods.tojson(request.form.get('request_body_data'))

        print(if_name,group_id,if_url,if_method,if_type,request_header_data,request_body_data)

        if if_url and if_method:
            if sb_type == '0':
                try:
                    import datetime
                    db.session.query(InterfaceInfo).filter(InterfaceInfo.id == if_id) \
                        .update({
                        'if_name': if_name,
                        'if_url': if_url,
                        'if_method': if_method,
                        'if_type': if_type,
                        'request_header_data': Methods.tostr(request_header_data),
                        'request_body_data': Methods.tostr(request_body_data),
                        'group_id' :group_id,
                        'user_id': 'linweili',
                        'add_date': datetime.datetime.now()
                    })

                    db.session.commit()
                    print('接口数据更新成功')
                    return jsonify({'code': '200', 'msg': '接口数据更新成功', 'data': '接口数据更新成功'})
                except:
                    print('接口请求成功,更新数据失败')
                    return jsonify({'code': '201', 'msg': '接口数据更新失败', 'data': '接口数据更新失败'})
            else:
                try:
                    status_code, result_text = Execute.call_interface(if_proxie, if_method, if_url, request_header_data,
                                                                      request_body_data, if_type)
                    print(status_code,result_text)
                    if status_code == 200:
                            print('测试接口成功,不保存数据')
                            return jsonify({'code': status_code, 'msg': '接口请求成功', 'data': result_text})
                    else:
                        print('接口请求失败')
                        return jsonify({'code': status_code, 'msg': '接口请求失败', 'data': result_text})
                except:
                    print('接口请求异常')
                    return jsonify({'code': status_code, 'msg': '接口请求异常', 'data': result_text})
        else:
            print('请求url及请求方式不能为空')
            return jsonify({'code': 201, 'msg': '接口请求失败', 'data': '请求url及请求方式不能为空'})

