"""# text_variado = 'Palabra 123  0-* #%&'"""
# print(type(text_variado))

# Podemos utilizar comillas triples para que el texto se muetre como la cadena que hemos escrito
# print("""Funcionamiento de \
# programa: (Opciones)
#     - 1 Para acceder a opciones
#     - 2 Para salir
# """)

# Subscripting e Indexado
# texto = 'Python'

# # print(texto[0])
# # print(texto[5])
# # print(texto[-1])
# # print(texto[-6])

# # print(texto[6]) # Error! no podemos acceder a una linea que no existe
# # print(texto[-7]) # Error! no podemos acceder a una linea que no existe

# letra = texto[0]
# print(letra)
# # texto[0] = 'p' # Error! no podemos modeificar una cadena

# letra = 'p'
# print(letra)

# texto_compuesto = letra + texto[1] #Concatenación
# print(texto_compuesto)

###########################################################################################################################

# Slicing o substringing

texto = 'Python'
# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])
# print(texto[-4:-2:-1]) # Aqui hay que inidicar el paso negativo ya que se comienza con un nuemro negativo y no confudir rn que direccion se lee la cadena

# print(texto[2:])
# print(texto[:3]) # La el indice final en este caso '3' no se imprimrá o nose tomará en ceunta a la hora de usarlo

# print(texto[-3::-1])

# print(texto[::-1])
# print(texto[1:50])
# print(texto[2:2])



"""Si utilizas un paso negativo diferente a -1, como -2 o -3, al hacer 
slicing en una cadena de texto, Python seleccionará los caracteres en pasos de esa 
magnitud desde el índice inicial hacia atrás."""

# texto = 'PythonProgramming'
# print(texto[-2:-10:-2])  
# print(texto[-2:-12:-3])

#################################################################################################################

# Cadenas y formatos

# texto = 'Hola mundo! Buenastardes'
# print(texto.lower())
# print(texto.upper())
# print(texto.capitalize()) 
# print(texto.title())
# print(texto.swapcase()) 
# texto = texto.upper()
# print(texto)

################################################################################################################

print('{} + {} = {}'.format(2, 3, 2 + 3))
print('{} + {} = {}'.format('Hola', 'Mundo', 'Hola Mundo'))
print('{:.3f} + {:.4f} = {}'.format(2, 3, 2 + 3 ))
print('{1} + {0} = {2}'.format(2, 3, 2 + 3 ))
print('{2} + {0} = {1}'.format('Hola', 'Mundo', 'Hola Mundo'))
print('{:d} = {:b} = {:o} = {:x}'.format(15, 15, 15, 15))