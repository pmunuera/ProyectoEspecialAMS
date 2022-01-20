import pymysql
import funcions as func
conn=pymysql.connect(host="20.126.87.93",user="delegado",password="delegado",db="RPM")
cur=conn.cursor()

adventures={
            }
query='select * from ADVENTURE'

cur.execute(query)

tupla=cur.fetchall()

for i in tupla:
    adventures[i[0]]={}#1:{}
    adventures[i[0]]['Name']=i[1]
    adventures[i[0]]['Description'] = i[2]
    query2=f"select name from `CHARACTER` where id_character in (select id_character from ARE_AVAILABLE where id_adventure='{i[0]}')"
    cur.execute(query2)
    tupla2=cur.fetchall()
    for j in tupla2:
        adventures[i[0]]['Characters'] = j[0]
#print(adventures)
#func.getFormatedAdventures(adventures)
characters={

    }
query='select * from RPM.CHARACTER'

cur.execute(query)

rows=cur.fetchall()

for i in rows:
    characters[i[0]]=i[1]

#print(characters)

Answers_ByStep_Adventure={
}
query='select * from ANSWER'

cur.execute(query)

tupla=cur.fetchall()
print(tupla)
for i in tupla:
    Answers_ByStep_Adventure[i[0],i[2]]={}#1:{}
    Answers_ByStep_Adventure[i[0],i[2]]['Description']=i[1]
    query2=f"select description from STEP where id_step={i[2]}"
    cur.execute(query2)
    tupla2 = cur.fetchall()
    for j in tupla2:
        Answers_ByStep_Adventure[i[0], i[2]]['Resolution_Answer']=j[0]
    Answers_ByStep_Adventure[i[0], i[2]]['NextStep_Adventure'] = i[2]

ByStep_Adventure={
                  }
query='select * from STEP'

cur.execute(query)

tupla=cur.fetchall()


for i in tupla:
    ByStep_Adventure[i[0]]={}#1:{}
    ByStep_Adventure[i[0]]['Description']=i[1]
    query2=f"select * from ANSWER where id_step_resolution in {i}"
    cur.execute(query2)
    tupla2 = cur.fetchall()
    ByStep_Adventure[i[0]]['answers_in_step']=()
    c=0
    for j in tupla2:
        ByStep_Adventure[i[0]]['answers_in_step'][0]=j[0]
        c+=1
    ByStep_Adventure[i[0]]['Final_Step'] = i[2]

print(ByStep_Adventure)


'''replayAdventures={idGame:{'idUser':id_user,'Username':username,
                          'IdAdventure':id_adventure,
                          'Name':adventure_name,
                          'date':date,
                          'idCharacter':id_character,
                          'CharacterName':character_name}
                  }
query='select * from GAME'
cur.execute(query)
tupla=cur.fetchall()
for i in tupla:
    replayAdventures[i[0]]={}
    query2=f"select username from USER where id_user='{i[3]}'"
    cur.execute(query2)
    tupla2=cur.fetchall()
    replayAdventures[i[0]]['idUser']=i[3]
    for j in tupla2:
        replayAdventures[i[0]]['Username'] = j[0]
    replayAdventures[i[0]]['IdAdventure'] = i[2]
    query3=f"select adventure_name from ADVENTURE where id_adventure='{i[2]}'"
    cur.execute(query3)
    tupla3=cur.fetchall()
    for g in tupla3:
        replayAdventures[i[0]]['Name'] = g[0]
    replayAdventures[i[0]]['date'] = i[5]
    replayAdventures[i[0]]['idCharacter'] = i[4]
    replayAdventures[i[0]]['CharacterName'] = i[3]'''