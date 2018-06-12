from celery import Celery
import config
#celery -A taskmanager.celery worker -l info -P eventlet win10
# celery -A taskmanager.celery worker --loglevel=info

# svn checkout 'https://svn.tuandai888.com:8443/svn/developers4/活动运营部发布文件/201805/31/单点登录-调整app里跳转授权登录逻辑/td-passport' --username linweili --password linweili
from autotest import app

celery = Celery('my_background_task',brokend = 'redis://:123456a@192.168.1.5:6379/2', broker='redis://:123456a@192.168.1.5:6379/2')
# celery = Celery(app.name,broker = 'redis://:mWRK6joVy5No@node.td-k8s.com:1379/2',backend = 'redis://:mWRK6joVy5No@node.td-k8s.com:1379/2')
celery.config_from_object('config')
