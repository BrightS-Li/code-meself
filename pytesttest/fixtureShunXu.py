import pytest
import os
path = os.path.join(os.path.dirname(__file__),(__file__)) # 获取当前文件的绝对路径

'''setup顺序执行'''
@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    print('\n-----------------')
    print('我是module fixture')
    print('-----------------')

@pytest.fixture(scope='class')
def class_fixture():
    print('\n-----------------')
    print('我是class fixture')
    print('-------------------')

@pytest.fixture(scope='function', autouse=True)
def func_fixture():
    print('\n-----------------')
    print('我是function fixture')
    print('-------------------')

def test_1():
    print('\n 我是test1')

@pytest.mark.usefixtures('class_fixture')
class TestFixture1(object):
    def test_2(self):
        print('\n我是class1里面的test2')

    def test_3(self):
        print('\n我是class1里面的test3')

@pytest.mark.usefixtures('class_fixture')
class TestFixture2(object):
    def test_4(self):
        print('\n我是class2里面的test4')

    def test_5(self):
        print('\n我是class2里面的test5')

if __name__ == "__main__":
    pytest.main(['-q','-s',path])