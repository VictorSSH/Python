#!/usr/bin/env python
# coding=utf-8
import random

#1.定义一个嵌套列表，
rooms =[[],[],[],[]]
#2.有一个列表，保存了8位老师的姓名
teacher =[
    "李克强","温家宝","张家辉",
    "薛之谦","李晨","陈赫","嘉玲",
    "毛不易","宋东野"]

#3.随机把8位老师的名字添加到第一个列表中，

for name in teacher:
    randomNum =random.randint(0,3)
    rooms[randomNum].append(name)


    #print(rooms)
i=1
for room in rooms:
    #print(rooms)
    print("办公室%d里面的老师姓名是："%i)
    for name in room:
        print(name,end=" ")
    print(" ")
    i+=1
