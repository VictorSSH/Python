#!/usr/bin/env python
# coding=utf-8
#在函数外面定义的变量叫全局变量
numb = 100

def numb_1():
   #如果在函数中直接修改全局变量，那么会产生异常
   #如果真的需要修改全局变量，那么在函数里面进行声明
   global numb
   print(numb)
   numb+=2
   print(numb)

numb_1()
   
