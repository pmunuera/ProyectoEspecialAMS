import pymysql
import funcions as func
conn=pymysql.connect(host="20.126.87.93",user="delegado",password="delegado",db="RPM")
cur=conn.cursor()

adventures={id_adventure:{'Name': adventure_name,
                          'Description':adventure_description,
                          'Characters': adventure_characters}
            }
for i in t:
    adventures[i[0]]={}#1:{}
    adventures[i[0]]['Name']=i[1]

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
                            'NextStep_Adventure':NextStep}
BySteps_Adventure={id_ByStep_Adventure:{'Description':Description,
                                       'answers_in_step':answers_in_step,
                                       "Final_Step":Final_Step}
                  }
replayAdventures={idGame:{'idUser':id_user,'Username':username,
                          'IdAdventure':id_adventure,
                          'Name':adventure_name,
                          'date':date,
                          'idCharacter':id_character,
                          'CharacterName':character_name}
                  }