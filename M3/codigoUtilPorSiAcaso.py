'''userExists=False
        while userExists==False:
            user=input("Username: ")
            userExists=func.userExists(user)
        password=""
        queryPasswordCheck = f'select password from USERS where username={user}'

        cur.execute(queryPasswordCheck)

        correctPassword = cur.fetchall()
        while password!=correctPassword:
            password=input("Introduce la contraseña correcta: ")'''