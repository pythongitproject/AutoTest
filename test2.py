#/usr/bin/env python3
#coding=utf-8
#拉取远程代码
# github
# git clone http://linweili0615:linweili123@github.com/pythongitproject/python-project.git
# coding
# git clone http://linweili:linweili123@git.coding.net/linweili/javaproject.git
#拉取分支
# git clone -b test http://linweili:linweili123@git.coding.net/linweili/javaproject.git

#拉取到最新
# Already up-to-date.
# if 已更：
#     pass
# else:
#     mvn
#mvn clean package
# mvn clean install -Dmaven.test.skip=true
def mvn_install(dir_list):
    msg = '打包失败'
    status = False
    text = ''
    os.chdir(dir_list)
    sh = 'mvn clean package'
    process = subprocess.Popen(sh, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        buff = process.stdout.readlines()
        if buff:
            print('buff:%s' % buff)
            print(str(process.stdout.readlines(), encoding="utf-8"))
        result = process.returncode
        if result == 0:
            print("执行maven打包命令成功")
        else:
            print("执行maven打包命令失败")
        if buff == '' and process.poll() is not None:
            print('没有返回值')
            break

    for dir in os.listdir(dir_list):
        if dir.endswith('.jar'):
            print('找到文件')
            text = dir
    if text != '':
        status = True
        msg = '打包成功'

    return msg, status, text




import subprocess, os
name = 'linweili'
pwd = 'linweili123'
addr = 'git.coding.net/linweili/javaproject.git'
branch = 'test'
target_dir = addr.split('/')[-1].split('.')[0]
print(target_dir)
print('target_dir：%s' % target_dir)
sh = ''
if os.path.exists(target_dir):
    print('当前项目路径已存在')
    print(os.getcwd())
    print('切换路径')
    os.chdir(target_dir)
    print(os.getcwd())
    print('更新代码。。。')
    sh = 'git pull'
    process = subprocess.Popen(sh, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    ret = str(process.stdout.readline(), encoding="utf-8")
    if ret.strip() == 'Already up-to-date.':
        print('该项目暂无更新')
    else:
        result = process.returncode
        if result == 0:
            print("git 更新成功")
            mvn_install('list_dir')
        else:
            print("git 更新失败")
else:
    print('开始拉取项目代码')
    if branch:
        sh = 'git clone -b %s http://%s:%s@%s' % (branch,name, pwd, addr)
    else:
        sh = 'git clone http://%s:%s@%s' % (name, pwd, addr)
    process = subprocess.Popen(sh ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        buff = process.stdout.readlines()
        if buff:
            print('buff:%s' % buff)
            print(str(process.stdout.readlines(), encoding="utf-8"))
        result = process.returncode
        if result == 0:
            print("git拉取：成功")
            mvn_install('list_dir')
        else:
            print("git拉取：失败")
        if buff == '' and process.poll() is not None:
            print('没有返回值')
            break

#删除文件
# def del_file(path):
#     for i in os.listdir(path):
#         path_file = os.path.join(path, i) // 取文件绝对路径
#         if os.path.isfile(path_file):
#             os.remove(path_file)
#         else:
#             del_file(path_file)