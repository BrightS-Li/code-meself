import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
TEST_CONFIG = os.path.join(BASE_DIR,'config','config.ini')