# 导入div函数
from Unit_test.div import div
# pytest标签需导入
import pytest


# 作业：测试div函数
def test_div_int():
    assert div(10, 5) == 2


# Pytest标签，也叫装饰器，执行它：pytest -m "tab"
@pytest.mark.tab
def test_div_float():
    assert div(6.5, 3.2) == 2.03125


def test_div_except():
    assert div(10, 'a') == "error"
