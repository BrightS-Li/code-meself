import os,sys
sys.path.append(os.path.dirname(__file__))
from config import setting
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from lib.newReport import new_report
from db_fixture import test_data
from package.HTMLTestRunner import HTMLTestRunner


def add_case(test_path=setting.TEST_CASE):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(test_path)
    return discover