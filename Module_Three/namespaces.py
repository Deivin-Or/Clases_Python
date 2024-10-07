# un namespace es el esapcio abstracto en el que viven los identificadores.
# OJO No podemos tener dos identificadores iguales en un namespace

# se pude tener dos identificares iguales siempre y cuando sean en programas distintos para eso hay que saber que son los 
# los namespaces del ambito global y los namespaces locales
# El ámbito global es aquel en el que trabajamos desde que abrimos el intérprete de python.
# es todo que se decalre fuera de una función.

# el ámbito local corresponde al esapcio que sea crea durante la ejecución de una función.
# Este es un esapcio temporal que se eliminara al cerrar la ejecución del programa.
# el ambito local se crea dentro del ámbito global.
# por esa razon las funiciones pueden anidar otras funciones y poder separarlas en niveles inferiores y superiores.

# los objetos de un ámbito superior solo son accesibles como lectura en un ámbito inferiro
# cada vez que creamos una funcion automaticamente se crea una namespce


# Probando ámbitos

titulo = 'Probando ambitos'
suma = 10.5

def sumar():
    suma = 2 + 2
    titulo = titulo + 'mundo'
    print(titulo)
    print('Suma en ambito local', suma, id(suma))

print('Antes de llamar a la funcion')
print('Suma en ambito global', suma, id(suma))
sumar()
print('print despues de llamr a la funcion sumar')
print('Suma en ambito global',suma, id(suma))

# parametros: las variables que se declaran en la definicion de una funcion.
# argumentos: son los valores por los caules se invoca una funcion
# son posicionales, asi que se deben respetar en que posición los dejamos.