"""
Ecribir un programa con las siguientes requisitos:
- Crear una clase llamada Empleado donde sus atributos deben ser nombre, edad, sueldo y de nacionalidad peruana,
  tendrá un método para solicitar su nombre y otro para solicitar su edad. Así como un método cumpleaños donde
  cada vez que invoque aumentará en un año la edad de la persona.
- Crear la instancia de la clase Empleado y usar el nuevo método aumentoSueldo que incrementar su sueldo en un 30%
  (mínimo instanciar la clase 2 veces, mostrar por pantalla dicho sueldo ya incrementado).
- Crear un siguiente método prediccion() que retorne un mensaje donde indique que: “En el año XXXX tendrá XX años”,
  el año se ingresará por parámetro y la edad también, realizar una validación si la edad ingresada por parámetro es
  menor a la del constructor indicar que no es posible realizar la operación (Mostrar por pantalla este valor)
Aplicando la definición de Herencias. Crear una clase llamada Persona (Que heredará de la anterior Clase) y agregar
un atributo sueldo a esta clase
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual que tiene la persona) para la clase mencionada
- El método transferencia hace que la clase Empleado que llame al método pueda transferir la cantidad monto al objeto Empleado2
  por consiguiente deberá ir actualizando también el saldo o monto que tiene el otro empleado en su cuenta cada vez que use el
  método transferencia
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e imprimir “Saldo insuficiente”. Comprobar instanciado la
  clase realizando una transferencia y con dos personas.
"""

class Empleado:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sol_nombre(self):
        return f"Nombre del empleado: {self.nombre}"

    def sol_edad(self):
        return f"Edad del empleado: {self.edad}"

"""Instancia de la clase Empleado"""

empleado_1 = Empleado("Carolina", 31)

print(empleado_1.sol_nombre())
print(empleado_1.sol_edad())

class Persona(Empleado):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo