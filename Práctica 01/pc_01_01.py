"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente.
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un
usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
salario, según corresponda.
"""

nombre = "Camila"
salario = 7000
edad = 34
empresa = "Google"
sal_2 = salario ** 2
sal_porc = (salario * 10)/100
print(sal_porc)
bono_final = sal_2 + sal_porc
print(bono_final)

print(type(nombre))
print(type(salario))
print(type(edad))
print(type(empresa))

edad_str = str(edad)
print(type(edad_str))

if edad > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")

if edad < 30:
    print("Usted tiene un bono del 5% en el mes diciembre")
