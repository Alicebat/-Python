#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Alicehuang


import pymysql

conn = pymysql.connect(host='192.168.4.50', port=3306, user='root', password='123456', db='db3')

cursor = conn.cursor()


# 表查询  打印
sql_select = '''select * from user '''
cursor.execute(sql_select)
result = cursor.fetchall()
for row in result:
    print(row)
    # id = row[0]
    # name = row[1]
    # password = row[2]
    # uid = row[3]
    # gid = row[4]
    # comment = row[5]
    # homedir = row[6]
    # sell = row[7]
    # print(id, name, password, uid, gid, comment, homedir, sell)


conn.commit()

cursor.close()
conn.close()