import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
TEST_CONFIG = os.path.join(BASE_DIR,'database','config.ini')
# 测试用例模板文件
SOURCE_FILE = os.path.join(BASE_DIR,'database','DemoAPITestCase.xlsx')