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
