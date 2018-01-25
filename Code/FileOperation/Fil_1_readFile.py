#!/usr/bin/env python
# coding=utf-8
#问题：
    #想从一个文件中读取文本数据，
    #最方便的方法时一次性读取文件中的所有内容放置到一个大字符串中：
#提示并且要复制的文件名称

name = input("请输入要复制的文件名称\n")
#打开要复制的文件

f_read = open(name,"r")
#创建一个新的文件，用来存储源文件的内容
f_write = open("test[附件].txt","w")

#复制
#第一种
content = f_read.read()
f_write.write(content)
#第二种
for lineContent in f_read.readline():
    if len(lineContent)>0:
        f_write.write(lineContent)
    else:
        break

#关闭文件
f_read.close()
f_write.close()

