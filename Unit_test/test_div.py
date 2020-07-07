# 导入div函数
from Unit_test.div import div
# pytest标签需导入
import pytest


# 作业：测试div函数
def test_div_int():
    assert div(10, 5) == 2


# 参数化
@pytest.mark.parametrize("num1,num2,expect", {
    (10, 5, 2),
    (8, 2, 4),
    (20, 10, 2)
})
def test_div_param(num1, num2, expect):
    assert div(num1, num2) == expect


# Pytest标签，也叫装饰器，执行它：pytest -m "tab"
@pytest.mark.tab
def test_div_float():
    assert div(6.5, 3.2) == 2.03125


# 装饰器方式：失败用例重跑；重跑3次，每次间隔5秒
@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_div_except():
    assert div(10, 'a') == "error"


# 预期异常的断言用法
def test_expect_except():
    # 括号内输入报错的结果
    with pytest.raises(TypeError):
        assert div(10, 'a')
