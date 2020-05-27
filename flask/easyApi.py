import flask,json
from flask import request

'''
flask : web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url，username，passwd
'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)

# server.config['JSON_AS_ASCII'] = Flask
# @ server.route()可以将普通函数转换变为服务，登录接口的路径，请求方式

@server.route('/login',methods=['get','post'])
def login():
    # 获取通过url请求传参的数据
    name = request.values.get('name')
    # 获取url请求传的密码，明文
    pwd = request.values.get('pwd')
    # 打印解析完的参数
    print(name)
    print(pwd)
    # 判断用户名，密码都不为空，如果不传用户名，密码则name和pwd为None
    if name and pwd:
        if name == 'admin' and pwd == 'admin':
            # 登录成功后可以将信息鞋子啊cookie里
            resu = {'code':200,'message':'sucess'}
            # 将字典转换为json串，json是字符
            return json.dumps(resu,ensure_ascii=False)

        else:
            resu = {'code':-1,'message':'failure'}
    else:
        resu = {'code':10001,'message':'param is none'}
        return json.dumps(resu,ensure_ascii=False)

# 启动服务，默认端口号是5000
# debug = True，修改代码后，不需要启动服务，它会帮你自动重启
if __name__ == "__main__":
    server.run(debug=True,port=8899,host='0.0.0.0')
# 指定端口，host，0.0.0.0别人可以通过ip访问，任何ip都可以访问
       
