print("Bienvenido al sistema de computación de años")

actual_year = input("Ingrese el año actual: ")
if actual_year.isdigit():
    actual_year = int(actual_year)
else:
    print("El año ingresado no es válido")
    exit()

user_year = input("Ingrese el año que deaea calcular: ")
if user_year.isdigit():
    user_year = int(user_year)
else:
    print("El año ingresado no es válido")
    exit()

if actual_year == user_year + 1:
    print(f"El año {user_year} ya pasó, ha pasado un año.")
elif actual_year == user_year - 1:
    print(f"El año {user_year} será el año que viene")
    exit()
else:
    if user_year == actual_year:
        print("El año ingresado es el mismo que el año actual")
    elif user_year > actual_year:
        print(f"Faltan {user_year - actual_year} años para el año {user_year}")
    elif actual_year > user_year:
        print(f"Han pasado {actual_year - user_year} años desde el año {user_year}")
    else:
        print("El año que ingres o no es váildo intente de nuevo")