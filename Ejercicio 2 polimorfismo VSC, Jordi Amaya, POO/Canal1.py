# Ejercicio 2 de polimorfismo
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

from Personajes import Personajes
from Animes import Animes
from Personajes import personaje1
from Animes import anime1

class Canal1(Personajes,Animes):
    def verAnime():
        return "Están dando a {} de {} en el canal TVX.".format(personaje1.nombrePersonaje, anime1.nombreAnime)