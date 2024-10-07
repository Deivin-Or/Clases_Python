# utilizar almenos dos funciones
# Preguntar cuantos alumnos se registrarán, en caso de no ingresar una cantidad, se asume que se registrarán 3 alumnos.
# Preguntará el nombre y dos calificaciones.
# Mostrar el nombre en pantallla con inicial mayúscula y promedio.
# Al finalizar el programa se mostrará una lista con el nombre de cada alumno y sus calificaciones.

number_students = input('¿Cúantos alumnos se registrarán? ')

def students_capture(number = 3):
    '''
    Registra alumnos y dos calificaciones
    Recibe copmo parametro la cantidad de alumnos a registrar
    Si no se especifica el número de alumnos se registraran 3
    '''
    students_list = []
    for _ in range(number):
        name = input(f'{_ + 1}.-Ingrese el nombre del alumno: ').capitalize()
        calification_1 = int(input(f'Ingrese la calificación de {name}: '))
        calification_2 = int(input(f'Ingrese la calificación de {name}: '))
        students_list.append([name, calification_1, calification_2])
        promedio(name, calification_1, calification_2)
    print('Las calificaicones de los alumnos son', students_list)


def promedio(name, calification_1, calification_2):
    '''
    Calcula el promedio de un alumn y lo despliega en pantalla por emdio de un mensaje
    Recibe como parámetors el nombre y dos calificaciones del alumno
    '''
    promedio = (calification_1 + calification_2) / 2
    print(f'El promedio de {name} es {promedio}')


if number_students.isdigit():
    number_students = int(number_students)
    students_capture(number_students)
else:
    students_capture()