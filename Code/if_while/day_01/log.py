#!/usr/bin/env python
# coding=utf-8
#使用if 编写程序,实现以下功能：
    #从键盘输入用户名和密码，
    #如果用户名和密码都正确（预先定义一个用户名和密码），那么即显示“欢迎进入的界面",否则提示密码或者用户名错误
import getpass
logintimes = 0
while logintimes < 3:
    name=input("Please input your username:\n")
    pwd=getpass.getpass("Please input your password:\n")
    if name=='sushenghong' and pwd=='123456':
        #正确后允许进入并且退出循环
        print('Welcome,Login My World')
        break
    else:
        #错误时，出错提示计数加1
        print("Error,Login Again:\n")
        logintimes+=1
else:
            #将错误达到三次后，结束循环
            print("Sorry,Account has Been Loced!\n")
              


