# 14.核心语法-数据存储与运算-字符串定义

# (1)定义字符串的三种方式
# 双引号定义
s1 = "hello"    # 不可直接换行

# 单引号定义
s2 = 'python'   # 不可直接换行

# 三引号定义
s3 = """
Hello:
        欢迎来到python!
"""  # 可以直接换行
print(s1)
print(s2)
print(s3)

# 注意:在定义字符串的时候需要注意字符串里面出现的单引号尤其是英文中,需要用到转义字符

# (2)常见的转义字符
# \' 单引号 表示'
# \" 双引号 表示"
# \n 换行符 换一行
# \t 制表符 空四个也就是tab键
msg = ' It\'s very good '   # 用转义字符来解决
print(msg)

msg2 = " It's very good "   # 当有单引号的时候可以用双引号来解决
print(msg2)

msg3 = "Hello是\"你好\"的意思"
print(msg3)

msg4 = 'Hello是"你好"的意思'
print(msg4)

print("\t你好py\nthon")