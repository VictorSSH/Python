#!/usr/bin/env python
# coding=utf-8
for i in range(3):
    name=input("请输入用户名：\n")
    pwd=input("请输入密码:\n")
    if name =='xiaoming' and pwd == '123':
        print("登陆成功，")
        break
    else:
        print("用户名或者密码错误\n")
mZlse:
    print("抱歉！输入次数过多，该账户已被锁定!\n")

