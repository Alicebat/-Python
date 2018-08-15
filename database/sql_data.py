#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Alicehuang

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column,DATE,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship


import sys

reload(sys)
sys.setdefaultencoding('utf-8')
# 连接mysql数据库
engine = create_engine("mysql+pymysql://root:123456@192.168.4.50/school")

# 定义orm基类
Base = declarative_base()


# 查询时 要将你要查询的表结构列举出来
class Student(Base):
    __tablename__ = 'student'  # 你想要查询的表名
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(32))
    register_date =Column(DATE,nullable=False)

    # 要查询的字段
    def __repr__(self):
        return "<%s name:%s,register_date:%s >" % (self.name, self.register_date)

class StudyRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer, primary_key=True)
    day = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey("student.id"))

    student= relationship("Student" ,backref="my_study_record")

    def __repr__(self):
        return "<%s status:%s , day:%s>" % (self.status,self.day)

Base.metadata.create_all(engine)  #创建表结构


Session_class = sessionmaker(bind=engine)
Session = Session_class()


s1=Student(name="alex",register_date="2018-08-01")
s2=Student(name="bob",register_date="2016-08-01")
s3=Student(name="lucy",register_date="2017-08-01")
s4=Student(name="jhon",register_date="2000-08-01")

study_obj1=StudyRecord(day=1,status="YES",stu_id=1)
study_obj2=StudyRecord(day=2,status="YES",stu_id=1)
study_obj3=StudyRecord(day=5,status="NO",stu_id=2)
study_obj4=StudyRecord(day=4,status="YES",stu_id=1)

Session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])

Session.commit()

