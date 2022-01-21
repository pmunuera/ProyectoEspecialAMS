import pymysql
import funcions as func
conn=pymysql.connect(host="20.126.87.93",user="delegado",password="delegado",db="RPM")
cur=conn.cursor()
opc=False
while opc==False:
    opc=func.getOpt()
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
                print(func.playgame(func.chooseadventure(func.choosechar(func.getCharacter()))))
        opc=False

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
        func.replay()
        print()
        opc=False

    if opc==4:
        func.reportsmenu()
        opc=False

    if opc==5:
        break

