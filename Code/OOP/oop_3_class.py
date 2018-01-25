#!/usr/bin/env python
# coding=utf-8
#示例属性如下：
    #cookedLevel: 这是数字：
    #0-3表示还是生的，超过3表示半生不熟，超过5表示已经考好了，超过8表示已经烤过头了
    #cookedString:这是字符串：描述地瓜的生熟程度
    #condiments：这是地瓜的配料列表，比如番茄酱，芥末酱等
#示例方法如下：
#cook():把地瓜烤一段时间
#addCondiments():给地瓜添加配料
#__init__():设置默认的属性
#__str__():让pint的结果看起来好一些


#定义类，并且定义__init__()方法

#定义“地瓜”类

class SweerPotato:
    '这是地瓜类'


    #定义初始化方法

    def __init__(self):
        self.cookedLevel = 0
        self.cookedString= "生的"
        self.codiments= []


#添加“烤地瓜”方法
    '烤地瓜方法'
    def cook(self,time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
             self.cookedString = "烤成灰了"
        elif self.cookedLevel >5:
            self.cookedString = "烤好了"
        elif self.cookedLevel > 3:
            self.cookedString = "半生不熟"
        else:
            self.cookedStrinh = "生的"



#测试

mySweetPotato = SweerPotato()
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
print(mySweetPotato.codiments)

#测试cook方法
print("开始烤............\n")
mySweetPotato.cook(4) #烤了4分钟了
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
