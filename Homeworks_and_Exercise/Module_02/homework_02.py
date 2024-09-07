print ("Bienvenido al sistema de verificación de contraseñas")

turn = 1


while turn < 4:
    password = input("Ingrese su contraseña: ")
    if password == "":
        print("La contraseña no puede ser un espacio en blanco")
        turn +=1
    elif password[0] in "0123456789":
        break
    else: 
        print("La contraseña debe comenzar con un número")
        turn +=1

while turn < 4:
    password_r = input("ingrese la contraseña nuevamente: ")
    if password == password_r:
        print("Contraseña correcta")
        break
    else:
        print(f"""Las contraseñas no coinciden
abortando proceso, Intento No.: {turn}""")
        turn +=1

