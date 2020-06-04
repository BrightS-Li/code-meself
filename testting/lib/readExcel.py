import os,sys,xlrd
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # 本文件加入环境变量中
from configFile import filedir

data = xlrd.open_workbook(filedir.TEXT_EXCEL)
