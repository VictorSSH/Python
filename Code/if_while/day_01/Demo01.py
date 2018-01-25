#!/usr/bin/env python
# coding=utf-8
#用1代表由车票,0代表没有车票

for i in range(3):
    chePiao = input("请输入车票编码\n")
    if chePiao == '123' :
        print("---------------------------")
        print("你输入的车票编号为：\n",chePiao)
        print("有效车票！可以上车")
        print("老司机开车，不存在翻车！")
        break
        print("---------------------------")
    else:
        print("---------------------------")
        print("无效车票，看清楚在输入！")
        print("---------------------------")
else:
    print("抱歉，输入次数过多，我报警了！")
