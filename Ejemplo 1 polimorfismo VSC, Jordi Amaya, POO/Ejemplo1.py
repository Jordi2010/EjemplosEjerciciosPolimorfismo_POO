# Ejemplo 1 de polimorfismo
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

class Persona1:
    pass
    def idioma():
        return 'Luis habla en Aleman'

class Persona2:
    def idioma():
        return 'Pedro habla en Ruso'
    
persona1 = Persona1
persona2 = Persona2
print (persona1.idioma())
print (persona2.idioma())