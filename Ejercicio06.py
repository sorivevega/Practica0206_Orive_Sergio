#Escribir un programa que permita gestionar la base de datos de alumnado de un classroom. Los alumnos y alumnas se guardarán en una lista que almacena un diccionario para cada alumno/a en el que la clave de cada alumno/a será su NIF, y el valor será otro diccionario con los datos del alumno/a (nombre, apellidos, teléfono, correo, aprobado), donde aprobado tendrá el valor True si ha aprobado el módulo. El programa debe preguntar al usuario por una opción del siguiente menú:
#(1) Añadir alumno/a
    #Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
#(2) Eliminar alumno/a
    # Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
#(3) Mostrar alumno/a
    #Preguntar por el NIF del alumno/a y mostrar sus datos.
#(4) Listar todo el alumnado
    #Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre
#(5) Listar alumnado aprobado
    #Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
#(6) Terminar.
    #Terminar.


Datos = {}
print('1) Añadir alumno/a:')
print('2) Eliminar alumno/a')
print('3) Mostrar alumno/a')
print('4) Listar todo el alumnado')
print('5) Listar alumnado aprobado')
print('6) Terminar')
opcion = (input('Introduzca el numero segun lo necesario: '))
   

while opcion != '6':
    if opcion == '1':

        print('Usted ha elegido Añadir Alumno/a')
        NIF = input('Introduzca el NIF del alumno: ')
        nombre = input('Introduzca el nombre completo del alumno: ')
        tlf = int(input('Introduzca el telefono del alumno: '))
        correo = input('Introduzca el correo del alumno: ')
        notas = float(input('Introduzca la nota del alumno: '))
        Alumno = {'nombre':nombre,'tlf':tlf,'correo':correo,'notas':notas}
        Datos[NIF] = Alumno
   
    if opcion == '2':
        print('Usted ha elegido Eliminar alumno/a')
        NIF = input('Introduzca el NIF del alumno')
        if NIF in Datos:
            del Datos[NIF]
        else:
            print('Este alumno no esta en nuestra base de datos')


    if opcion == '3':
        print('Usted ha elegido Mostrar alumno/a')
        NIF = input('Introduzca el NIF del alumno')
        if NIF in Datos:
            print (Datos[NIF])
        else:
            print('Este alumno no esta en nuestra base de datos')


    if opcion == '4':
        print(Datos)

    if opcion == '5':
        if tlf >= '5':
            print(Datos[NIF])

    opcion = (input('Introduzca el numero segun lo necesario: '))

        
if opcion == '6':
    print('Adios')