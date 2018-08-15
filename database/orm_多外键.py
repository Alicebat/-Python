#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Alicehuang



import sqlalchemy
from  sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine=create_engine("mysql+pymysql://root:123456@192.168.4.50/db3?charset=utf8")   #echo=True 打印创建过程

#定义orm基类
Base = declarative_base()


class Book(Base):
    __tablename__='books'
    id=Column(Integer,primary_key=True)
    name=Column(String(10))
