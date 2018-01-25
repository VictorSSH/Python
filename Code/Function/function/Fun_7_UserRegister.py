#!/usr/bin/env python
# coding=utf-8
#demo 
#验证用户注册信息，
#编译用户组册账号所使用的函数，

#创建函数并设置其默认值
def registerUser(userName="su",idcard="python",tel="123"):
    #提示用户输入名称
    userName = input("请输入用户名称：\n")
    #判断用户输入名称的长度
    if ( len(userName) >3  and len(userName)<20):
        idcard=input("请输入您的账号:\n")
        #判断用户输入的账号是否为数字
        if (idcard.isdigit()):
            tel=input("请输入您的电话号码:\n")
            #判断用户电话号码的长度及格式
            if(tel.isdigit() and len(tel)>7 and len(tel)<11):
                print("恭喜！注册成功！")
            else:
                print("电话格式及长度不正确！")
        else:
            print("账号格式不正确，请输入数字！")
    else:
        print("用户名称的长度必须在3-20之间！")

registerUser()

#在上述的实例中，虽然在函数registerUser()中分别设置了默认值，
#def registerUser(userName="su",idcard="python",tel="123")
#但当按照提示重新输入实际的参数值时，形式参数的实际值将覆盖原有的默认值，在函数
#registerUser()中，按照实际输入的参数并根据条件做出的判断，运行得到了不同的输出
