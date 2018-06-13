#/usr/bin/env python3
#coding=utf-8
from celery import Task
from taskmanager import celery
from autotest.common.execute import Execute
from autotest.common.utils import Methods
from autotest.models import InterfaceInfo


class IFTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task done:{0}'.format(retval))
        return super(IFTask,self).on_success(retval, task_id, args, kwargs)
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason:{0}'.format(exc))
        return super(IFTask,self).on_failure(exc,task_id,args,kwargs,einfo)
    def on_retry(self, exc, task_id, args, kwargs, einfo):
        print('task retry, count:{0}'.format(exc))
        return super(IFTask,self).on_retry(exc,task_id,args,kwargs,einfo)


@celery.task(base = IFTask)
def my_background_task():
    from autotest.common.execute import Execute
    Execute = Execute('','')
    info = InterfaceInfo.query.order_by(InterfaceInfo.add_date.desc()).all()[0]
    method = info.if_method
    url = info.if_url
    header = Methods.str_to_dict(info.request_header_data)
    data = Methods.str_to_dict(info.request_body_data)
    content_type = info.if_type
    status, result = Execute.call_interface(method, url, header, data, content_type)
    print('status:' + str(status) + 'result:' + str(result))
    return "ok"

#执行异步任务，返回任务id
def start_task(args):
    task = my_background_task.apply_async()
    return task.task_id

#根据任务id获取任务状态
def get_task_status(task_id):
    r2 = celery.AsyncResult(task_id,app=celery)
    print(r2.status)
    print(r2.state)
    return r2.status

#根据任务id更改任务状态
def modify_task_status(task_id):
    return 'Hello World!'