#!/usr/bin/env python
# coding=utf-8
#添加元素("增"append,extend,insert)
lis = ['xiaoming','xiaohong','xiaohua']

print("------添加之前的元素---------")
for temName in lis:
    print(temName)


    #提示，并且添加元素

    temp = input("请输入要添加的字段")
    lis.append(temp)

    print("添加之后的列表")
    for temName in lis:
        print(temName)
