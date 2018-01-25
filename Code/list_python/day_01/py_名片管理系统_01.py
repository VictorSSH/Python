#!/usr/bin/env python
# coding=utf-8

#用来保存学生的所以信息
stuInfos = []

while True:

    #1,打印功能提示
    print("-"*30)
    print("学生管理系统")
    print("1，添加学生信息")
    print("2，删除学生信息")
    print("3，修改学生信息")
    print("4，查循学生信息")
    print("5，显示所以学生信息")
    print("0，退出系统")
    print("-"*30)

    #2,获取功能选择
    kay = input("请输入要操作的编号:\n")

    #3根据用户的选择，进行相关的操作



    if kay=="1":
        #添加学生信息

        #提示获取学生的姓名
        newName=input("请输入新学生的名字:\n")

        #提示获取学生的性别
        newSex=input("请输入新学生的性别(男/女)\n")

        #提示获取学生的手机号码
        newPhone = input("请输入新学生的手机号吗: \n")
        
        newInfo ={}
        newInfo["name" ]= newName
        newInfo["sex"] = newSex
        newInfo["Phone"] = newPhone

        stuInfos.append(newInfo)
    elif kay == '3':
        pass
        #修改学生的信息

        #提示并且获取需要修改的学生姓名
        stuID = input("请输入要修改学生的编号:\n")

        #重新输入学生的信息(姓名。性别，手机ihao号码)
        #提示获取学生的姓名
        newName=input("请输入新学生的名字:\n")

        #提示获取学生的性别
        newSex=input("请输入新学生的性别(男/女)\n")

        #提示获取学生的手机号码
        newPhone = input("请输入新学生的手机号吗: \n")
        stuInfos[stuID-1]['name']= newName
        stuInfos[stuID-1]['name']= newName
        stuInfos[stuID-1]['name']= newName

    elif kay == '5':
       # print(stuInfos)
        print("="*30)
        print("学生的信息如下:\n")
        print("="*30)

        print("序号     姓名      性别        手机号码")
        i = 1
        for tempInfo in stuInfos:
            print("%d       %s        %s        %s"%(i,tempInfo['name'],tempInfo['sex'],tempInfo['Phone']))
            i+=1
