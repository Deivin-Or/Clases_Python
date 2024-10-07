# Que son las funciones
# Las funciones son bloques de codigo que se pueden reutilizar y ejecutar varias veces
# no duplicar codigo
# dividir una tarea compleja en varias especificas 
# # ocultar los detalles de la implementacion 
# Mejora la legibilidad del código 
# Mejora la trazabilidad del código

# la sentencia ddef se usa para definir las funciones

# Funcion simple 
def funtion_simple():
    # docstring o cadenas de documentación para indicar hace cada funcion que creemos
    """ Está funsion no hace nada
    """
    pass

print("antes de llamar a la funcion")
funtion_simple()
print("Ya se ha llamado a la función")

# funcion que saluda al mundo

def saludo():
    '''Funicon que saluda al mundo'''
    print("Hola mundo")

print("antes de llamar a la funcion")
funtion_simple()
saludo()
print("Ya se ha llamado a la función")

help(saludo)
help(funtion_simple)
# Los parametros es lo que va dentro de los parentesis
# los parametros son variables que vamos a utilizar para dar valores de entradada en diferentes funciones o métodos.
