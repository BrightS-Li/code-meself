from config import Config

class test():
    def testt():
        sql = Config().sql
        srv = sql.ExecQuery('''select * from srv''')
        print(srv)
if __name__ == "__main__":
    test.testt()
