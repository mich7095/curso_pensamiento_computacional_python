print('AHORA TRABAJAREMOS CON DICCIONARIOS!')
estudiantes = {'mexico':10,'colombia':15,'puerto_rico':4}#El diccionario es un iterable o recorrible
#Por lo tanto vamos a recorrerlo con un fora continuación
for pais in estudiantes:
    print(pais)
print('\n')

for pais in estudiantes.keys():#Entiendo, según los apuntes de Platzi, esto hace lo mismo anterior
                               #porque recorre las llaves del diccionario (KEYS!)
    print(pais)
print('\n')

for pais in estudiantes.values():#Aquí ya cambia, recorre es los valores del diccionario
    print(pais)
print('\n')

for pais in estudiantes.items():#Aquí recorre los items del diccionario, o sea toda la info
    print(pais)
print('\n')