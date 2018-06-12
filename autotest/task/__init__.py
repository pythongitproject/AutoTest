from flask import Blueprint


task_views = Blueprint('task', __name__, url_prefix = '/task')
from autotest.task import add_view, index_view