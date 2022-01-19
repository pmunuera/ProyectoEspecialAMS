import pymysql
import funcions as func
conn=pymysql.connect(host="20.126.87.93",user="delegado",password="delegado",db="RPM")
cur=conn.cursor()
textOpts = "\n1)Login\n2)Create user\n3)Show Adventures\n4)Exit"
inputOptText = "\nElige tu opción: "
lista = [1, 2, 3, 4]
exceptions = ["w", "e", -1]
opc=False
while opc==False:
    opc=func.getOpt(textOpts, inputOptText, lista, exceptions)
    if opc==1:
        check=-1
        while check<1:
            user = input("Username: ")
            password = input("Introduce la contraseña: ")
            check=func.checkUserbdd(user,password)
            if check==0:
                print("Este usuario no existe")
            elif check==-1:
                print("Contraseña incorrecta")
            elif check==1:
                print("Usuario y contraseña correctos")
                '''Aventuras disponibles getFormatedAdventures()'''
                adventure=input("Escoge una aventura: ")

    if opc==2:
        usercheck = False
        while usercheck == False:
            user = input("Username: ")
            usercheck = func.checkUser(user)
            exists=func.userExists(user)
            if exists==False:
                passwordcheck = False
                while passwordcheck == False:
                    password = input("Password: ")
                    passwordcheck = func.checkPassword(password)
                if usercheck and passwordcheck:
                    func.insertUser(user,password)
                    opc=False
            else:
                print("Este usuario ya existe")
                opc=False

    if opc==3:
        while True:
            crrect = False
            replay = []
            for i in func.getGames():
                for j in i:
                    print(j, end=" ")
                print()
            option = input("What adventure you want replay?: ")
            for i in func.getGames():
                if option == str(i[0]):
                    replay = [i[0], i[2]]
                    crrect = True
            if crrect:
                historylist = func.getHistory(replay[0])
                print(str(replay[1]).center(100, "*"))
                for i in range(len(historylist)):
                    queryreplays = f"select description from STEP where id_step='{historylist[i][0]}'"
                    cur.execute(queryreplays)
                    replays = cur.fetchall()
                    print(replays[0][0], "\n\n")
                    queryreplays = f"select description from ANSWER where id_current_step='{historylist[i][0]}'"
                    cur.execute(queryreplays)
                    replays = cur.fetchall()
                    for j in range(len(replays)):
                        print(j + 1, replays[j][0])
                    print("\nOpcion seleccionada: ", end="")
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

    if opc==4:
        break

