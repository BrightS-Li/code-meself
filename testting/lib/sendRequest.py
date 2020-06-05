import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import requests,json
from readExcel import ReadExcel
from configFile import filedir
import ddt



class SendRequest():
    
    # def get_login():
    #     def loggin(self):
    #     # 获取session
    #     session = requests.session()

    #     cf = configparser.ConfigParser()
    #     cf.read(setting.TEST_CONFIG,encoding='UTF-8')

    #     user = cf.get('serverconf','web_user')
    #     pwd = cf.get('serverconf','web_password')
    #     ip = cf.get('serverconf','ip')

    #     url = "http://" + ip + ":8082/userAction_login.action"
    #     header = {"Accept":"application/json"}
    #     data = {"loginName":user,"password":pwd}

    #     r = session.request(url=url,method='post',data=data,headers=header)
    #     return session

    def get_test_msg(self,data):
        '''获取测试用例相关信息'''
        test_module = data['module']    # 测试模块
        test_number = data['number']    # 测试编号
        test_title = data['title']      # 测试标题
        test_expected_result = data['expected_result']  # 预期结果
        test_actual_result = data['actual_result']      # 实际结果
        test_result = data['test_result']               # 测试结果

        return test_module,test_number,test_result,test_title,test_expected_result,test_actual_result

    def get_request(self,data):
        '''进行接口请求'''
        test_url = data['url']
        test_data = eval(data['data'])
        test_method = data['method']
        re = requests.request(url = test_url,data = test_data,method=test_method)
        print(re.json())
        return re.json()

if __name__ == "__main__":
    data = ReadExcel(filedir.TEXT_EXCEL,'Sheet1').get_excel()
    SendRequest().get_request(data[2])
        


