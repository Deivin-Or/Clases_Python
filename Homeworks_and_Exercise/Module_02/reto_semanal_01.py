print("Bienvenido al sistema de indicador de edad")

years_old = input("Ingrese su edad: ")

if years_old.isdigit():
    years_old = int(years_old)
else:
    print("Ingrese una edad válida")
    exit() # sirve para interrumpir la ejecución de todo el progreama a diferencia del break que solo corta el ciclo de un bloque especifico de while.
    

if years_old <= 0:
    print("Que edad tan joven!!! pero eso no es posible") # nota parece redudnate pero solo es para hacer constar que es una edad que no es posible para el programa.
elif years_old > 115:
    print("Al parecer eres demasiado mayor")
elif years_old < 18:
    print("Eres menor de edad")
else:
    print("Tienes la edad suficiente")