# if
# Es usada para la toma de decisiones
# Se utiliza para ejecutar el bloque de código si se cumplen una condición en especifico.

# en este caso usamos if para imprimer guau guau si cumple y si que con el bloque de codigo 
# si no se cumpe el requisto este no imprimra nada y seguira con el bloquye de código siguiente.
animal = input("Dame un nombre de un animal: ")
if animal == "perro":
    print("guau guau")
print("no conozco muchos animales")

# Second example:

num = int(input("Dame un número: "))
if num < 0:
    num = -num
print(f"Su valor absoluto es {num}")

# If else estructure
# Es una estructura que permite ejecutar un bloque de código si se cumple una condición y 
# otro bloque de código si no se cumple la condición.
# En otras palabra la sentencia else está en oposición al condicinal if.

animal = input("Dame un nombre de un animal: ")
if animal == "perro":
    print("guau guau")
else:   
    print("no conozco su sonido")

# If elif else estructure
# Es utilizada si tenemos varias condiciones a evaluar.

animal = input("Dame un nombre de un animal: ")
if animal == "perro":
    print("guau guau")
elif animal == "gato":
    print("miau miau")
elif animal == "vaca":
    print("muuu")
else:
    print("no conozco su sonido")
print("no conozco muchos animales")


