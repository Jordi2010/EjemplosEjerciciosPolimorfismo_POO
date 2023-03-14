# Ejercicio 2 de polimorfismo
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

from Personajes import Personajes
from Animes import Animes
from Personajes import personaje3
from Animes import anime3
from Canal1 import Canal1
from Canal2 import Canal2


class Canal3(Personajes,Animes):
    def verAnime():
        return "Están dando a {} de {} en el canal FUNIMATION.".format(personaje3.nombrePersonaje, anime3.nombreAnime)
    
programa1=Canal1
programa2=Canal2
programa3=Canal3
print(programa1.verAnime())
print(programa2.verAnime())
print(programa3.verAnime())