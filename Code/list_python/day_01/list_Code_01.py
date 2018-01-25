#!/usr/bin/env python
# coding=utf-8
#<1> 查找列表中的元素,("查" in,not in,index ,count)三个

#1.1 in  

#demo

    #待查找的列表
nameList = ['北京','上海','甘肃','杭州','济南']
    #获取要查找的名字
findName = input("请输入要查找的名字\n")
    #查找是否存在,
if findName in nameList:
        print("找到了！")
else:
            print("没有找到!")

#1.2 not in 

#not in  的方法跟in 的使用方法一样，只不过not in 判断的是不存在

#待查找的列表
nameList_02 = ['a','n','h','w''g']
#获取要查找的名字
findName_02 = input("请输入要查找的名字\n")
#查找是否不存在
if findName_02 not  in nameList_02:
    print("不存在！")
else:
    print("存在!")


