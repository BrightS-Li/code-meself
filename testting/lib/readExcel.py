import os,sys,xlrd
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # 本文件加入环境变量中
from configFile import filedir

data = xlrd.open_workbook(filedir.TEXT_EXCEL) # 打开excel文件
table = data.sheet_by_name(sheet_name = 'Sheet1') # 通过名字获取表
nrow = table.nrows # 获取总行数)
list_nrow = []
for n in range(0,nrow):
    a = table.row_values(n)
    list_nrow.append(a)
excel_head = []
header = {
    '测试模块':'test_module',
    '测试编号':'test_number',
    '测试标题':'test_title',
    '接口':'url',
    '数据':'data',
    '方法':'mehtod',
    '预期结果':'expected_result',
    '实际结果':'actual_result',
    '测试结果':'test_result'
}

for d in list_nrow[0]:
    # header中如果没有d，则把d的值传进去
    d = header.get(d,d)
    excel_head.append(d)
# print(excel_head)
list_dict_data = []
for i in list_nrow[1:]:
    dict_data = {}
    for y in range(len(excel_head)):
        dict_data[excel_head[y]] = i[y] 
    list_dict_data.append(dict_data)

print(list_dict_data)
# ceshi git

