import sql
import configparser

'''读取配置文件'''
config = configparser.ConfigParser()
config.read("sql/sqlConfig.ini")

ip = config.get("server","ip")
user = config.get("server","user")
password = config.get("server","password")
database = config.get("server","database")


sqll = sql.SQLServer(server=ip,user=user,password=password,database=database)
s = sqll.ExecQuery("select * from test")
i = sqll.Other("INSERT INTO [testting].[dbo].[test] ([name], [description]) VALUES ('张三', '嫩');")
d = sqll.Other("delete from test where id = 1 ")
print(s)