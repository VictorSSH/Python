#!/usr/bin/env python
# coding=utf-8

#用1代表由车票，0 代表没有车票
#管制刀具长度，单位为cm
logintimes = 0
while logintimes < 3:
    chePiao = input("请输入车票编码\n")
    daoLenght = input("请输入道具长度(cm)\n")
    daoLenght = 9
    chePiao = 1

    if chePiao == 1 and daoLenght < 9:
        print("有效车票，可以进站!")
        print("通过安检，终于可以见到她啦，美滋滋～～～～～\n")
        break
    else:
        print("无效车票，请检查车票编码！")
        print("没有通过安检，等待相关工作人员处理～～～\n")
        logintimes+=1
else:
    print("别试了年轻人！没有车票，赶紧区买票把")
    print("亲爱的只能下次再见了~~~~~\n")

