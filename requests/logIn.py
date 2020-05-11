import requests

# 登录
url = "http://192.168.3.61:8082//userAction_login.action"
header = {"Accept":"application/json"}
data = {"loginName":"admin","password":"admin"}
r = requests.post(url,data=data,headers=header)

# 获取header
header = r.request.headers

# 保存cookie
session = requests.Session()
cookie_jar = session.post(url,data)
cookie = requests.utils.dict_from_cookiejar(cookie_jar.cookies)


# 播放接口
urle = "http://192.168.3.61:8082/tsCmdStoreAction_setCmdByArea.action"    #测试的接口url

datae = {                                        #接口传送的参数
        "tsCmdType": 0,
        "areaIds": 92,
        "mediaId":100,
        "playCount": 1,
        "ebmLevelValue":'04',
        "ebmClassValue":'0005',
        "ebmTypeValue":10000,
        "in_channel_id":0,
        "out_channel_id":1,
        "systemTime":0,
        "duration":60
    }

re = requests.post(url = urle,data = datae,cookies = cookie,headers = header)
print(re.text)