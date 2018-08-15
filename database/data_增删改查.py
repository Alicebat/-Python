#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Alicehuang

import pymysql

#出现了编译错误 临时添加的
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#连接mysql数据库
conn=pymysql.connect(host='192.168.4.50',port=3306,user='root',password='123456',db='db3')
#获取游标对象
cursor=conn.cursor()

#增
data=[
    ("bob","x",2018,2018,"mysql","/root","/bin/bash"),
    ("lek","x",2019,2018,"mysql","/root","/bin/bash"),
    ("boduoye","x",2020,2018,"mysql","/root","/bin/bash")
]
sql_insert="insert into user(name,password,uid,gid,comment,homedir,sell) values(%s,%s,%s,%s,%s,%s,%s)"

cursor.executemany(sql_insert,data)

#删
sql_delete='''delete  from user WHERE name="kook"'''
cursor.execute(sql_delete)


#改
sql_update='''update user  set password="A"  where id=1'''
cursor.execute(sql_update)


#查
sql_select='''select * from user '''
cursor.execute(sql_select)
result=cursor.fetchall()
for i in result:
    print(i)


cursor.close()
conn.commit()
conn.close()

