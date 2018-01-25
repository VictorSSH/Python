#!/usr/bin/env python
# coding=utf-8
"定义变量，添加默认值"
cla = [
    '小红', '晓明', '小刚', '小李' ]
print(----"添加之前的默认值------")

for tempName in cla:
    print(tempName)

    "提示并且添加元素"
    temp = input("请输入要添加的字段")
    cla.append(temp)

    print("-----添加之后的字段list----")

    "遍历输出"
    for tempName in cla:
        print(tempName)
