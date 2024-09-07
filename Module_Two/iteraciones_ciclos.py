# whiile = mientras cierta condicion booleana sea verdadera, mientras la condicion sea real
# esta evelua la expresion es true evalua buevamente el ciclo, en false solo salta el código dandolo por terminado el ciclo

x = 1

while x <= 10:
    print(x)
    x += 2
# Es deceir que mientras x sea emnor a 10 imprimira x sumado más dos. (hasta que llegue a superar a 10)

factorial = 5
contador = factorial - 1

while contador > 0:
    factorial *= contador # significa factorial = factorial * contador
    contador -= 1 # significa contador = contador - 1
# esta multiplicara cada ciclo hasta que contador sea 0 o menor

print("El factorial de 5 es: ", factorial)

# Ciclo for sirve para repetir bloques de código en elementos iterables como listas, tuplas, diccionarios, etc.
# Iterable: objeteo que cuenta con varios elementos o valores, que se puede realizar una acción elemento por elemento.
# for = para cada elemento del iterable es
# mietras haya un elemento sin ejecutar este seguira con la ejecución de caso contrario se dará por terminado el for
# tambien permite elegir cuales elementos del iterable se van a ejecutar y con que frecuencia
#nota habra una variable la cual permitira recopilar la información de los elementos del iterable

for i in 1, 2, 3:
    print(i)

# range especifica cual es el rango de los elementos
for i in range(3):
    print(i)

# sobre lsitas de strings
# Este for solo se itera sobre una cadena de caracteres.
# y puede anidar otras estructuras de control dentro.
for i in ["Ale", "Maria", "Luis", "Ana", "Juan","Iván", "Monse", "Luis", "Rafa", "Luca"] :
    print(i)

for i in " Hola Mundo ":
    if i == "M":
        pass
    else:
        print(i, end = " ")
# pasas por cada elemento y al identificar M lo salta gracias a la estructura de control if
# ademas estas estructucturas como if if else elif while y for se puede anidar
# es decir que todas las estructuras de control puden anidar otras estructuras de control ya sean otras o otras mismas (como ejemplo usar un for dentro de un for)
