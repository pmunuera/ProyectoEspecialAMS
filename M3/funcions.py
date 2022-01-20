import pymysql
conn=pymysql.connect(host="20.126.87.93",user="delegado",password="delegado",db="RPM")
cur=conn.cursor()

def get_answers_bystep_adventure():
    queryAdventureSteps = f'select id_step from STEP where id_adventure={adventure}'

    cur.execute(queryAdventureSteps)

    rowsAdventureSteps = cur.fetchall()
    for i in rowsAdventureSteps:
        adventrureAnswer=i[0]

    queryAdventureAnswer = f'select id_answer from ANSWERS where id_adventure={adventure}'

    cur.execute(queryAdventureAnswer)

    rowsAdventureAnswer = cur.fetchall()
    for i in rowsAdventureSteps:
        adventrureAnswerStep=i[0]

    return Answers_ByStep_Adventure[{adventrureAnswer,adventrureAnswerStep}]

def get_adventures_with_chars():
    return adventures

def get_bystep_adventure():
    return BySteps_Adventure

'''MIRAR'''
def get_first_step_adventure():
    query=f"select min(id_step) from STEP where id_adventure='{adventure}'"
    cur.execute(query)
    tupla = cur.fetchall()
    return

def get_characters():
    return characters

def getReplayAdventures():
    return ReplayAdventures

def getChoices(game):
    queryChoices=f"select id_answer,id_step from HISTORY where id_game={game}"
    cur.execute(queryChoices)
    tupla = cur.fetchall()
    return tupla

def getIdGames():
    query="select id_game from GAME"
    cur.execute(query)
    tupla = cur.fetchall()
    return tupla

def insertCurrentGame(idUser,idChar,idAdventure):
    query = f"insert ignore into GAME(id_adventure,id_user,id_character) values ('{idAdventure}','{idUser}','{idChar}')"
    cur.execute(query)
    conn.commit()
    conn.close()

def getUsers():
    query="select * from USER"
    cur.execute(query)

    tupla = cur.fetchall()
    users={}
    for i in tupla:
        users[i[1]]={}
        users[i[1]]['password']=i[2]
        users[i[1]]['idUser']=i[0]
    return users
#print(getUsers())


def getUserIds():
    users=getUsers()
    usersAndIds=[]
    usernames=[]
    userIds=[]
    for i in users:
        usernames.append(i)
        userIds.append(users[i]['idUser'])
    usersAndIds.append(usernames)
    usersAndIds.append(userIds)
    return usersAndIds
#print(getUserIds())

def insertUser(user,password):
    queryUser = f"insert ignore into USER(username,password) values ('{user}','{password}')"
    cur.execute(queryUser)
    conn.commit()
    conn.close()
    print("Usuario creado con exito")

def get_table(query):
    tupla=()
    tupla1=()
    cur.execute(query)
    columnas = cur.description
    dades=cur.fetchall()
    for i in columnas:
        tupla1 += (i[0],)
    tupla2=dades
    tupla+=(tupla1,tupla2)
    return tupla
print(get_table("select * from ADVENTURE"))

def checkUserbdd(user,password):
    queryCorrectUser=f"select username from USER"
    cur.execute(queryCorrectUser)
    Corruser = cur.fetchall()
    print(Corruser)
    Correctuser=[]
    tpassword=[]
    for i in Corruser:
        Correctuser.append(i[0])
    if user not in Correctuser:
        return 0
    elif user in Correctuser:
        queryCorrectPassword = f"select password from USER where username='{user}'"
        cur.execute(queryCorrectPassword)
        Correctpassword = cur.fetchall()
        for i in Correctpassword:
            tpassword.append(i[0])
        if password in tpassword:
            return 1
        else:
            return -1
#checkUserbdd("Pablo","Matterblast")

'''MIRAR POR SI ACASO'''
def setIdGame():
    queryHistory = f"insert ignore into GAME(id_game) values '(max(id_game)+1)'"
    cur.execute(queryHistory)
    conn.commit()
    conn.close()

def insertCurrentChoice(idGame,actual_id_step,id_answer):
    queryHistory = f"insert ignore into HISTORY(id_game,id_answer,id_step) values ('{idGame}','{id_answer}','{actual_id_step}')"
    cur.execute(queryHistory)
    conn.commit()
    conn.close()

def formatText(text,lenLine,split):
    text=text.split(" ")
    totallenght=0
    for i in range(0,len(text)):
        if totallenght+len(text[i])>lenLine:
            print(split+text[i], end=" ")
            totallenght=len(text[i])+1
        else:
            print(text[i], end=" ")
            totallenght+=len(text[i])+1
    print()
#formatText("Hola soy el tipotipejo tipo amo claro",10,"\n")

def getHeader(text):
    print("*"*60)
    if len(text)%2==1:
        print("=" * (30 - (len(text) // 2)) + text + "=" * (30 - (len(text) // 2+1)))
    else:
        print("="*(30-(len(text)//2))+text+"="*(30-(len(text)//2)))
    print("*" * 60)

def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0):
    texts=[]
    totallenght=0
    linea=""
    textLinea=[]
    textosLineas=[]
    for i in range(0,len(tupla_texts)):
        texts.append(tupla_texts[i].split(" "))
    for j in range(0, len(texts)):
        textLinea.append(linea+" "*(tupla_sizes[j-1]+margin-len(linea)))
        linea = ""
        textLinea=[]
        c=0
        for i in texts[j]:
            c+=1
            if len(tupla_texts[j])<tupla_sizes[j]:
                if c==len(texts[j]):
                    linea += i+" " * ((tupla_sizes[j] + margin) - len(linea))
                    textLinea.append(linea)
                    linea = ""
                else:
                    linea += i + " "
            elif len(linea)+len(i)+1+margin > tupla_sizes[j]:
                linea+=" "*(tupla_sizes[j]+margin-len(linea))
                textLinea.append(linea)
                linea = ""
                linea += i + " "
            else:
                linea+=i+" "
        textosLineas.append(textLinea)
    textLinea.append(linea+" "*(tupla_sizes[j]+margin-len(linea)))
    if len(textosLineas[0])>len(textosLineas[1]) and len(textosLineas[0])>len(textosLineas[2]):
        c=0
    elif len(textosLineas[1])>len(textosLineas[0]) and len(textosLineas[1])>len(textosLineas[2]):
        c=1
    else:
        c=2
    for j in range(0,len(textosLineas)):
        if len(textosLineas[j])<=len(textosLineas[c]):
            for i in range(0,len(textosLineas[c])-len(textosLineas[j])):
                textosLineas[j].append(" "*tupla_sizes[j])
    for i in range(0,len(textosLineas[c])):
        print(textosLineas[0][i],end="")
        print(textosLineas[1][i], end="")
        print(textosLineas[2][i])
text = "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo seguir con la aventura que estabas viviendo simplemente"
#getFormatedBodyColumns((text,text,text),(20,30,50),margin=2)

adventures={1:{'Name': "Este muerto esta muy vivo",
                      'Description':"Beowulf, se embarca en la busqueda de la espada llamada la Ira de Los Cielos",
                       'Characters': "Hola"},
            2:{"Name": "La Matanza de Texas",
               "Description": "Mario Vaquerizo, se enfrenta al horror"}
            }
def getFormatedAdventures(adventures):
    print("="*60+"Adventures"+"="*60)
    texto=("Id Adventure", "Adventure", "Description")
    print(texto[0].ljust(15, " "),end="")
    print(texto[1].ljust(30," "),end="")
    print(texto[2].ljust(50, " "))
    print("*"*130)
    for i in adventures:
        getFormatedBodyColumns((str(i), adventures[i]['Name'], adventures[i]['Description']), (15, 30, 50), margin=0)
#getFormatedAdventures(adventures)

def getFormatedAnswers(idAnswer,text,lenLine,leftMargin):
    query = f"select id_answer,description from ANSWER where id_current_step={idAnswer}"

    cur.execute(query)

    rows = cur.fetchall()
    id=[]

    for i in rows:
        for j in i:
            id.append(i[0])
            text.append(i[1].split(" "))
            break
    totallenght = 0
    for i in range(0, len(text)):
        print(" " * leftMargin + str(id[i]) + ")", end="")
        for j in range(len(text[i])):
            if totallenght + len(text[i][j]) > lenLine:
                totallenght = 0
                print("\n" +" "*leftMargin+ text[i][j], end=" ")
                totallenght += len(text[i]) + 3
            else:
                print(text[i][j], end=" ")
                totallenght += len(text[i]) + 1
        totallenght = 2
        print()
query=f"select description from STEP where id_step=1"
cur.execute(query)

row = cur.fetchall()
#formatText(row[0][0],60,"\n")
#getFormatedAnswers(1,[],30,5)

def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title=""):
    total=0
    space=[]
    for i in t_size_columns:
        total+=i
    for i in range(0,len(t_name_columns)):
        space.append(t_size_columns[i]-len(t_name_columns[i]))
    print("=" * total)
    for i in range(0,len(t_name_columns)):
        if i==len(t_name_columns)-1:
            print(t_name_columns[i]+" " * space[i])
        else:
            print(t_name_columns[i],end=(" " * space[i]))
    print("*"*total)
#getHeadeForTableFromTuples(("column1", "column2", "column3"), (20, 40, 30))

def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data):
    for i in dict_of_data:
        print(i, end="")
        for j in range(len(tuple_of_keys)):
            print(" "*((weigth_of_columns[j])-len(dict_of_data[i])),end="")
            print(dict_of_data[i][tuple_of_keys[j]], end="")
        print()

diccionari= {4: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
'date': (2021, 11, 28, 18, 17, 20), 'idCharacter': 1, 'CharacterName': 'Beowulf'}, 5: {'idUser': 2, 'Username': 'Jordi',
'idAdventure': 1, 'Name': 'Este muerto esta muy vivo', 'date': (2021, 11, 26, 13, 28, 36), 'idCharacter': 1,
'CharacterName': 'Beowulf'}}
tuple_of_keys = ("Username","Name","CharacterName","date")
weigth_of_columns = (20, 30, 20, 20)

#getTableFromDict(tuple_of_keys,weigth_of_columns,diccionari)


def getOpt(textOpts="",inputOptText="",rangeList=[],exceptions=[]):
    print(textOpts)
    op=input(inputOptText)
    rangeList=lista
    if op.isdigit()==True:
        op=int(op)
    if op in rangeList or op in exceptions:
        return op
    else:
        print("Opcion no valida")
        return False

textOpts = "\n1)Login\n2)Create user\n3)Show Adventures\n4)Exit"
inputOptText = "\nElige tu opción: "
lista = [1, 2, 3, 4]
exceptions = ["w", "e", -1]
#opc=getOpt(textOpts, inputOptText, lista, exceptions)

def getFormatedTable(queryTable,title=""):
    title=queryTable[0]
    c = 0
    for i in title:
        c+=1
    print("=" * 30*c)
    for i in title:
        print(i.ljust(30),end="")
    print()
    print("*" * 30*c)
    for i in queryTable[1]:
        getFormatedBodyColumns((str(i[0]), str(i[1]), str(i[2])), (30, 30, 30), margin=0)


getFormatedTable(get_table("select id_answer, description, id_step_resolution from ANSWER"))

def checkPassword(password):
    compPassword = False
    cont = 0
    espacio = True
    otro = False
    if len(password) >= 8 and len(password)<=12:
        for i in range(len(password)):
            if password[i].isspace() == True:
                print("La contraseña no puede contener espacios en blanco")
                espacio = False
            if password[i].isalpha() == True:
                letra = True
            if password[i].isnumeric() == True:
                numero = True
            if password[i].islower() == True:
                minuscula = True
            if password[i].isupper() == True:
                mayuscula = True
            if password[i].isalnum() == False:
                otro = True
        if espacio == True and letra == True and numero == True and minuscula == True and mayuscula == True and otro == True:
            print("Contraseña segura")
            return True
        else:
            print("La contraseña escogida no es segura")
            return False
    else:
        print("La contraseña escogida no es segura")
        return False

def checkUser(user):
    if (len(user) < 10 and len(user) >= 6) and user.isalnum() == True:
        return True
    elif len(user) > 10:
        print("El nombre de usuario no debe tener más de 10 caracteres ")
        return False
    elif len(user) < 6:
        print("El nombre de usuario ha de tener más de 6 carácteres ")
        return False
    elif user.isalnum() == False:
        print("El nombre de usuario solo puede contener letras y números")
        return False

def userExists(user):
    queryUserCheck = 'select username from USER'

    cur.execute(queryUserCheck)

    rowsUsers = cur.fetchall()
    Users=[]
    for i in rowsUsers:
        for j in i:
            Users.append(j)
    if user in Users:
        return True
    else:
        return False

def getGames():
    querygameid = f"select g.id_game,u.username,a.name,c.name,date_format(g.date_creation,'%d/%m/%Y') from GAME g inner join ADVENTURE a on a.id_adventure=g.id_adventure inner join RPM.CHARACTER c on c.id_character=g.id_character inner join USER u on u.id_user=g.id_user"
    cur.execute(querygameid)
    games = cur.fetchall()
    return games

def getHistory(id_game):
    historyend = []
    queryhistory = f"select id_step,id_answer from HISTORY where id_game='{id_game}'"
    cur.execute(queryhistory)
    history = cur.fetchall()
    for i in history:
        historyend.append(i)
    return historyend
#print(getChoices(1))





