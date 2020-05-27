import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class SendRequests():
    '''发送请求数据'''
    def sendRequests(self,s,apiData):
        try:
            # 从读取的表格中获取想要的参数作为传递
            method = apiData['method']
            url = 'http://127.0.0.1:8899/' + apiData['url']
            print(url)
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

            # 发送请求
            re = s.request(method = method,url = url,headers =h,params=par,data=body,verify=v)
            # print(re)
            return re
        except Exception as e:
            print(e)



# from config import setting
# from readexcel import ReadExcel
# import requests
# def main():
#     s = requests.session()
#     test_data = ReadExcel(setting.SOURCE_FILE,'Sheet2').read_data()
#     SendRequests().sendRequests(s,test_data)
    
# if __name__ == "__main__":
#     main()