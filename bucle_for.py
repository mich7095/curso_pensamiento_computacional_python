"""
Una segunda forma de crear un bucle definido es iterando en una colección de objetos.
Esta es la forma que Python utiliza:

for <variable> in <iterable>:
    <expresión>

En la definición anterior debemos entender <iterable> como una colección de objetos; 
la <variable> como el elemento específico que se está exponiendo mediante el bucle en cada iteración.
"""

frutas = ['manzana', 'pera', 'mango']
for fruta in frutas:
    print(fruta)