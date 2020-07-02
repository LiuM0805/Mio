# r 原样输出字符
print("C:\\User\name")
print(r'C:\User\name')

# f和format两种：字符内添加变量
x = 'abc'
print(f'C:\\User\\name\\{x}')
print("C:\\User\\name\\{a}\\{b}".format(b=123, a='abc'))

# 列表及切片打印
Mio_list = [1, 'abc', 7, 15, "python"]
print(Mio_list[1:3])

# 字符列表
python = "hello"
print(python[0])
