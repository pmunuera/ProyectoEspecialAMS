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
                    queryUser = f"insert into USER(username,password) values ('{user}','{password}')"
                    cur.execute(queryUser)
                    conn.commit()
                    print("Usuario creado con exito")
                    opc=False
            else:
                print("Este usuario ya existe")
                opc=False

    if opc==3:
        print()

    if opc==4:
        break

