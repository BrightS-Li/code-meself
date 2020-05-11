import configparser

#载入配置文件
config = configparser.ConfigParser()

#IpConfig.ini可以是一个不存在的文件，意味着准备新建配置文件
config.read("config/IpConfig.ini")

'''写入过程'''
'''
#配置文件中添加section
config.add_section("Server")

#在节School中增加新的参数
config.set("Server","ip","192.168.3.1")

#增加完所有需要的项目后，进行写入操作。config/ ---写入某个文件夹
config.write(open("config/IpConfig.ini","w"))
'''

'''读取过程'''
ip = config.get('Server','ip')
user = config.get('Server','user')
password = config.get('Server','password')
database = config.get('Server','database')

print(ip,user,password,database)
