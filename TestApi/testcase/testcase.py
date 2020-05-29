import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,requests,ddt,json
from lib.readexcel import ReadExcel
from lib.login import Login
from config import setting
from db_fixture.mysql_db import DB
import configparser
from lib.sendRequests import SendRequests
from lib.writeexcel import WriteExcel
import warnings

testData = ReadExcel(setting.SOURCE_FILE,'Sheet2').read_data()
print()

@ddt.ddt
class Demo_API(unittest.TestCase):
    '''融合平台'''
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)
    def setDown(self):
        pass

    @ddt.data(*testData)
    def test_api(self,data):
        # 获取id字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[2])
        print(rowNum)
        # print(data)
        # 发送请求
        r = SendRequests().sendRequests(data)
        # 获取服务端返回的值
        self.result = r.json()
        # print(self.result)
        # 获取excel表格数据
        readData_code = int(data['status_code'])
        readData_msg = data['msg']
        if readData_code == self.result['status'] and readData_msg == self.result['message']:
             OK_data = 'PASS'
             WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1,OK_data)
        if readData_code != self.result['status'] or readData_msg !=self.result['message']:
            NOT_data = 'FALL'
            WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1,NOT_data)
        
        self.assertEqual(self.result['status'],readData_code,'返回实际结果->:%s' % self.result['status'])
        self.assertEqual(self.result['message'],readData_code,'返回实际结果->:%s' % self.result['message'])



    
if __name__ == "__main__":
    unittest.main()