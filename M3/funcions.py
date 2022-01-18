import pymysql
import funcions as func
conn=pymysql.connect(host="20.126.87.93",user="delegado",password="delegado",db="RPM")
cur=conn.cursor()
def get_answers_bystep_adventure():
    queryAdventureSteps = f'select id_steps from STEP where id_adventure={adventure}'

    cur.execute(queryAdventureSteps)

    rowsAdventureSteps = cur.fetchall()

    queryAdventureAnswer = f'select id_answers from ANSWERS where id_adventure={adventure}'

    cur.execute(queryAnswer)

    rowsAdventureAnswer = cur.fetchall()

    return Answers_ByStep_Adventure[{rowsAdventureAnswer,rowsAdventureSteps}]

def get_adventures_with_chars():
    return adventures

def get_bystep_adventure():
    return BySteps_Adventure

def get_first_step_adventure():
    '''return '''

def get_characters():
    return characters

def getReplayAdventures():
    return ReplayAdventures

def getChoices():
    '''getChoices() no es correcta - Esta sería la correcta
Devolvemos una tupla de tuplas binarias donde cada tupla binaria representa un paso y la seleccion
Por ejemplo, empezamos la aventura X, empezamos en el paso 101 y elegimos la opcion 101 ( en este caso la id de opcion coincide con  el id de paso )
Esta eleccion nos lleva al paso 103, en el que escogemos la opcion 108.
Esta elección nos lleva al paso 108 donde escogemos la opción 110 y se acaba la aventura.
En este caso, si escogemos revivir esta aventura, la función nos devolvería:
((101, 101), (103, 108), (108, 110))'''
    queryChoices=f"select id_step from GAME"

def getIdGames():
    '''return '''

def insertCurrentGame(idGame,idUser,idChar,idAdventure):
    '''return '''

def getUsers():
    '''return '''

replayAdventures={1:{'idUser':1,'Username':'username',
                          'IdADventure':'id_adventure',
                          'Name':'adventure_name',
                          'date':'date',
                          'idCharacter':'id_character',
                          'CharacterName':'character_name'},
                2:{'idUser':  2,'Username':'username2',
                          'IdADventure':'id_adventure',
                          'Name':'adventure_name',
                          'date':'date',
                          'idCharacter':'id_character',
                          'CharacterName':'character_name'}

                  }

def getUserIds():
    usersAndIds=[]
    users=[]
    userIds=[]
    for i in replayAdventures:
        users.append(replayAdventures[i]['Username'])
    for i in replayAdventures:
        userIds.append(replayAdventures[i]['idUser'])
    usersAndIds.append(users)
    usersAndIds.append(userIds)
    return usersAndIds
#print(getUserIds())

def insertUser(user,password):
    queryUser = f"insert into USER(username,password) values ('{user}','{password}')"
    cur.execute(queryUser)
    conn.commit()
    conn.close()
    print("Usuario creado con exito")

def get_table(query):
    tupla=()
    cur.execute(query)
    columnas = cur.description
    tupla.append(columnas[0],columnas)
    print(tuplas)
    conn.close()

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


def setIdGame():
    '''return '''

def insertCurrentChoice(idGame,actual_id_step,id_answer):
    '''return '''

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
        textLinea.append(linea+" "*(tupla_sizes[j]+margin-len(linea)))
        linea = ""
        textLinea=[]
        for i in texts[j]:
            if j!=len(texts):
                if len(linea)+len(i)+1+margin > tupla_sizes[j]:
                    linea+=" "*(tupla_sizes[j]+margin-len(linea))
                    textLinea.append(linea)
                    linea = ""
                    linea += i + " "
                #elif len(tupla_texts[j])<tupla_sizes[j]:
                    #linea = tupla_texts[j]+" "*(tupla_sizes[j]+margin-len(linea))
                    #textLinea.append(linea)
                    #linea=""
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
    for i in range(0,len(textosLineas[c])):
        '''if i>=len(textosLineas[0]):
            print(" "*tupla_sizes[0], end="")
            if i>=len(textosLineas[1]):
                print(" " * tupla_sizes[1]+" "*tupla_sizes[2], end="")'''
        if i<len(textosLineas[0]):
            if i>=len(textosLineas[1]):
                print(textosLineas[0][i])
            else:
                print(textosLineas[0][i], end="")
        if i<len(textosLineas[1]):
            if i>=len(textosLineas[2]):
                print(textosLineas[1][i])
            else:
                print(textosLineas[1][i], end="")
        if i < len(textosLineas[2]):
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
    getFormatedBodyColumns(("Id Adventure", "Adventure", "Description"), (15, 25, 50), margin=0)
    print("*"*130)
    for i in adventures:
        getFormatedBodyColumns((str(i), adventures[i]['Name'], adventures[i]['Description']), (15, 20, 50), margin=0)
#getFormatedAdventures(adventures)

def getFormatedAnswers(idAnswer,text,lenLine,leftMargin):
    '''return '''

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
    '''return '''

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







