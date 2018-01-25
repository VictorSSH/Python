#!/usr/bin/env python
# coding=utf-8
#打印提示功能
import pdb

def printMenu():
    #pdb.set_trace()
    print("-"*20)
    print("学生管理系统")
    print("1,添加学生信息")
    print("2，删除学生信息")
    print("3，修改学生信息")
    print("4，查询学生信息")
    print("5,显示所有学生信息")
    print("0，退出学生管理系统")

#获取一个学生的信息
#全局变量
newName=""
newSex=""
newPhone = ""
def getInfo():


    #global newName
    #global newSex
    #global newPhone

    #提示用户获取学生的姓名
    newName = input("请输入新学生的名字:\n")

    #提示并且获取新学生的性别
    newSex = input("请输入新学生的性别:\n")

    #提示获取学生的手机号码
    newPhone = input("请输入新学生的手机号码：\n")
    #通过列表的方式把数据整合成一个整体，然后返回
    #return [newName,newSex,newPhone]
    #通过元组的方式把数据整合成一个整体，然后返回
    #return (newName,newSex,newPhone)
    #通过字典的方式把数据整合成一个整体，然后返回
    return {'name':newName,'sex':newSex,'phone':newPhone}


#添加一个学生的信息
def addStuInfo():
    #pdb.set_trace()
    result = getInfo()

    newInfo = {}

    #newInfo['name']= result[0]
    #newInfo['sex']= result[1]
    #newInfo['phone'] = result[2]
    #pdb.set_trace()
    newInfo['name'] = result['name']
    newInfo['sex'] = result['sex']
    newInfo['phone'] = result['phone']



    stuInfos.append(newInfo)

    
#用来修改一个学生的信息
def modifyStuInfo():
    #提示并且获取需要修改的学生编号
    stuId = int(input("请输入要修改的学生编号:\n"))

    getInfo()

    stuInfos[stuId-1]['name'] = newName
    stuInfos[stuId-1]['sex'] = newSex
    stuInfos[stuId-1]['phone'] = newPhone



#用来保存学生的所以信息
stuInfos =[]

while True:
    #1，打印功能提示
    printMenu()

    #2,获取功能的选择
    kay = input("请输入功能对应的数字:\n")

    #3,根据用户的输入，进行相关的操作
    if kay =='1':
        #添加学生的信息
        addStuInfo()
    elif kay =='3':
        #修改学生的信息
        modifyStuInfo()
    elif kay =='5':
        print("-"*15)
        print("学生的信息如下:\n")
        print("-"*15)

        print("序号         姓名       性别         手机号码")
        i = 1
        for tempInfo in stuInfos:
            print("%d       %s      %s      %s"%(i,tempInfo['name'],tempInfo['sex'],tempInfo['phone']))
            i+=1


