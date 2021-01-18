"""
Es un algoritmo eficiente para encontrar un elemento en una lista ordenada de elementos. 
Funciona al dividir repetidamente a la mitad la porción de la lista que podría contener al elemento,
hasta reducir las ubicaciones posibles a solo una.
"""
objetivo = int(input('Escoge un numero: '))
epsilon = 0.001
bajo = 0.0
alto = max(1.0, objetivo)
# aqui generamos el valor medio de nuestro conjunto, a lo cual se puede genera el condicional (if)
# para elegir la mitad menor o la mitad mayor.
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2
# Repitiendo este loop, llegará un punto en el que el conjunto sea muy pequeño, y hallaremos la raiz cuadrada.
# Los loops necesarios serán mucho menos que si usamos busqueda exhaustiva o aproximacion
print(f'La raiz cuadrada de {objetivo} es {respuesta}')