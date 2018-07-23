#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/test')

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer(20), primary_key=True)
    name = Column(String(50))


Base.metadata.create_all(engine) #创建所有表结构


if __name__ == '__main__':

    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    # 创建新User对象:
    new_user = User(id=4, name='Bob')
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()