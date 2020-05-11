import requests

# 登录
url = "http://192.168.3.61:8082//userAction_login.action"
header = {"Accept":"application/json"}
data = {"loginName":"admin","password":"admin"}
r = requests.post(url,data=data,headers=header)

# cookie及其用法。
# 提取cookies的方法：调用requests对象的cookies属性获得登录的cookies，并赋值给变量cookies，最后带着cookies去请求
cookies = r.cookies["JSESSIONID"] # ["cookies_name"]
print(cookies)

# 获取headers
print(r.request.headers)

# session及其用法
# session是会话过程中，服务器用来记录特定用户会话信息，session和cookies关系密切-----cookies中储存这seesion信息，seesion中又储存了cookies信息
session = requests.Session()  # 用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies
cookie_jar = session.post(url,data) # 在会话下发起登录请求
cookiee = requests.utils.dict_from_cookiejar(cookie_jar.cookies)# cookie格式化
print(cookiee)