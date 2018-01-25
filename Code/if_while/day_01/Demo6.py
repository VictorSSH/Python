#!/usr/bin/env python
# coding=utf-8
#定义一个列表，里面有一些名字
NameList = ['北京','上海','广州','成都','济南','兰州']
# 从键盘获取要查找的关键字
insertName = input("请输入年要查找的关键字: \n")
# 判断 输入的关键字是否存在，并且给出相关提示

a =0
for name in NameList:
    if name==insertName:
         a =1
    #如果在前面已经检索出来里，那么即结束检索，
    #提升程序运行效率
         break

if a ==1:
        print("欢迎你\n")
else:
        print("没有相关信息")



#第二种方法
if insertName in  NameList:
    print(“找到了")
else:
    print("没有找到")




