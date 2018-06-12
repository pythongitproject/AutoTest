CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://:123456a@192.168.1.5:6379/2'
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24   # 任务过期时间
CELERY_ACCEPT_CONTENT = ["json"]            # 指定任务接受的内容类型.
CELERY_IMPORTS = ("autotest.task.common", )