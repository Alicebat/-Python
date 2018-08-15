#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Alicehuang

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import  declarative_base
from   sqlalchemy import Integer,String,Column
from sqlalchemy.orm import sessionmaker

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#连接mysql数据库
engine = create_engine("mysql+pymysql://root:123456@192.168.4.50/db3")


#定义orm基类
Base = declarative_base()


#查询时 要将你要查询的表结构列举出来
class User(Base):
    __tablename__= 'user3' #你想要查询的表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

#要查询的字段
    def __repr__(self):
        return "<User(name='%s',password='%s,id=%s')>" % (self.name,self.password,self.id)


Session_class = sessionmaker(bind=engine)
Session = Session_class()

#查找对象

#查找表中所有数据
all_user3=Session.query(User).all()
print (all_user3)

#使用filter_by做条件查询
all_by=Session.query(User).filter_by(name='alex').all()
print(all_by)
#使用filter做条件查询
all_filter=Session.query(User).filter(User.name=='bob').all()
print(all_filter)
#获取结果中的第一条数据
all_user=Session.query(User).filter_by(name='alex').first()
print(all_user3)
#多条件查询















Session.commit()