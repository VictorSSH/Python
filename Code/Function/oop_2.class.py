#!/usr/bin/env python
# coding=utf-8
#定义一个类
class Animal:

    #方法

    def __init__(self,name):
        self.name = name

    def printName(self):
        print("名字为：%s"%self.name)

#定义一个函数

def myPrint(animal):
    animal.printName()

dog1 = Animal("嬉戏")
myPrint(dog1)


dog2 = Animal("北京闭")
myPrint(dog2)
