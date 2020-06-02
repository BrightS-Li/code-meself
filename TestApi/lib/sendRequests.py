import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from lib.login import Login
from config import setting
import configparser,requests

class SendRequests():
    '''发送请求数据'''
    def loggin(self):
        # 获取session
        session = requests.session()

        cf = configparser.ConfigParser()
        cf.read(setting.TEST_CONFIG,encoding='UTF-8')

        user = cf.get('serverconf','web_user')
        pwd = cf.get('serverconf','web_password')
        ip = cf.get('serverconf','ip')

        url = "http://" + ip + ":8082/userAction_login.action"
        header = {"Accept":"application/json"}
        data = {"loginName":user,"password":pwd}

        r = session.request(url=url,method='post',data=data,headers=header)
        return session


    def sendRequests(self,s,apiData):
        try:
            # 从读取的表格中获取想要的参数作为传递
            method = apiData['method']
            url = 'http://192.168.3.61:8082/' + apiData['url']
            if apiData['params'] == '':
                par = None
            else:
                par = eval(apiData['params'])
            
            if apiData['headers'] == '':
                h = None
            else:
                h = eval(apiData['headers'])
            
            if apiData['body'] == '':
                body_data = None
            else:
                body_data = eval(apiData['body'])
            
            type = apiData['type']
            v = False

            if type == 'data':
                body = body_data
            elif type == 'json':
                body = json.dumps(body_data)
            else:
                body = body_data

            
            # print('url = ' + url)
            # print('headers = ' + str(h))
            # print('data = ' + str(body))
            # print('verify = ' + str(v))
            # print('params = ' + str(par))


            re = s.request(url = url,method = method,headers =h,data=body,params = par)
            return re
        except Exception as e:
            print(e)


# import configparser
# from lib.login import Login
# from config import setting
# from readexcel import ReadExcel
# import requests
# def main():
#     cf = configparser.ConfigParser()
#     cf.read(setting.TEST_CONFIG,encoding='UTF-8')
#     user = cf.get('serverconf','web_user')
#     paw = cf.get('serverconf','web_password')
#     ip = cf.get('serverconf','ip')

#     s = Login().session(ip,user,paw)

#     test_data = ReadExcel(setting.SOURCE_FILE,'Sheet2').read_data()
#     SendRequests().sendRequests(s,test_data)
    
# if __name__ == "__main__":
#     main()