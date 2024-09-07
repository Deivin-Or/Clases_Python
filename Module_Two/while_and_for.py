# while sentence

# Es una condicional que permite crear un ciclo
# en donde ejecutara el bloque de código hasta que cierta condición se booleana se cumple.
# While in spanish is mientras

# una forma de describirlo es, un profesor toma lista de los estudiantes siempre y cuando haya 
# un alumno en la siguiente posición de la lista.

# first example
print("Impares menores a 10")
x = 1

while x <= 10:
    print(x)
    x += 2
# Mientras x sea menor a 10 se le sumará 2 numeros

# second example
factorial = 5
contador = factorial - 1

while contador > 0:
    factorial = factorial * contador
    # Tambien se escribe como factorial *= contador
    contador -= 1
    # Tambien se escribe como contador = contador - 1
print(f"el factoreial de 5 es {factorial}")
# Para extraer un factorial es multiplicar los anteceroes de un número ejemplo 5 se tienen que multiplizar por 4, 3, 2, 1
# en este caso se hace el blo que de cófigo para que contador sea un numero menor a factorial y asi evitar multiplicar el número por 
# si mismo, y mientras contador sea mayor a cero se guiera multiplicando y contador restara un número por cada multipliceción
# hasta que contador sea igual a cero y se salga del ciclo.



# for cycle
# Es un ciclo que permite recorrer una lista de elementos
# Es decir pertite generar un ciclo sobre un elemento iterable
# Iterable es decir un objeto que cuenta con vairos elementos con los cuales podemos realizar una acción con cada uno.

# first example
# Al aplicar el mismo bloque de código a diferentes elementos. Se puedennusar variables.
for i in 1,2,3:
    print(i)

# Second example
# al implentar range su pede utilizar delimitar hast donde queremos que se aplique dicho ciclo
# Ojo dará los resultados del 0 al 5 ya que igual a los indices en una lista tienen un numero exluyente
for i in range(5):
    print(i)

# Third example
# Se puede aplicar en listas

for i in [1,2,3,4,5]:
    print(i)

# Fourth example
# Las cadenas de strings tambien fucnionan para dar condiciones

for i in "Hola mundo":
    if i == "m":
        pass # la sentencia pass es para terminar el ciclo si ya no hay nada que hacer
    #investigar por usa u
    else:
        print(i,end = " ")