#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x
    
    def test_two(self):
        x = 'check'
        assert hasattr(x,'check')
def f():
    return 3
def test_function():
    a = f()
    assert a % 2 == 0,'判断a为偶数，当前a的值为：%s' % a

# 异常断言
def test_zero_division():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1/0       
    
    # 断言异常类型 type
    assert excinfo.type == ZeroDivisionError
    # 断言异常value值
    assert 'dibision by zero' in str(excinfo.value)

# 断言装饰器
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_f():
    1/0
        