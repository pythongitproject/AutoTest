# -*- coding: gbk -*-
import subprocess
mycmd = ['dir']
p = subprocess.Popen(mycmd, shell=True,stdout=subprocess.PIPE,cwd='D:/test/javaproject/Weather')
print(str(p.stdout.readline(),encoding='gbk'))
# for i in p.stdout.readlines():
# #     print(str(i,encoding='gbk'))