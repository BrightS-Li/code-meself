import sql


sqll = sql.SQLServer(server="192.168.3.61",user="sa.tuners",password="tuners2012",database="volador")
q = sqll.ExecQuery("select * from srv")
print(q) 