# 官网示例
def inc(x):
    return x + 1


# 修改IDE默认使用Pytest执行case，就会有绿箭头了
def test_answer():
    assert inc(3) == 5
