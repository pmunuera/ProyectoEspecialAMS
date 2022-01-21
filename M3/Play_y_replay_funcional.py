import pymysql
conn=pymysql.connect(host="20.126.87.93",user="delegado",password="delegado",db="RPM")
cur=conn.cursor()
##############REPLAY#################
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
"""
while True:
    crrect=False
    replay=[]
    for i in getGames():
        for j in i:
            print(j,end=" ")
        print()
    option=input("What adventure you want replay?: ")
    for i in getGames():
        if option==str(i[0]):
            replay=[i[0],i[2]]
            crrect=True
    if crrect:
        historylist=getHistory(replay[0])
        print(str(replay[1]).center(100,"*"))
        for i in range(len(historylist)):
            queryreplays = f"select description from STEP where id_step='{historylist[i][0]}'"
            cur.execute(queryreplays)
            replays = cur.fetchall()
            print(replays[0][0],"\n\n")
            queryreplays = f"select description from ANSWER where id_current_step='{historylist[i][0]}'"
            cur.execute(queryreplays)
            replays = cur.fetchall()
            for j in range(len(replays)):
                print(j+1,replays[j][0])
            print("\nOpción seleccionada: ",end="")
            queryreplays = f"select description from ANSWER where id_answer='{historylist[i][1]}'"
            cur.execute(queryreplays)
            replays = cur.fetchall()
            print(replays[0][0],"\n")
            aux=input("enter para continuar")
        queryreplays = f"select s.description from STEP s inner join ANSWER a on a.id_step_resolution=s.id_step where id_answer='{historylist[len(historylist)-1][1]}'"
        cur.execute(queryreplays)
        replays = cur.fetchall()
        print(replays[0][0])
        break
    else:
        print("NO VALID OPTION")
        aux=input("Enter to continue")
"""
#################PLAY#################
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
    print("ID".center(15),"NAME".center(20),"DESCRIPTION".center(30))
    for j in tuplee:
        print(str(j[0]).center(15),str(j[1]).center(20),str(j[2]).center(30))
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
    print("ID".center(15), "NAME".center(20), "DESCRIPTION".center(30))
    for j in getAdventures(characterselected):
        print(str(j[0]).center(15), str(j[1]).center(20), str(j[2]).center(30))
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
    print(statement[0][0])
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
while check<1:
    user = input("Username: ")
    password = input("Introduce la contraseña: ")
    check=checkUserbdd(user,password)
    if check==0:
        print("Este usuario no existe")
    elif check==-1:
        print("Contraseña incorrecta")
    elif check==1:
        print("Usuario y contraseña correctos")
print(playgame(chooseadventure(choosechar(getCharacter()))))