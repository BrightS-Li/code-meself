import requests,json

s = requests.session()


# 登录
url = "http://192.168.3.61:8082/userAction_login.action"
header = {"Accept":"application/json"}
data = {"loginName":'admin',"password":'admin'}
r = s.request(url=url,method='post',data=data,headers=header)
print(r.json())
print(s.cookies)

url1 = "http://192.168.3.61:8082/tsCmdStoreAction_setCmdByArea.action"    #测试的接口url
header1 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }

data1 = {                                        #接口传送的参数
    "tsCmdType": 0,
    "areaIds": 91,
    "multiMediaIds": 100,
    "playCount": 2,
    "ebmLevelValue":'04',
    "ebmClassValue":'0005',
    "ebmTypeValue":10000,
    "in_channel_id":0,
    "out_channel_id":1,
    "systemTime":0,
    "duration":60
    }

rr = s.request(url=url1,method='post',data=data1,headers=header1)
print(rr.json())
print(s.cookies)

# url1 = "http://192.168.3.61:8082/setParameterAction_timeCalibration.action"    #测试的接口url
# header1 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
#         }

# data1 = {                                        #接口传送的参数
#     "realTime":"2020-05-28+13:26:37",
#     "tsCmdTypes":"1",
#     "sendTick":"10"
#     }

# rr = s.request(url=url1,method='get',data=data1,headers=header1)
# print(rr.json())