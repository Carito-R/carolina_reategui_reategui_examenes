"""
Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiantes.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio
"""

procesar_notas = {"Carlos": [12, 14, 15], "Gabriel": [11, 10, 10], "Luna": [12, 16, 18]}

print("Las notas de Carlos son las siguientes: {}". format(procesar_notas["Carlos"]))
print("Las notas de Gabriel son las siguientes: {}". format(procesar_notas["Gabriel"]))
print("Las notas de Luna son las siguientes: {}". format(procesar_notas["Luna"]))

prom_carlos = (12 + 14 + 15)/3
prom_gabriel = (11 + 10 + 10)/3
prom_luna = (12 + 16 + 18)/3

print((f"{prom_carlos:.2f}"), (f"{prom_gabriel:.2f}"), (f"{prom_luna:.2f}"))

prom_estudiantes = {"Carlos": {"promedio": 13.67, "estado": "aprobado"}, "Gabriel": {"promedio": 10.33, "estado": "desaprobado"}, "Luna": {"promedio": 15.33, "estado": "aprobado"}}

prom_estudiantes_values = list(prom_estudiantes.values())
print(prom_estudiantes_values)

print("Carlos fue el estudiante con mayor promedio del curso: {}". format(prom_estudiantes["Carlos"]))
