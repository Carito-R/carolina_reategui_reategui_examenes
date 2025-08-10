"""
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original
"""

normalizar_nombres = "maria    bruno raul fabiola    roger alessia alessia alessia"
print(normalizar_nombres)

norm_nomb_sin_espacios = normalizar_nombres.split()

print("Lista de nombres: {}".format(norm_nomb_sin_espacios))

nombres_titulo = normalizar_nombres.title()

print("Nombres a formato título: {}".format(nombres_titulo))

def eliminar_duplicados(norm_nomb_sin_espacios):
    vistos = set()
    sin_repetidos = []
    for elemento in norm_nomb_sin_espacios:
        if elemento not in vistos:
            vistos.add(elemento)
            sin_repetidos.append(elemento)
    return sin_repetidos

print(eliminar_duplicados(norm_nomb_sin_espacios))

