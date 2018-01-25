#!/usr/bin/env python
# coding=utf-8
nameList =['北京','上海','天津','河南','郑州','山东']
for tem in nameList:
    print(tem.splitlines())
    print(tem)
print("上面是用for输出")
    
i=0
while i<len(nameList):
    print(nameList[i])
    i+=1
