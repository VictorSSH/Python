#!/usr/bin/env python
# coding=utf-8
#函数能处理比当初声明时更多的参数，这些参数叫做不定长参数，声明时不会命名
#基本语法如下
        #def functionName([formal_ages,] *ages,**kwargs):
        #"函数_文档字符串"
        #    function_suite
        #    return [expression]
#加了(*)号的变量ages会存放所以未命名的变量参数，args为元组；而加(**)的变量kwargs会存放命名的参数，即形如key=value的参数，kwargs为字典 


def fun(a,b,*args,**kwargs):
    """可变参数演示"""
    print("a = ",a)
    print( "b = ",b)
    print( "args=",args)
    print( "kwargs:")

    for key,value in kwargs.items():
        print (key,"=",value)

fun(1,2,3,4,5, m =6,n=7,p=8)#注意参数传递的参数对应


