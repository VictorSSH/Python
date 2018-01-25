#!/usr/bin/env python
# coding=utf-8

#定义一个类car类
class Car:

    #方法
    #移动
    def move(self,name):
        print(name,"车正在移动.....")
    #停止
    def stoping(self):
        print("车突然没油了，，，悲剧")


    def maxing(self,name,age,add):
        
        print("我的名字：\t",name,"\n年龄\t",age,"\n地址\t",add)
        #print("马欣丢了")


#创建一个对象，并用变量MBC来保存他的引用
MBC = Car()
MBC.move("baoma")
MBC.stoping()
MBC.maxing("maxing",15,"甘肃省")
