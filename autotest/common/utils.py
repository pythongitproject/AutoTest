import datetime
import decimal
import json,re
from flask import make_response
from functools import wraps

from sqlalchemy.ext.declarative import DeclarativeMeta


class Methods():
    # 验证str是否为json格式数据
    def valid_json(self,raw_msg):
        if isinstance(raw_msg, str):
            try:
                json.loads(raw_msg, encoding='utf-8')
            except ValueError:
                return False
            return True
        else:
            print('该数据非字符串')
            return True
    #替换'为''
    def change(self,string):
        if string:
            string = re.sub('\'', '\"', string)
            # string = json.loads(string)
            return string
        else:
            return None
    def str_to_dict(self,string):
        if string:
            return eval(string)
        else:
            return None

    #转换为字符串
    def tostr(self,string):
        if string:
            return str(string)
        else:
            return None

    def tojson(self,string):
        if string:
            return json.loads(string)
        else:
            return None
    def object_to_json(self,obj):
     if object:
         return json.dumps(obj,cls=AlchemyEncoder)
     else:
         return None

    #字符串查询
    def find_str(self,source_str,f_str):
        if source_str.find(f_str)>0:
            return True
        else:
            return False

    #正则表达式截取
    def json_find_str(self,str):
        pass

#跨域访问装饰器
def allow_cross(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun

from sqlalchemy.ext.declarative import DeclarativeMeta
import json,datetime
class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    data = obj.__getattribute__(field)
                    try:
                        json.dumps(data)  # this will fail on non-encodable values, like other classes
                        fields[field] = data
                    except TypeError:  # 添加了对datetime的处理
                        if isinstance(data, datetime.datetime):
                            fields[field] = data.isoformat()
                        elif isinstance(data, datetime.date):
                            fields[field] = data.isoformat()
                        elif isinstance(data, datetime.timedelta):
                            fields[field] = (datetime.datetime.min + data).time().isoformat()
                        else:
                            fields[field] = None
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)

