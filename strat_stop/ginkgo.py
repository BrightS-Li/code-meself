import requests
import json
import time
from logg import Logger
from config import Config  # 读取数据库，并连接数据库

class Ginkgo(Config):

    def Kaibo(self):

        # 登录
        url = "http://" + self.ip + ":8082/userAction_login.action"
        header = {"Accept":"application/json"}
        data = {"loginName":self.web_user,"password":self.web_password}
        r = requests.post(url,data=data,headers=header)

        # 保存cookie
        session = requests.Session()
        cookie_jar = session.post(url,data)
        cookie = requests.utils.dict_from_cookiejar(cookie_jar.cookies)
        # print(cookie)
        # print(cookie_jar.headers)

        # # 播放接口
        url = "http://" + self.ip + ":8082/tsCmdStoreAction_setCmdByArea.action"    #测试的接口url
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
        elif r.text[11] == "2":
            self.log.logger.warning("------------目前正在应急广播或上级用户或区域正在直播，直播任务无法下发-----------------")
        else:
            self.log.logger.warning("查看打印信息" + r.text)
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

        prid = self.sql.ExecQuery("SELECT pr_id FROM playRecord p LEFT join Organization o on o.org_codea = p.PR_AREACODE where o.org_id = %d " % int(self.areaIds))
        prlids = prid[0][0]
        self.sql.Other("DELETE playRecord where pr_id = %d" % prlids)
        self.log.logger.info('-----------------------------停播成功-----------------------------')

if __name__ == "__main__":
    Ginkgo().Kaibo()