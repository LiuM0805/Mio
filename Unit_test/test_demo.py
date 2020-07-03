import unittest


# unittest规定，需要继承Testcase才能识别为测试用例类
class TestDemo(unittest.TestCase):
    # 测试装置：带class的是类级别方法需加@classmethod注解
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def tearDown(self):
        print("tearDown")

    # 以test开头为测试用例
    def test_sum(self):
        x = 1 + 2
        self.assertEqual(3, x)
        print("This is Test Case")

    def test_num(self):
        price = 4.91
        sum = 100
        stock_price = (price * sum + price * sum * 1 / 1000 + 11) / 100
        print("您的股票成本是：%.3f元" % stock_price)


# __name__=当前模块名
# 执行当前模块文件，加下面代码
# 当前文件被导入或引用，下面代码无效
if __name__ == '__main__':
    unittest.main()
