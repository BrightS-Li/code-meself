from SQLServer import SQLServer
import configparser
from logg import Logger
import os


class Config():
    '''连接数据库，读取接口数据'''
    def __init__(self):
        config = configparser.ConfigParser()
        fp_dir = os.getcwd() # 获取exe目录
        path_conf = os.path.join(fp_dir,"conf.ini") # 拼接配置文件名
        config.read(path_conf,encoding='UTF-8')
        # config.read('strat_stop\conf.ini',encoding='UTF-8')

        # 登录账号密码
        self.web_user = config.get('server','web_user')
        self.web_password = config.get('server','web_password')

        # 连接数据库
        self.ip = config.get('server','ip')
        user = config.get('server','user')
        password = config.get('server','password')
        database = config.get('server','database')

        self.sql = SQLServer(server=self.ip,user=user,password=password,database=database)

        # 读取配置文件播放接口信息
        self.areaIds = config.get('startPlay','areaIds')
        self.mediaId = config.get('startPlay','mediaId')
        self.playCount = config.get('startPlay','playCount')
        self.time = config.get("startPlay","time")
        self.counts = config.get('startPlay','counts')

        # 日志打印log
        path_log = os.path.join(fp_dir,'log.txt')
        self.log = Logger(path_log,level='debug')

def main():
    sqll = Config().sql
    srv = sqll.ExecQuery('''select * from srv''')
    print(srv)

if __name__ == '__main__':
    main()