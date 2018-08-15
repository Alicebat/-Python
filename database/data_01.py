#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Alicehuang

import pymysql

conn=pymysql.connect(host='192.168.4.50',port=3306,user='root',password='123456',db='db3',charset='utf8')


cursor = conn.cursor()
sql_select='''select * from user '''
cursor.execute(sql_select)
result=cursor.fetchall()
for row in result:
    print(row)
    #id= row[0]
    # name= row[1]
    # password=row[2]
    # uid=row[3]
    # gid=row[4]
    # comment=row[5]
    # homedir=row[6]
    # sell=row[7]
    # #print("id =%d ,name =%s,password =%s,uid=%d,gid=%d,comment=%s,homedir=%s,sell=%s"%(id,name,password,uid,gid,comment,homedir,sell))
    # print(id,name,password,uid,gid,comment,homedir,sell)
    #


#cursor.execute("create table d1(id int)engine=innodb")
#data=[100,200,300]
# sql_insert='''insert into d1(id) values(100)'''
# print(cursor.executemany(sql_insert))
# print (cursor.fetchone())
#cursor.executemany("insert into d1(id) values("ss")")

# data=[
#     ("kook",299,231,"/sbin/"),
#     ("lucy",25000,110,"/www")
# ]
#
# #sql_data='''insert into ygtab(user) VALUES("bob")'''
# #cursor.execute(sql_data)
# #cursor.executemany("insert into ygtab(user) values("tom")")
# cursor.executemany("insert  into user(name,uid,gid,sell) values(%s,%s,%s,%s)",data)


conn.commit()


cursor.close()
conn.close()