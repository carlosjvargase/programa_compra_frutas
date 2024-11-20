'''
Ej 4:
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla.
Pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese
número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
informando de ello.

'''

dict_frutas = {
    'banano': 3500,
    'manzana': 1500,
    'pera': 1800,
    'naranja': 2000,
    'sandia': 5000,
    'mango': 4500,
    'durazno': 5500,
    'aguacate': 3000,
    'limon': 2500
}

while True:
  seguir = input('Desea comprar comprar una Fruta (Si/No): ').lower()
  if seguir == 'no':
    print('Muchas gracias por visitar nuestra tienda!!')
    break
  elif seguir == 'si':
    fruta = input('Digita la fruta: ').lower()
    if fruta in dict_frutas:
      kilos = float(input('Cuantos kilos desea llevar: '))
      precio = dict_frutas[fruta]*kilos
      print(f'El costo total de {fruta} es de: ${precio}')
    else:
      print('La Fruta ingresada no hay en este momento.')
  else:
    print('Ingrese una opcion válida.')