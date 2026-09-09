#2026-09-09 Python 核心语法
#1.数据存储与运算-子面量
#字面量类型及书写格式
#数字类型 布尔类型（True False） 字符串类型（必须用引号括起来） 空值 数据容器
# print(3.14) #浮点型
# print(100) #整型
#print("100") #字符串类型
# print("hello world") #字符串类型
# print(True) #bool类型
#
# print(True + False) #bool类型本质也是整型
# print(True - 1)

#2.数据存储与运算-变量
#变量：在程序中来存储单个数据的容器，通常把经常发生变化的数据存储在变量中。
#定义格式：变量名 = 变量值 e.g:num = 114.1
#Python是动态型的语言，程序运行时才进行检查，变量类型可以在运行程序是改变。一个变量可以有有个值,但是项目开发中，尽量在同一个变量中用同一个类型
# num = 1114.1
# print(num)
#
# num = num + 1
# print(num)
#
# num = "OK"
# print(num)
#
# num = True
# print(num)
#案例
# base = 20.7
# incr = 50
# print("未来一个月的播放总量：" , base + incr)
# print("未来二个月的播放总量：" , base + incr + incr)

#一次性定义多个变量
# base , incr = 20.7 , 50
# print("未来一个月的播放总量：" , base + incr)
# print("未来二个月的播放总量：" , base + incr + incr)

#3.数据存储与运算-标识符
#规则：
# 1.只能包含字母、数字、下划线
# 2.不能以数字开头
# 3.不能使用关键字：True 、 False 、 and 、or 、 if 、 else 、 elif 、 for 、 while....
# 4.严格区分大小写

#命名规范：
# 1.见名知意
# 2.多个部分用下划线链接：update_time , my_name...
# 3.英文字母全小写

#4.数据存储与运算-变量交换（案例）
#案例：现有两个变量，分别为：a=10，b=20，现需要将这两个变量值交换，然后输出到控制合。
# a = 10
# b = 20
# print("交换前a = ",a)
# print("交换前b = ",b)
# c = a
# a = b
# b = c
# print("交换后a = ",a)
# print("交换后b = ",b)

#练习：现有三个变量，分别为：a=100，b=200，c=300，现需要将这三个变量值进行交换，将a，b，c的值分别赋值给c，a，b，并将其输出到控制台。
# a = 100
# b = 200
# c = 300
# print(a,b,c)
# m = a
# a = c
# n = b
# b = m
# c = n
# print(a,b,c)

#5.数据存储与运算-数据类型
#int（整型） float（浮点型） str（字符串类型） bool（布尔类型） nonetype（空值类型）
#如果想查到数据类型可以用以下方法：

#通过type()语句来得到数据类型，具体用法：type(要查看类型的数据)
#e.g:
# print(type(10))
# print(type("hello"))
# print(type(True))
# print(type(None))
# num = 3.14
# print(num)
# print(type(num))  #注意：变量本身没有类型，type(变量)输出的类型是变量中存储数据的类型
#直接把type理解成调用python的一种函数

#还有种方法可以来判断数据类型
#通过isinstance()检查数据是否属于指定的类型，返回的是一个bool值，具体语法为：isinstance（数据，类型）。如果是返回True，不是返回False
# num = 5.0
# print(isinstance(num, int))
# print(isinstance(num, float))
# print(isinstance(num, bool))
