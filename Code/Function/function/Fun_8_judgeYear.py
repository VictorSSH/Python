#!/usr/bin/env python
# coding=utf-8

#创建函数judegYear()，在该函数中声明一个名称为message的变量，用于返回函数的值，

#定义用于判断瑞年于平年的函数
def judegYear():
    #声明变量用于返回值
    year= int(input("请输入年份：\n"))
    #判断时闰年于平年的条件
    if((year%4 ==0)and(year%100!=0)or(year%400 ==0)):
        print( "闰年！")
    else:
        print("平年!")


#调用judgeYear(),并传入参数 2011，
judegYear()


#上例中，使用用户输入方式来获取参数，使用条件if((year%4 ==0)and(year%100!=0)or(year%400 ==0)):
#来判断用户输入的年份是否为闰年还是平年,
