import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import configparser
import requests
from config import setting

class Login():
    def session(self,ip,web_user,web_password):
        # 登录
        url = "http://" + ip + ":8082/userAction_login.action"
        header = {"Accept":"application/json"}
        data = {"loginName":web_user,"password":web_password}
        r = requests.post(url,data=data,headers=header)

        # 保存cookie
        session = requests.Session()
        cookie_jar = session.post(url,data)
        cookie = requests.utils.dict_from_cookiejar(cookie_jar.cookies)
        return session
        
if __name__ == "__main__":
    cf = configparser.ConfigParser()
    cf.read(setting.TEST_CONFIG,encoding='UTF-8')
    user = cf.get('serverconf','web_user')
    paw = cf.get('serverconf','web_password')
    ip = cf.get('serverconf','ip')
    s = login().session(ip,user,paw)
    print(s)