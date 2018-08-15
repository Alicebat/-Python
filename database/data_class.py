#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Alicehuang

import pymysql
#打开数据库
db=pymysql.connect(host='192.168.4.50',port=3306,user='root',password='123456',db='school')

#获取游标对象
cursor = db.cursor()

#执行sql操作
sql_select= "select version()"
cursor.execute(sql_select)

#获取版本信息
data = cursor.fetchone()
print("DB version is : %s" %data)

#如果存在删除
cursor.execute("drop table if exists class")

#创建表
sql_create="create table  class(class_id INT PRIMARY KEY auto_increment,class  CHAR(10),FOREIGN KEY(class_id) REFERENCES student(student_id) ON UPDATE CASCADE ON DELETE CASCADE )engine = innodb charset = utf8"
cursor.execute(sql_create)
#插入数据
sql_insert= '''insert into class(class) values("三年级三班")'''
try:
    cursor.execute(sql_insert)
    db.commit()
except:
    db.rollback()


#查询表数据
sql_select= '''select * from class'''
try:
    cursor.execute(sql_select)
    #获取所有记录列表
    result = cursor.fetchall()
    for row in result:
        id = row[0]
        name = row[1]
        print ("id = %d,name=%s" %(id,name))
except:
    print("Error:unable to fetch data")


# try:
#     cursor.execute(sql_insert)
#     db.commit()
# except:
#     db.rollback()

print("end")
db.commit()
cursor.close()
db.close()
