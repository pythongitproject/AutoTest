from autotest.task import task_views
from autotest.models import Task
from flask import render_template, request, jsonify



@task_views.route('/list')
def list():
    paginate = Task.query.order_by(Task.add_date.desc()).paginate(page=1, per_page=15)
    return render_template('task/list.html', task=paginate.items, paginate=paginate)