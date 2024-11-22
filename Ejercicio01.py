#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
moneda = input('¿Que divisa utilizas?: ')
divisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
if moneda in divisa.keys():
    print(divisa.get(moneda))
else:
    print('No esta') 