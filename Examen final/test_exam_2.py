"""
Utilizar el concepto de módulo necesariamente. Y Escribir un programa para el manejo de listas el cuál cumplirá los siguientes
requerimientos (2 ptos):
Reglas:
-Crear una función que le permitirá almacenar X números aleatorios en una lista y finalmente los imprimirá por consola al llamar
 la función. X solo puede ser entero. No otro tipo de dato. Y también un índice existente en la lista.
-Crear una función que le permita almacenar los números no repetidos de la lista anterior, retornar este valor e imprimirlo por consola.
-Crear una función donde se creará una lista para ordenar de mayor a menor la lista que se creó en el ítem anterior (número no repetidos)
 y otra lista para ordenarlas de menor a mayor, retornar este valor e imprimirlos por consola.
-Crear una función para indicar cuál es el mayor número par de la lista (lista del ítem 2), retornar este valor e imprimirlo por consola.
-Crear el archivo principal.py, donde solo llamarás las anteriores funciones que se encontrarán alojadas en un módulo"""

num_enteros = [12, 45, 22, 7, 34, 22, 31, 22, 45]
print(num_enteros)

def eliminar_duplicados(lista):
    vistos = set()  #cojunto vacío
    sin_repetidos = []
    for elemento in lista:
        if elemento not in vistos:
            vistos.add(elemento)
            sin_repetidos.append(elemento)
    return sin_repetidos

num_actualizados = eliminar_duplicados(num_enteros)
print(num_actualizados)

def num_unicos(lista):
    return sorted(num_actualizados, reverse=True)

print(num_unicos(num_actualizados))
