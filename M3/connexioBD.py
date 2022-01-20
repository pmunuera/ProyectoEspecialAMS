import pymysql
conn=pymysql.connect(host="20.126.87.93",user="delegado",password="delegado",db="RPM")
cur=conn.cursor()

query='select * from STEP'

cur.execute(query)

rows=cur.fetchall()

print(rows)

'''row1=cur.fetchone()
print(row1)

queryCorrectUser=f"select * from USER"
cur.execute(queryCorrectUser)
username=cur.description
tupla=()
tupla1=()
columnas = cur.description
dades=cur.fetchall()
for i in columnas:
    tupla1 += (i[0],)
tupla2=dades
tupla+=(tupla1,tupla2)
print(tupla)'''
