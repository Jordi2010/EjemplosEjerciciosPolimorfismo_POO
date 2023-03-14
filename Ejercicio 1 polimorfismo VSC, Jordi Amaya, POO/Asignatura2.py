# Ejercicio 1 de polimorfismo
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

from Estudiantes import Estudiantes
from Estudiantes import estudiante2

class Asignatura2(Estudiantes):
    def estudiar():
        return "El estudiante {} {} va a estudiar de la asignatura PROGRAMACIÓN.".format(estudiante2.nombre, estudiante2.apellido)