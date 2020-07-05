# 官网示例
def inc(x):
    return x + 1


# 修改IDE默认使用Pytest执行case，就会有绿箭头了
def test_answer():
    assert inc(3) == 5


# Pytest的测试装置 - module最先执行
def setup_module():
    print("setup module")

# Pytest的测试装置 - function第二执行
def setup_function():
    print("setup function")


# Pytest的类无需继承unittest
class TestClass:
    # Pytest的测试装置 - setup最后执行
    def setup(self):
        print("setup")

    # 给类定义方法加@classmethod，第三执行
    @classmethod
    def setup_class(cls):
        print("setup class")

    name = 'xiaomi'

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
