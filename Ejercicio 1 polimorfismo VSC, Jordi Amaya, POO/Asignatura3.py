# Ejercicio 1 de polimorfismo
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

from Estudiantes import Estudiantes
from Estudiantes import estudiante3
from Asignatura1 import Asignatura1
from Asignatura2 import Asignatura2

class Asignatura3(Estudiantes):
    def estudiar():
        return "El estudiante {} {} va a estudiar de la asignatura REDES.".format(estudiante3.nombre, estudiante3.apellido)

materia1=Asignatura1
materia2=Asignatura2
materia3=Asignatura3
print(materia1.estudiar())
print(materia2.estudiar())
print(materia3.estudiar())