#!/usr/bin/env python
# coding=utf-8
#字典的修改，只要通过key找到，即可修改
info = {'ID':13,'name':"李晨",'sex':"男",'age':18,'addr':"北京市门头沟"}
newId = input("请输入新的编号")
info['ID'] = int(newId)
print("修改后的ID为%d:"%info['ID'])
print(info.values())
print(info.items())
