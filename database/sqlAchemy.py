#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Alicehuang



import sqlalchemy
from  sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine=create_engine("mysql+pymysql://root:123456@192.168.4.50/db3",encoding='utf-8',echo=True)   #echo=True 打印创建过程

#定义orm基类
Base = declarative_base()



class User(Base):
    __tablename__= 'user' #表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
    uid = Column(Integer)
    gid = Column(Integer)
    commint =Column(String(32))
    homedir = Column(String(32))
    shell =Column(String(32))


Base.metadata.create_all(engine)  #创建表结构

#与数据库建立socket连接
Session_class = sessionmaker(bind=engine)   #创建与数据库会话
Session = Session_class()    #生成session实例

# user_obj = User(name="alex",password="123456")   #生成你要创建的对象
#
# print(user_obj.name,user_obj.id)
#
# Session.add(user_obj)    #添加对象


Session.commit()
