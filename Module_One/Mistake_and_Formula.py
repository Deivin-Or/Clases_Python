numHuevos = 12 # Error de concatenar sin hacer cast o una print formateado
# print('Tengo' + numHuvos + 'huevos')

# Opcion 1
print('Tengo ' + str(numHuevos) + ' huevos')

# Opcion 2
print('Tengo %s huevos' %(numHuevos)) # %s indica que hay una variable en el string y luego se señala la variable usando %s

"""Error de Lógica"""
# Calcular la superficie o área de un cuadrado

lado = int(input('Ingrese la medidad del área de un cuadrado: \n\t'))
# superficie = lado * lado * lado # Ojo esta no es la formula solo es un ejemplo de un error de lógica.
# print('La superficie del cuadrado es: ' + str(superficie))

# Solución 
superficie = lado ** 2
print('La superficie del cuadrado es: ' + str(superficie))
