#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas, hasta que el usuario introduzca la palabra “terminar”. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
Traducctor = {}
traduccion = input('Escribe una palabra y su traduccion separada por (:),'
                   'si se quieren añadir palabras, deben estar separadas por una coma: ')
traduccion = traduccion.split(',')
traduccion.pop(-1)
for i in range(len(traduccion)):
    clave,valor = traduccion[i].split(':')
    Traducctor[clave] = valor
Frase = (input('Escribe la frase que quieras traducir al ingles')).capitalize()
Frase = Frase.split()
for i in Frase:
    if i in Traducctor:
        print(Traducctor[i])
    else:
        print(i)