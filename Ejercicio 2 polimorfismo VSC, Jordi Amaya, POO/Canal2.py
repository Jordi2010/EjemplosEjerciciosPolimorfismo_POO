# Ejercicio 2 de polimorfismo
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

from Personajes import Personajes
from Animes import Animes
from Personajes import personaje2
from Animes import anime2

class Canal2(Personajes,Animes):
    def verAnime():
        return "Están dando a {} de {} en el canal CRUNCHYROLL.".format(personaje2.nombrePersonaje, anime2.nombreAnime)