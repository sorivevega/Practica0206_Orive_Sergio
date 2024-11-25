#Escribir un programa que guarde en un diccionario los precios de los artículos de la tabla, pregunte al usuario por un artículo, un número de unidades y muestre por pantalla el precio de esa cantidad de producto. Si el producto no está en el diccionario debe mostrar un mensaje informando de ello.
producto = {'pan':1.4, 'huevos':2.30, 'cebolla':0.85, 'aceite':4.30}
compra = input('¿Que quieres comprar? ')
if compra in producto.keys():
    cantidad = input('¿Cuanta cantidad quieres comprar? ')
    print('Vas a tener que pagar', producto.get(compra) * cantidad, '€')
else:
    print('No tenemos existencias de ese producto')