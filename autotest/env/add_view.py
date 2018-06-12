#/usr/bin/env python3
#coding=utf-8
from autotest.env import env_view
from flask import request, render_template, jsonify
from autotest.models import Master, Group
from autotest import db
import uuid,datetime

@env_view.route('/add',methods = ['GET','POST'])
def add():
    if request.method == 'GET':
        master = Master.query.order_by(Master.add_date.desc()).all()
        return render_template('env/add.html', master = master)
    if request.method == 'POST':
        ms = request.form.get('ms')
        ms_name = request.form.get('ms_name')
        master = Master()
        master.id = str(uuid.uuid1())
        master.ms = ms
        master.ms_name = ms_name
        master.add_date = datetime.date.today()
        try:
            db.session.add(master)
            db.session.commit()
            print('保存成功')
            return jsonify({'success': True})
        except:
            print('保存失败')
            return jsonify({'success': False})

@env_view.route('/del',methods = ['POST'])
def del_ms():
    if request.method == 'POST':
        ms_id = request.form.get('ms_id')
        try:
            Master.query.filter_by(id=ms_id).delete()
            db.session.commit()
            print('删除成功')
            count = Master.query.count()
            if count > 0:
                return jsonify({'success': True, "sum" : count})
            else:
                return jsonify({'success': True, 'sum': count})
        except:
            print('删除失败')
            return jsonify({'success': False})


@env_view.route('/gp/add',methods = ['GET','POST'])
def gp_add():
    if request.method == 'GET':
        group = Group.query.order_by(Group.add_date.desc()).all()
        return render_template('env/group_add.html', group=group)
    if request.method == 'POST':
        gp_name = request.form.get('gp_name')
        group = Group()
        group.id = str(uuid.uuid1())
        group.group_name = gp_name
        group.add_date = datetime.date.today()
        try:
            db.session.add(group)
            db.session.commit()
            print('保存成功')
            return jsonify({'success': True})
        except:
            print('保存失败')
            return jsonify({'success': False})

@env_view.route('/gp/del',methods = ['POST'])
def gp_del():
    if request.method == 'POST':
        gp_id = request.form.get('gp_id')
        try:
            Group.query.filter_by(id=gp_id).delete()
            db.session.commit()
            print('删除成功')
            count = Group.query.count()
            if count > 0:
                return jsonify({'success': True, "sum" : count})
            else:
                return jsonify({'success': True, 'sum': count})
        except:
            print('删除失败')
            return jsonify({'success': False})