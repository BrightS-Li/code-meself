import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,requests,ddt,json
from lib.readexcel import ReadExcel
# from lib.login import Login
from config import setting
from db_fixture.mysql_db import DB
import configparser
from lib.sendRequests import SendRequests
from lib.writeexcel import WriteExcel
import warnings

testData = ReadExcel(setting.SOURCE_FILE,'Sheet2').read_data()


@ddt.ddt
class Demo_API(unittest.TestCase):


    '''融合平台'''
    @classmethod
    def setUpClass(self):
        self.s = SendRequests().loggin()
        warnings.simplefilter('ignore',ResourceWarning)
    def setDown(self):
        pass

    @ddt.data(*testData)
    def test_api(self,data):
        '''开播测试'''
        # 获取id字段数值，截取结尾数字并去掉开头
        rowNum = int(data['ID'].split("_")[1])
        # print(data)
        # 发送请求
        r = SendRequests().sendRequests(self.s,data)
        # 获取服务端返回的值
        self.result = r.json()
        print(self.result)
        # 获取excel表格数据
        readData_code = data['status_code']
        readData_msg = data['msg']
        if readData_code == self.result['status']:
            OK_data = 'PASS'
            WriteExcel(setting.SOURCE_FILE).write_data(rowNum + 1,OK_data)
        if readData_code != self.result['status']:
            NOT_data = 'FAIL'
            WriteExcel(setting.SOURCE_FILE).write_data(rowNum + 1,NOT_data)
        
        self.assertEqual(self.result['status'],readData_code,'返回实际结果->:%s' % self.result['status'])
        # self.assertEqual(self.result['message'],readData_code,'返回实际结果->:%s' % self.result['message'])
    
if __name__ == "__main__":
    unittest.main()