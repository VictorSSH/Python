#!/usr/bin/env python
# coding=utf-8
#缺省参数，
#在调用函数时，缺省参数的值如果没有传入，则被认为是默认值，下列会打印默认的age，如果aeg没有被传入:
import pdb
#可写函数说明
def printinfo(name,age = 89):
    pdb.set_trace()
    "打印任何传入的字符串"
    print ("Name：",name)
    print ("Age：",age)

#调用printinfo函数
printinfo( age=90,name="su" )
printinfo( name="张")
