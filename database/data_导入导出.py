#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Alicehuang

import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
conn=pymysql.connect(host="192.168.4.50",port=3306,user="root",password="123456",db='db3')

cursor=conn.cursor()

#文件导入
sql_load='''load data infile "/filedir/passwd" into table db3.user fields terminated by ":" lines terminated by "\n" '''
cursor.execute(sql_load)

# sql_select='''select * from user'''
# cursor.execute(sql_select)
# results=cursor.fetchall()
# for i in results:
#     print(i)
#
# #数据导出
# sql_outfile='''select * from user into outfile "/filedir/user_data.txt"'''
# cursor.execute(sql_outfile)
# print("end")
#
cursor.close()
conn.commit()
conn.close()