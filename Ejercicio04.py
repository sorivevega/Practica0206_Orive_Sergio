#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
datos = {}
name = input('¿Como te llamas?: ')
age = input('Introduce tu edad: ')
sex = input('¿Cual es tu sexo?: ')
telefono = input('Introduce tu numero de telefono')
datos['Nombre'] = name
datos['Edad'] = age
datos['Sexo'] = sex
datos['Tlf'] = telefono
print(datos)