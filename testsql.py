#/usr/bin/env python3
#coding=utf-8
import pymysql.cursors
#连接数据库
connect = pymysql.connect(host='10.100.11.152',port=3306, user='test', passwd='L1a4yCP9/EE+kY2t', db='tuandai_info',charset='utf8',)
#获取游标

cursor = connect.cursor()
def addSignDetail(day,signid):
    day = int(day) + 1
    sql = """
    drop procedure if exists 存储过程名1;
    create procedure 存储过程名1()
    begin
    DECLARE i int;
    SET i=1;
    WHILE i<{0} do
    insert into UserSignDetail(id,signdate,type,signday,description,isprize,prizeid,usersignid,adddate,prizereceivestatus,prizegroup,isprizeget)
    values(UUId(),date_format(date_ADD(now(),INTERVAL i-{1} day),'%Y-%m-%d'),1,{2},'正常签到',0,null,'{3}',date_ADD(now(),INTERVAL i-{4} day),
    null,0,0);
    SET i=i+1;
    end while;
    END
    """.format(day,day,day,signid,day)
    try:
        cursor.execute(sql)
        connect.commit()
        cursor.execute('call 存储过程名1()')
        connect.commit()
        print('ok了')
    except:
        print('错了错了')
        cursor.rollback()

if __name__ == '__main__':
    day = 1
    signid = '28d63e5b-d40c-11e7-9fdf-0050568f594f'
    addSignDetail(day,signid)