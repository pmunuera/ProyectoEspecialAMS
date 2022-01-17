import pymysql
conn=pymysql.connect(host="20.126.87.93",user="delegado",password="delegado",db="RPM")
cur=conn.cursor()

query='select * from RPM.CHARACTER'

cur.execute(query)

rows=cur.fetchall()

print(rows)

row1=cur.fetchone()
print(row1)

queryCorrectUser=f"select username from USER"
cur.execute(queryCorrectUser)
username=cur.fetchall()
print(username)