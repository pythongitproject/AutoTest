from autotest.task import task_views
from flask import request, render_template
from autotest.task.common import start_task,get_task_status,modify_task_status


@task_views.route('/add', methods = ['GET','POST'])
def add():
    if request.method == 'GET':
        if_id = '5eeab89c-6e27-11e8-8f7c-005056c00008'
        task_id = start_task(if_id)
        print('task_id:' + task_id)
        # return render_template('task/add.html')
        return 'task_id:' + task_id

    elif request.method == 'POST':
        return 'ok'
@task_views.route('/status',methods = ['GET','POST'])
def status():
    if request.method == 'GET':
        task_id = request.args.get('task_id')
        print(task_id)
        task_status = get_task_status(task_id)
        return task_status


