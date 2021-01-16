"""
Ejemplo visto en la clase 9.
En esta clase vimos que los iteradores son estructuras de control que me permiten 
llevar un flujo siempre que una condición se cumpla. Si esta condición se cumple eternamente,
 y no le decimos al programa que se detenga se generará un infinit loop.
"""
contador_externo = 0
contador_interno = 0

while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        contador_interno += 1

        if contador_interno >= 3:
            break

    contador_externo += 1
    contador_interno = 0