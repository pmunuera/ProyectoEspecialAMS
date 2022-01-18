import pymysql
import funcions as func
conn=pymysql.connect(host="20.126.87.93",user="delegado",password="delegado",db="RPM")
cur=conn.cursor()

adventures={id_adventure:{'Name': adventure_name,
                          'Description':adventure_description,
                          'Characters': adventure_characters}
            }
query='select * from ADVENTURE'

cur.execute(query)

tupla=cur.fetchall()

for i in tupla:
    adventures[i[0]]={}#1:{}
    adventures[i[0]]['Name']=i[1]
    adventures[i[0]]['Description'] = i[2]
    query2=f"select name from CHARACTER where id_character in (select id_character from HAS where id_adventure='{i[0]}')"
    cur.execute(query2)
    tupla2=cur.fetchall()
    for j in tupla2:
        adventures[i[0]]['Characters'] = j[1]

characters={

    }
query='select * from RPM.CHARACTER'

cur.execute(query)

rows=cur.fetchall()

for i in rows:
    characters[i[0]]=i[1]

print(characters)

Answers_ByStep_Adventure={{idAnswers_ByStep_Adventure, idByStep_Adventure}:{
                            'Description':description,
                            'Resolution_Answer':Resolution_Answer},
                            'NextStep_Adventure':NextStep
}
query='select * from ANSWER'

cur.execute(query)

tupla=cur.fetchall()

for i in tupla:
    Answers_ByStep_Adventure[{i[0],i[2]}]={}#1:{}
    Answers_ByStep_Adventure[{i[0],i[2]}]['Description']=i[1]

ByStep_Adventure={id_ByStep_Adventure:{'Description':Description,
                                       'answers_in_step':answers_in_step,
                                       "Final_Step":Final_Step}
                  }
query='select * from STEP'

cur.execute(query)

tupla=cur.fetchall()

for i in tupla:
    ByStep_Adventure[i[0]]={}#1:{}
    ByStep_Adventure[i[0]]['Description']=i[1]
    query2=f"select * from ANSWER where id_step_resolution in '{i[0]}'"
    cur.execute(query2)

    tupla2 = cur.fetchall()
    ByStep_Adventure[i[0]]['answers_in_step']=[]
    for j in tupla2:
        ByStep_Adventure[i[0]]['answers_in_step'].append(j[0])
    ByStep_Adventure[i[0]]['Final_Step'] = i[2]


replayAdventures={idGame:{'idUser':id_user,'Username':username,
                          'IdAdventure':id_adventure,
                          'Name':adventure_name,
                          'date':date,
                          'idCharacter':id_character,
                          'CharacterName':character_name}
                  }