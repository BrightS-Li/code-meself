# coding=utf-8
import pymssql

class SQLServer:
    def __init__(self,server,user,password,database):
    # 类的构造函数，初始化DBC连接信息
        self.server = server
        self.user = user
        self.password = password
        self.database = database

    def __GetConnect(self):
    # 得到数据库连接信息，返回conn.cursor()
        if not self.database:
            print(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(server=self.server,user=self.user,password=self.password,database=self.database)
        cur = self.conn.cursor() # 获取数据库游标对象
        if not cur:
            print(NameError,"连接数据库失败")  # 将DBC信息赋值给cur
        else:
            return cur
             
    def ExecQuery(self,sql):
        '''
        执行查询语句
        返回一个包含tuple的list，list是元素的记录行，tuple记录每行的字段数值
        '''
        cur = self.__GetConnect()
        cur.execute(sql) # 执行查询语句
        result = cur.fetchall() # fetchall()获取查询结果
        # 查询完毕关闭数据库连接
        self.conn.close()
        return result
    
    def Other(self,sqls):
        # 增 删 改
        cur = self.__GetConnect()
        cur.execute(sqls) # 执行查询语句
        # 提交事务
        self.conn.commit()
        self.conn.close()


def main():
    msg = SQLServer(server="192.168.3.61",user="root",password="tuners2012",database="tuenrs_agent")
    result = msg.ExecQuery("SELECT * FROM `sys_role`")
    for (Value) in result:
        print(Value)
 
if __name__ == '__main__':
    main()