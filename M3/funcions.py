import pymysql
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

characters={

    }
query='select * from RPM.CHARACTER'

cur.execute(query)

rows=cur.fetchall()

for i in rows:
    characters[i[0]]=i[1]


Answers_ByStep_Adventure={
}
query='select * from ANSWER'

cur.execute(query)

tupla=cur.fetchall()

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
    ByStep_Adventure[i[0]]['Description']=i[2]
    query2=f"select * from ANSWER where id_current_step in ({i[0]})"
    cur.execute(query2)
    tupla2 = cur.fetchall()
    ByStep_Adventure[i[0]]['answers_in_step']=()
    for j in tupla2:
        ByStep_Adventure[i[0]]['answers_in_step']+=(j[0],)
    ByStep_Adventure[i[0]]['Final_Step'] = i[1]



replayAdventures={
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
    query3=f"select name from ADVENTURE where id_adventure='{i[2]}'"
    cur.execute(query3)
    tupla3=cur.fetchall()
    for g in tupla3:
        replayAdventures[i[0]]['Name'] = g[0]
    replayAdventures[i[0]]['date'] = i[4]
    replayAdventures[i[0]]['idCharacter'] = i[3]
    query4 = f"select name from RPM.CHARACTER where id_character='{i[3]}'"
    cur.execute(query4)
    tupla4 = cur.fetchall()
    for k in tupla4:
        replayAdventures[i[0]]['CharacterName'] = k[0]

def get_answers_bystep_adventure(adventure):
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
    return Answers_ByStep_Adventure[adventrureAnswer,adventrureAnswerStep]

def get_adventures_with_chars():
    return adventures

def get_bystep_adventure():
    return BySteps_Adventure

def first_step_adventure(id_adventure):
    queryplay = f"select s.id_step from STEP s where s.id_adventure='{id_adventure}' group by s.id_step order by count(s.id_step) desc limit 1"
    cur.execute(queryplay)
    step = cur.fetchall()
    return step[0]

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


def checkUserbdd(user,password):
    global userid
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
    return ""


def getHeader(text):
    print("*"*120)
    if len(text)%2==1:
        print("=" * (60 - (len(text) // 2)) + text + "=" * (60 - (len(text) // 2+1)))
    else:
        print("="*(60-(len(text)//2))+text+"="*(60-(len(text)//2)))
    print("*" * 120)

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


def getTableFromDict(tuple_of_keys,weigth_of_columns,dict_of_data):
    for i in dict_of_data:
        print(i, end="")
        for j in range(0,len(tuple_of_keys)):
            print(" "*((weigth_of_columns[j])-len(dict_of_data[i])),end="")
            print(dict_of_data[i][tuple_of_keys[j]], end="")
        print()


def getOpt(textOpts="",inputOptText="",rangeList=[],exceptions=[]):
    textOpts = "\n1)Login\n2)Create user\n3)Show Adventures\n4)Reports\n5)Exit"
    inputOptText = "\nElige tu opción: "
    lista = [1, 2, 3, 4,5]
    exceptions = ["w", "e", -1]
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
    historyend=[]
    queryhistory = f"select id_step,id_answer from HISTORY where id_game='{id_game}'"
    cur.execute(queryhistory)
    history = cur.fetchall()
    for i in history:
        historyend.append(i)
    return historyend
def replay():
        crrect = False
        replay = []
        getHeader("Replay Adventures")
        getHeadeForTableFromTuples(("ID GAME","USER","ADVENTURE", "CHARACTER","DATE"),(10,20,40,20,30))
        while True:
            crrect = False
            replay = []
            for i in getGames():
                for j in i:
                    print(j, end=" ")
                print()
            option = input("What adventure you want replay?: ")
            for i in getGames():
                if option == str(i[0]):
                    replay = [i[0], i[2]]
                    crrect = True
            if crrect:
                historylist = getHistory(replay[0])
                print(str(replay[1]).center(100, "*"))
                for i in range(len(historylist)):
                    queryreplays = f"select description from STEP where id_step='{historylist[i][0]}'"
                    cur.execute(queryreplays)
                    replays = cur.fetchall()
                    print(formatText((replays[0][0]+"\n\n"),100,"\n"))
                    queryreplays = f"select description from ANSWER where id_current_step='{historylist[i][0]}'"
                    cur.execute(queryreplays)
                    replays = cur.fetchall()
                    for j in range(len(replays)):
                        print(formatText(str(j + 1)+") "+replays[j][0],100,"\n"))
                    print("\nOpción seleccionada: ", end="")
                    queryreplays = f"select description from ANSWER where id_answer='{historylist[i][1]}'"
                    cur.execute(queryreplays)
                    replays = cur.fetchall()
                    print(replays[0][0], "\n")
                    aux = input("enter para continuar")
                queryreplays = f"select s.description from STEP s inner join ANSWER a on a.id_step_resolution=s.id_step where id_answer='{historylist[len(historylist) - 1][1]}'"
                cur.execute(queryreplays)
                replays = cur.fetchall()
                print(replays[0][0])
                break
            else:
                print("NO VALID OPTION")
                aux = input("Enter to continue")



def checkUserbdd(user,password):
    global userid
    queryCorrectUser=f"select username from USER"
    cur.execute(queryCorrectUser)
    Corruser = cur.fetchall()
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
            queryuserid = f"select id_user from USER where username='{user}'"
            cur.execute(queryuserid)
            userid = cur.fetchall()
            return 1
        else:
            return -1

def getAdventures(char):
    queryadventures = f"select a.id_adventure,a.name,a.description from ADVENTURE a inner join ARE_AVAILABLE r on r.id_adventure=a.id_adventure where r.id_character='{char}'"
    cur.execute(queryadventures)
    adv = cur.fetchall()
    return adv
def getCharacter():
    querychar = f"select id_character,name,description from RPM.CHARACTER"
    cur.execute(querychar)
    character_tuple = cur.fetchall()
    return character_tuple
def choosechar(tuplee):
    global charid
    global charselect
    getHeadeForTableFromTuples(("ID","NAME","DESCRIPTION"),(15,20,30))
    for j in tuplee:
        print(str(j[0]),str(j[1]).rjust(20),str(j[2]).rjust(30))
    option=input("Choose your character: ")
    for i in tuplee:
        if str(i[0])==option:
            charselect=i[1]
            charid=i[0]
            return i[0]
    print("NOT VALID OPTION")
    aux=input("Enter to try again")
    return choosechar(tuplee)
def chooseadventure(characterselected):
    global advselect
    getHeadeForTableFromTuples(("ID","NAME","DESCRIPTION"),(15,20,30))
    for j in getAdventures(characterselected):
        getFormatedBodyColumns((str(j[0]), str(j[1]), str(j[2])),(15,20,60))
    option=input("Choose the adventure: ")
    for i in getAdventures(characterselected):
        if str(i[0])==option:
            advselect=i[0]
            print("THE ADVENTURE BEGIN".center(60),"\n",str(i[1]).center(60))
            return characterselected,i[0],initialsteep(i[0])
    print("NOT VALID OPTION")
    aux=input("Enter to try again")
    return chooseadventure(characterselected)
def initialsteep(id_adventure):
    queryplay = f"select s.id_step from STEP s where s.id_adventure='{id_adventure}' group by s.id_step order by count(s.id_step) desc limit 1"
    cur.execute(queryplay)
    step = cur.fetchall()
    return step[0]
def answersingame(idstep):
    queryans = f"select a.description,a.id_answer,a.id_step_resolution from ANSWER a inner join STEP s on s.id_step=a.id_current_step where a.id_current_step='{idstep}'"
    cur.execute(queryans)
    ans = cur.fetchall()
    return ans
def playgame(adventureandchar):
    global history_insert
    global userid
    global charid
    queryplay = f"select description,final_step,id_step,id_adventure from STEP where id_step='{adventureandchar[2][0]}'"
    cur.execute(queryplay)
    statement = cur.fetchall()
    print(statement[0][0])
    if statement[0][1]==1:
        userid=userid[0][0]
        queryinsert = f"insert ignore GAME (id_adventure,id_user,id_character) values ('{adventureandchar[1][0][0]}','{userid}','{charid}')"
        cur.execute(queryinsert)
        conn.commit()
        querymax = f"select max(id_game) from GAME"
        cur.execute(querymax)
        maxy = cur.fetchall()
        maxy = maxy[0][0]
        for i in history_insert:
            queryinsert = f"insert ignore HISTORY (id_game,id_step,id_answer) values ('{maxy}','{i[0]}','{i[1]}')"
            cur.execute(queryinsert)
            conn.commit()
        return "THE END"
        history_insert=[]
    print("\nQue debería hacer ",charselect," ?\n")
    while True:
        answerslist=[]
        for i in answersingame(statement[0][2]):
            answerslist.append(i)
            print(len(answerslist)," ",i[0])
        option=input("Option: ")
        for i in range(1, len(answerslist) + 1):
            if option==str(i):
                history_insert.append([adventureandchar[2][0],answerslist[i-1][1]])
                return playgame([[adventureandchar[0]],[adventureandchar[1]],[answerslist[i-1][2]]])
        print("NOT VALID OPTION!")
        aux = input("Enter to try again")
charid=0
userid=0
charselect=""
advselect=0
history_insert=[]
check=-1

def reportsmenu():
    getHeader("MENU REPORTS")
    print("\n\n1) Most used answer\n2) Player with more played games\n3) Games played by user\n4) Back".center(80))
    option=input("\nChoose: ".center(80))
    if option=="1":
        return mostusedanswer()
    elif option=="2":
        return mostplayerplays()
    elif option == "3":
        return gamesbyplayer()
    elif option == "4":
        return "TURNING BACK"
    else:
        print("INVALID OPTION")
        aux=input("ENTER TO TRY AGAIN")
        return reportsmenu()
def mostusedanswer():
    querymostansw = f"select count(h.id_answer),a.description from HISTORY h inner join ANSWER a on a.id_answer=h.id_answer group by h.id_answer order by count(h.id_answer) desc limit 1"
    cur.execute(querymostansw)
    mostansw = cur.fetchall()
    queryCorrectadv = f"select a.name from ADVENTURE a inner join STEP s on a.id_adventure=s.id_adventure inner join ANSWER r on s.id_step=r.id_current_step where r.description='{mostansw[0][1]}'"
    cur.execute(queryCorrectadv)
    adv = cur.fetchall()
    getHeadeForTableFromTuples(("ANSWER","ADVENTURE","TIMES CHOOSED"),(30,30,30))
    getFormatedBodyColumns((str(mostansw[0][1]),str(adv[0][0]),str(mostansw[0][0])),(30,30,30))
    print()
    aux=input("Enter to go back")
    return reportsmenu()
def mostplayerplays():
    queryuserplays = f"select u.username,count(g.id_user) from GAME g inner join USER u on g.id_user=u.id_user group by g.id_user order by count(g.id_user) desc limit 1"
    cur.execute(queryuserplays)
    bstuser = cur.fetchall()
    getHeadeForTableFromTuples(("NAME", "PLAYS"), (30, 30))
    #print("NAME".rjust(30), "PLAYS".rjust(30))
    print(str(bstuser[0][0]), str(bstuser[0][1]).rjust(30))
    aux=input("Enter to go back")
    return reportsmenu()
def gamesbyplayer():
    user=input("Please insert user to search: ")
    queryuserplays = f"select username,id_user from USER"
    cur.execute(queryuserplays)
    bbdduser = cur.fetchall()
    for i in bbdduser:
        if str(i[0])==user:
            querycount = f"select count(id_user) from GAME where id_user='{i[1]}'"
            cur.execute(querycount)
            cnt = cur.fetchall()
            cnt=cnt[0][0]
            getHeadeForTableFromTuples(("USER", "PLAYS"), (30, 30))
            print(str(user),str(cnt).rjust(30))
            aux=input("Enter to go back")
            return reportsmenu()
    print("USER NOT EXISTS")
    aux=input("Enter to try again")
    return gamesbyplayer()
