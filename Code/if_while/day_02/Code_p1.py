#!/usr/bin/env python
# coding=utf-8
#python中查找的常用方法为：
    #in [存在],如果存在那么结果为true，否则为false
    #not in [不存在],如果不存在那么结果位true,否则false


#demo


#待查找的列表

nameList=['李连杰','成龙','孙燕姿','张嘉义']

#获取用户要查找的名字
findName = input("请输入要查找的关键字")

#查找是否存在
if findName in nameList:
    print("在字典中有相同的名字")
elif findName not in nameList:
    print("没有找到..、\n 你是否要添加？ \n")
else:
    print ("非正常退出")

