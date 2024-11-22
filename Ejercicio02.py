#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>”
name = input('Introduce tu nombre: ')
age = int(input('Introduce tu edad: '))
direction = input('Introduce tu direccion: ')
tlf = int(input('Introduce tu numero de tlf: '))

info = {'nombre':name, 'edad':age, 'direccion':direction, 'Tlf':tlf}
print(info['nombre'], 'tiene', info['edad'], 'años, vive en', info['direccion'], 'y su numero de telefono es, ', info['Tlf'])