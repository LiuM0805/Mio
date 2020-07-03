import unittest


# unittest规定，需要继承Testcase才能识别为测试用例类
class TestDemo(unittest.TestCase):
    # 以test开头为测试用例
    def test_demo(self):
        x = 1 + 2
        print(x)
        self.assertEqual(3, x)


# __name__=当前模块名
# 执行当前模块文件，加下面代码
# 当前文件被导入或引用，下面代码无效
if __name__ == '__main__':
    unittest.main()
