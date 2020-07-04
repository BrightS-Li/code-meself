import pytest
import os
path = os.path.join(os.path.dirname(__file__),(__file__)) # 获取当前文件的绝对路径



def setup_module():
    print("setup_module =====整个.py模块开始前只执行一次:打开浏览器=====")


def teardown_module():
    print("teardown_module =====整个.py模块结束后只执行一次:关闭浏览器=====")


def setup_function():
    print("setup_function ===每个函数级别用例开始前都执行setup_function===")


def teardown_function():
    print("teardown_function ===每个函数级别用例结束后都执行teardown_function====")


def test_one():
    print("test_one one")


def test_two():
    print("test_two two")


class TestCase():
    def setup_class(self):
        print("setup_class ====整个测试类开始前只执行一次setup_class====")

    def teardown_class(self):
        print("teardown_class ====整个测试类结束后只执行一次teardown_class====")

    def setup_method(self):
        print("setup_method ==类里面每个用例执行前都会执行setup_method==")

    def teardown_method(self):
        print("teardown_method ==类里面每个用例结束后都会执行teardown_method==")

    def setup(self):
        print("setup =类里面每个用例执行前都会执行setup=")

    def teardown(self):
        print("teardown =类里面每个用例结束后都会执行teardown=")

    def test_three(self):
        print("test_three three")

    def test_four(self):
        print("test_four four")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "-ra", path])