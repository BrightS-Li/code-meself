import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.readExcel import ReadExcel
from lib.sendRequest import SendRequest
from configFile import filedir

test_data = ReadExcel(filedir.TEXT_EXCEL,'Sheet1').get_excel()


test_1_title = SendRequest().get_test_msg(test_data[2])
test_1 = SendRequest().get_request(test_data[2])
print('测试模块: ' + test_1_title['test_module'] + '\n测试编号: ' + str(test_1_title['test_number']) + '\n测试标题: ' + test_1_title['test_title'] + '\n预期结果: ' + test_1_title['test_expected_result'])
print((eval(test_1_title['test_expected_result']))['code'])