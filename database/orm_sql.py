#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Alicehuang

import sqlalchemy
from  sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,foreign

engine=create_engine("mysql+pymysql://root:123456@192.168.4.50/school",encoding='utf-8')   #echo=True 打印创建过程

#定义orm基类
Base = declarative_base()

class Customer(Base):
    __tablename__='customer'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    billing_address_id =Column(Integer,ForeignKey("address.id"))
    shipping_address_id =Column(Integer,ForeignKey("address.id"))


    billing_address=relationship("Address",foreign_keys=[billing_address_id])
    shipping_address =relationship("Address",foreign_keys=[shipping_address_id])

class Address(Base):
    __tablename__='address'
    id =Column(Integer,primary_key=True)
    street =Column(String(64))
    city= Column(String(64))
    state=Column(String(64))


Base.metadata.create_all(engine)  #创建表结构

Session_class=sessionmaker(bind=engine)
session =Session_class()

# addr1=Address(street="Tiantongyuan",city="changping",state="Bj")
# addr2=Address(street="TT",city="Guangzhou",state="Bj")
# addr3=Address(street="Wudaokou",city="Haidian",state="Bj")
#
# session.add_all([addr1,addr2,addr3])
#
# c1=Customer(name="Alex",billing_address=addr1,shipping_address=addr2)
# c2=Customer(name="bob",billing_address=addr3,shipping_address=addr1)
# c3=Customer(name="lucy",billing_address=addr2,shipping_address=addr2)
# session.add_all([c1,c2,c3])


session.commit()