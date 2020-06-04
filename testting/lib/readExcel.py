import os,sys,xlrd
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # 本文件加入环境变量中
from configFile import filedir

data = xlrd.open_workbook(filedir.TEXT_EXCEL) # 打开excel文件
table = data.sheet_by_name(sheet_name = 'Sheet1') # 通过名字获取表
nrow = table.nrows # 获取总行数
print(table.row_value(0))