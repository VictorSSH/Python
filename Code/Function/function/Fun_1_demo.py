#!/usr/bin/env python
# coding=utf-8
#定义一个函数，完成三个数的求和
import pdb
def num():
    pdb.set_trace()
    nu1 = int(input("请输入第一个数：\n"))
    #n1 =10
    if nu1 > 10:
        print("您输入的数不正确!")
        

    nu2 = int(input("请输入第二个数：\n"))
    nu3 =int(input("请输入第三个数：\n"))
    resutlt = nu1+nu1+nu3
    print("三个数的和为：\n",resutlt)
num()


#求两个数的平均数

def max():
    MaxPrint = int(input("请输入第一个数：\n"))
    if MaxPrint <10:
        print("您输入的数不正确！")
    else:
        print("请重新输入!:\n")
        MaxPrint_2 = input("请输入：\n")

    MaxPrint_i = int(input("请输入第二个数：\n"))
    if MaxPrint_i <10:
        print("您输入的数不正确!\n")

    Max_ = (MaxPrint_2+MaxPrint_i)/2
    print("这两个数的平均值为：\n",Max_)
    


max()
