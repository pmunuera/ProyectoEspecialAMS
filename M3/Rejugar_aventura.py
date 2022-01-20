import pymysql
conn=pymysql.connect(host="20.126.87.93",user="delegado",password="delegado",db="RPM")
cur=conn.cursor()
###############################
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

