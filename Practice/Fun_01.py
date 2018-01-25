#!/usr/bin/env python
# coding=utf-8
#__init__方法


class Car:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def move(self):
        print("这是一个人:\n")

#创建对象，并且调用init方法

NEW = Car("晓航",15)
print("我的名字是:\n",NEW.name)
print("我今年:\n",NEW.age)

a = Car("李新",25)
print("我的名字是:\t",a.name)
print("我今年:\t",a.age)
