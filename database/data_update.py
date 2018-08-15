#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Alicehuang

import pymysql

conn=pymysql.connect(host='192.168.4.50',port=3306,user='root',password='123456',db='db3')


cursor=conn.cursor()


sql_update='''update'''

