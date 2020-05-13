import requests
import json
from SQLServer import SQLServer
import time
import configparser
from logg import Logger

class Config():

    '''读取配置文件'''
    def __init__(self):
        # 读取数据库配置文件
        config = configparser.ConfigParser()
        config.read("C:/Users/Administrator/Desktop/音频流自动化测试/快速播放/conf.ini",encoding='UTF-8')

        self.ip = config.get('server','ip')
        self.user = config.get('server','user')
        self.password = config.get('server','password')
        self.database = config.get('server','database')

        # 读取配置文件播放接口信息
        self.areaIds = config.get('startPlay','areaIds')
        self.mediaId = config.get('startPlay','mediaId')
        self.playCount = config.get('startPlay','playCount')
        self.time = config.get("startPlay","time")
        self.counts = config.get('startPlay','counts')



class Ginkgo():

    def __init__(self):

        c = Config()

        self.ip = c.ip
        self.user = c.user
        self.password = c.password
        self.database = c.database

        # 连接数据库
        self.sql = SQLServer(server=self.ip,user=self.user,password=self.password,database=self.database)

        self.areaIds = c.areaIds
        self.mediaId = c.mediaId
        self.playCount = c.playCount

        # 日志打印
        self.log = Logger('C:/Users/Administrator/Desktop/音频流自动化测试/快速播放/log.txt',level='debug')

    def Kaibo(self):

        # 登录
        url = "http://192.168.3.61:8082/userAction_login.action"
        header = {"Accept":"application/json"}
        data = {"loginName":"admin","password":"admin"}
        r = requests.post(url,data=data,headers=header)

        # 保存cookie
        session = requests.Session()
        cookie_jar = session.post(url,data)
        cookie = requests.utils.dict_from_cookiejar(cookie_jar.cookies)
        # print(cookie)
        # print(cookie_jar.headers)

        # # 播放接口
        url = "http://192.168.3.61:8082/tsCmdStoreAction_setCmdByArea.action"    #测试的接口url
        header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
                }

        data = {                                        #接口传送的参数
            "tsCmdType": 0,
            "areaIds": self.areaIds,
            "mediaId":self.mediaId,
            "playCount": self.playCount,
            "ebmLevelValue":'04',
            "ebmClassValue":'0005',
            "ebmTypeValue":10000,
            "in_channel_id":0,
            "out_channel_id":1,
            "systemTime":0,
            "duration":60
            }

        # # 选择歌曲id
        # music = self.sql.ExecQuery("SELECT id,name FROM [dbo].[media]")
        # for i in music:
        #     print("id：" + str(i[0]) + " --→ " + str(i[1]))
        # print('-------------------')
        # data['mediaId'] = input("请输入歌曲id:")

        # #选择区域
        # org = self.sql.ExecQuery('select parentid,org_detail from Organization')
        # for org_one in org:
        #     print("org_id: " + str(org_one[0]) + "--→" + str(org_one[1]))
        # print('-------------------')
        # data['areaIds'] = input("请输入区域areaIds:")



        r = requests.post(url = url,data = data,cookies = cookie,headers = header)
        #return r.json
        if r.text[11] == "1":
            self.log.logger.info("-----------------------------开播成功-----------------------------")
        time.sleep(20)
        boFang = self.sql.ExecQuery('''SELECT
            pr_id 插播id,
            ORG_DETAIL 区域,
            PR_EVN_TYPE 播放模式,
                pid.PID_VALUE PID,
                pid.PID_UDP_PORT 复用器端口,
                pid.RTP_ADDRESS rtp地址,
                pid.RTP_PORT rtp端口,
                rtsp_url rtsp地址
        FROM
            playRecord p
        LEFT JOIN Organization o ON o.ORG_CODEA = p.PR_AREACODE
        LEFT JOIN PIDINFO pid on pid.Pid_ID = p.PR_PID''')

        self.log.logger.info("rtp_url  :  " + "rtp://" + boFang[0][5] + ":" + boFang[0][6])
        self.log.logger.info("rtsp_url :  " + str(boFang[0][7])[8:] )

    def Tingbo(self):
        '''停播接口'''
        prid = self.sql.ExecQuery("SELECT pr_id FROM playRecord p LEFT join Organization o on o.org_codea = p.PR_AREACODE")
        prlids = prid[0][0]
        tingBo = self.sql.Other("DELETE playRecord where pr_id = %d" % prlids)
        self.log.logger.info('-----------------------------停播成功-----------------------------')

if __name__ == "__main__":
    Ginkgo().Kaibo()