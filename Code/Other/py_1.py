#!/usr/bin/env python
# coding=utf-8
#并行迭代，
    #并行迭代即程序可一同时迭代两个程序 ，列如有两个列表分别保存姓名和年龄，结果需要打印出姓名对应的
    #年龄


print("\n-----使用range()函数进行迭代------")


name = ['晓明','小虎','王尔','立志','苏轼']
ages = [34,43,15,25,64,34]
for i in range(len(name)):
    print ( name[i],"年龄是：\t",ages[i] )
""""上述代码中i是循环索引的标准变量名，使用range()函数对两个列表进行迭代，"""


print("\n-----使用zip()函数进行迭代--------")
n1 = ['北京','上海','杭州','甘肃','济南','河北','成都']
n2 = [10,100,000,3434,564,2345,554,]
for n_1,n_2 in zip(n1,n2):
    print ("城市名称是:\t",n_1,"\t对应的编号是\t",n_2)
"""上述代码使用zip()函数进行并行迭代，zip()函数是把两个序列压缩在一起，然后返回一个元组列表"""




print("\n btesting 试题")
items = ['dcy','admin','mxl','another','heppy','sorry']
i =1  
while i<=1:
    i +=1
    print("------循环 GO ----------")
    for dang in items :
        if dang == 'sorry':
            break
        if dang =='admin':
            continue
        print("第",i-1,"次显示的名称是:\t",dang)




