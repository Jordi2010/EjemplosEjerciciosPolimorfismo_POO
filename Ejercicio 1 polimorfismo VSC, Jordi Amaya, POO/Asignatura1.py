# Ejercicio 1 de polimorfismo
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

from Estudiantes import Estudiantes
from Estudiantes import estudiante1

class Asignatura1(Estudiantes):
    def estudiar():
        return "El estudiante {} {} va a estudiar de la asignatura MATEMÁTICA.".format(estudiante1.nombre, estudiante1.apellido)