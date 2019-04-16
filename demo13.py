import pymysql
'''创建表'''
db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spider')
cursor = db.cursor()
sql = 'create table if not exists students(id varchar(25) not null,name varchar(255) not null,age int not null,primary key(id))'
cursor.execute(sql)
db.close()