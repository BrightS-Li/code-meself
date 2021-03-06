import pytest
import os
path = os.path.join(os.path.dirname(__file__),(__file__)) # 获取当前文件的绝对路径

'''fixture的实例化顺序'''

order = []

@pytest.fixture(scope="session")
def s1():
    order.append("s1")


@pytest.fixture(scope="module")
def m1():
    order.append("m1")


@pytest.fixture
def f1(f3, a1):
    # 先实例化f3, 再实例化a1, 最后实例化f1
    order.append("f1")
    assert f3 == 123


@pytest.fixture
def f3():
    order.append("f3")
    a = 123
    yield a


@pytest.fixture
def a1():
    order.append("a1")


@pytest.fixture
def f2():
    order.append("f2")


def test_order(f1, m1, f2, s1):
    # m1、s1在f1后，但因为scope范围大，所以会优先实例化
    print(order)
    assert order == ["s1", "m1", "f3", "a1", "f1", "f2"]

if __name__ == "__main__":
    pytest.main(['-q','-s',path,])