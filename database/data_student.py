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
cursor.execute("drop table if exists student")

#创建表
sql_create="create table student(student_id int PRIMARY KEY auto_increment,student_name  CHAR(10),gender  enum('boy','girl') DEFAULT 'boy', id CHAR(10))DEFAULT CHARSET=utf8 , engine=innodb"
#cursor.execute("create table ygtab(yg_id int PRIMARY KEY auto_increment,user CHAR(15))engine=innodb "
cursor.execute(sql_create)
#插入数据
sql_insert= '''insert into student(student_name,gender,id) values('lucy','girl','三年级二班')'''
try:
    cursor.execute(sql_insert)
    db.commit()
except:
    db.rollback()


#查询表数据
sql_select= '''select * from student'''
try:
    cursor.execute(sql_select)
    #获取所有记录列表
    result = cursor.fetchone()
    for row in result:
        id = row[0]
        name = row[1]
        gender= row[2]
        class_id=row[3]
        print ("id = %d,name=%s ,gender=%s,class_id=%s" %(id,name,gender,class_id))
except:
    print("Error:unable to fetch data")


try:
    cursor.execute(sql_insert)
    db.commit()
except:
    db.rollback()
    print("Error")

print("end")

db.close()
