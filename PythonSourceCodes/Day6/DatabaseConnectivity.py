import MySQLdb

db = MySQLdb.connect('127.0.0.1','root','SauravMysql1!','test')
cursor = db.cursor()
query = """select * from python"""
lines = cursor.execute(query)
data = cursor.fetchall()
print data
db.close()
