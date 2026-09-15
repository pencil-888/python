# 13.核心语法-数据存储与与运算-数据类型

# (1)常见数据类型
# int         整数      数字类型,存放整数
# float       浮点数     数字类型 存放小数
# str         字符串     用引号引起来的都是字符串
# bool        布尔       布尔类型,描述真假只有0和1
# NoneType    空值       表示空或者无值,仅包含一个值None

# (2)查询数据类型
# a.通过type()语句来得到数据的类型,具体语法为type(要查看的类型)
print(type("hello"))
print(type(10))
print(type(3.14))
print(type(None))
print(type(True))

num = 5.0
print(num)
print(type(num))

# b.通过isinstance()检查数据是否属于指定类型,返回一个bool值,具体语法为:isinstance(数据,类型)
#判断这个数是不是这个类型,不是返回False;是的话返回True.
num = 5.0
print(num)
print(isinstance(num, int))
print(isinstance(num, float))
print(isinstance(num, bool))

