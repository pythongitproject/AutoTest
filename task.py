from autotest.task import task_views
from autotest.common import Execute
from flask import jsonify
# from autotest import celery
from autotest import scheduler


import datetime
@task_views.route('/index')
def task_index():

    import uuid
    id = str(uuid.uuid1())
    #max_instances = 5    限制同一个job实例的并发执行数
    #misfire_grace_time=2  失败重试次数
    #coalesce=True 合并所有错过时间的job到一个job来执行
    result = scheduler.add_job(func=test_scheduler, id= id,args=[1],
                               trigger='interval',seconds=1,max_instances=1);
    get_jobs_list()
    return 'ok le'

def test_scheduler(num):
    print(num)
    print(datetime.datetime.now())
    return 'ok'

#暂停job
def pause_job(id):
    print('暂停job')
    scheduler.pause_job(id)

#恢复job
def resume_job(id):
    print('恢复job')
    scheduler.resume_job(id)

#删除job
@task_views.route('/delete_job/<id>')
def remove_scheduler(id):
    print('暂停job_id:%s' % id)
    pause_job(id)
    get_jobs_list()
    print('恢复job_id:%s' % id)
    resume_job(id)
    import time
    time.sleep(3)
    get_jobs_list()
    print('移除job_id:%s' % id)
    scheduler.remove_job(id)
    time.sleep(3)
    get_jobs_list()
    return 'ok'

#获取job_list
def get_jobs_list():
    print('获取job_list')
    scheduler.get_jobs()

#修改job
def modify_job(id):
    print('获取job')
    tg_job = scheduler.get_job(id)
    print('job信息:%s' % tg_job)
    scheduler.modify_job(id,trigger='')
