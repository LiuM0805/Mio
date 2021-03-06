# 导入Mio_Package包里面的Module模块
from Mio_Package.Module import Module

# 字符
print("Hello World")
# r：原样输出字符
print(r'C:\User\name')
# f和format两种：字符内添加变量
x = 'abc'
print(f'C:\\User\\name\\{x}')
print("C:\\User\\name\\{a}\\{b}".format(b=123, a='abc'))

# 列表
Mio_list = [1, 'abc', 7, 15, "python"]
print(Mio_list[1:3])
# 字符列表
python = "hello"
print(python[0])

# 集合
basket1 = {"apple", "banana", "a"}
basket2 = {"pear", "orange", "a"}
# 合并两个集合
print(basket1.union(basket2))
# 打印相同集合
print(basket1.intersection(basket2))
# 打印不同集合
print(basket1.difference(basket2))

# t=元祖,t1=元祖嵌套
t = 1, 2, 3
t1 = (1, 2, 3, (4, 5, 6))
print(f"t={t},t1={t1}")

# 词典
d = {'a': 1, 'b': 2}
print(d['a'])
# 添加词典
d['c'] = 3
print(d)
# items=拆分键值对给k,v循环遍历词典
for k, v in d.items():
    print(f"{k}:{v}")
# enumerat=拆分索引
for i, v in enumerate(d):
    print(f"索引:{i},值:{v}")

# if判断语句
a = 1
if a == 1:
    print(a)
elif a == 2:
    print(a)
else:
    print("啥也不是")

# for循环语句
l = [21, 28, 35, 40, 52]
for i in l:
    if 30 < i < 45:
        print(f"{i}岁是一个测试高工")
    elif i >= 45:
        print(f"{i}岁是一个测试专家")
    else:
        print(f"{i}岁是一个low")

# while循环
i = 1
while i < 6:
    print(i)
    i += 1


# 函数
def fun(a, b=1, *c, **d):
    print(f"a={a}\nb={b}\nc={c}\nd={d}")


# 调用函数并传参
fun(1, 2, 3, 4, x=1)


# 类
class MyClass:
    # 类变量
    i = 12345

    # 方法
    def f(self):
        print("Hello,World")


# 初始化类，x=类的实例
x = MyClass()
# 调用实例方法
x.f()


# 类方法
class Teacher:
    @classmethod
    def x(cls, *c):
        print(c)


# 无需实例化，直接调用类方法
Teacher.x(1, 2, 3)

# 包与模块
Module().Study()
