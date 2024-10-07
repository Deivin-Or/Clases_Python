# def sumar(parametro1, parametro2):
#     '''Funcion que suma dos parametros y los muestra en pantalla'''
#     print('Suma', parametro1 + parametro2)

# argumento1 = 5
# argumento2 = 7

# estamos invocando a la funcion por medio de parametros variables.
# sumar(argumento1, argumento2)

# invocando a la funcion por medio de parametros de valor
# sumar('mundo!', 'Hola ')
# sumar('Hola ', 'Mundo!')

# sumar ('Hola')

# Parametros opcionales

def muestra_alumno(nombre, edad = 18, sexo = 'F'):
    '''Funcion que muestra en pantalla los datos de un alumno
    recibe tres parametros
    1. nombre
    2. edad = 18
    3. sexo = 'F'
    '''
    print(f'Nombre: {nombre}, edad: {edad}, sexo: {sexo}')

# Ejecución de función con parámetro obligatorio
muestra_alumno('Pedro')

# ejecucion de funcion con parámetro obligatorio y uno opcional
muestra_alumno('Maria', 22)

# ejecucion de funcion con el primer y ultimo parámetro
muestra_alumno('Juan', sexo = 'M')