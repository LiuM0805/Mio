# 官网示例
def inc(x):
    return x + 1


# 修改IDE默认使用Pytest执行case，就会有绿箭头了
def test_answer():
    assert inc(3) == 5


# Pytest的类无需继承unittest
class TestClass:
    name = 'xiaomi'

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
