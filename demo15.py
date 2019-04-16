import pymysql

data = {
    'id':'20120001',
    'name':'Bob',
    'age':21
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'insert into {table}({keys}) on duplicate key update'.format(table=table,keys=keys,values=values)
update = ','.join([" {key}=%s".format(key=key) for key in data])
sql += update

print(sql)
print(update)
