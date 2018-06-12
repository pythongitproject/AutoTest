#/usr/bin/env python3
#coding=utf-8
json_str = '{"code":"SUCCESS","message":"服务正常调用"}'
#查找字符(substring not found 不存在时报异常)
# nPos = json_str.home(string)
# print(nPos)

# print(len(json_str and string))

import re, requests, json

if __name__ == '__main__':
    result = requests.get(url='http://wthrcdn.etouch.cn/weather_mini',params={'citykey':'101010100'})
    # print(result.text)
    res_text = result.text
    print(res_text)
    #str转dict
    dt = eval(res_text)
    for k in dt.keys():
        #获取返回key参数
        print(k)
    # start = '"status":'
    # end = ',"desc":"OK"'
    # get_list = []
    # one = {start:end}
    # get_list.append(one)
    # get_result = {}
    # for list in get_list:
    #     for k, v in list.items():
    #         print(k,v)
    #         res = re.findall(r'%s(.+?)%s' % (start, end), res_text)
    #         print(res[0])
    #         正则提取参数
    #         get_result['$keys'] = res[0]
    # print(str(get_result))
