"""
Reto: Escribir un programa que pida el nombre de dos personas y sus respectivas edades,
despues imprimiras quien es mayor o si las personas tienen la misma edad.
"""

per_1 = str(input('¿Cuál es el nombre de la primera persona? '))
per_2 = str(input('¿Cuál es el nombre de la segunda persona? '))

num_1 = int(input('¿Cuál es la edad de '+ per_1 + '? '))
num_2 = int(input('¿Cuál es la edad de '+ per_2+ '? '))

if num_1 > num_2:
    print(per_1 + ' es mayor')
elif num_1 < num_2:
    print(per_2 + ' es mayor')
else:
    print('Las dos personas tienen la misma edad')