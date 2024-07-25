"""Hacer un formulario simple solicitando al usuario nombres, apellidos, edad, correo y telefono"""

print('Bienvenido al sistema de registro provisional \n')

first_name = input ('Ingrese su primer nombre. \n\t Nombre: ')
second_name = input ('Ingrese su segundo nombre en caso de no tener deje el espacio en blanco. \n\t Segundo nombre: ')
last_names = input ('Ingrese sus apellidos. \n\t Apellidos: ')
old_years = str(input ('Ingrese su edad. \n\t Edad: '))
email = input('Ingrese su correo por ejemplo "correo@example.com". \n\t Correo Electronio: ')
telephone = input ('Ingrese su número telefonico. \n\t Tel: ')

"""Usando prints normales"""
print('\nLos datos regsitrados son: \n')
print('Nobre: ' + (first_name + second_name))
print('Apellidos ' + last_names)
print('Edad: ' + old_years + ' años.')
print('Correo electronico: ' + email)
print('Telefono: ' + telephone)

"""Usando prints formateados"""
# print('Los datos registrados son:')
# print(f'Nombres: {first_name + second_name}')
# print(f'Apellidos: {last_names}')
# print(f'Años de edad: {old_years} años.')
# print('Correo electronico: {email}')
# print(f'Telefono: {telephone}')

