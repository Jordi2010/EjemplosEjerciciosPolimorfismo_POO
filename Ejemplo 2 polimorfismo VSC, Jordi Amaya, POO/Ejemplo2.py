# Ejemplo 2 de polimorfismo
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

class VerTiktok:
    def __init__(self, nombre):
        self.nombre=nombre
tiktoker1=VerTiktok("La tamalera")
tiktoker2=VerTiktok("Wichito")

class Ixar(VerTiktok):
    pass
    def verTikTok():
        return "Ver tiktok de {}".format(tiktoker1.nombre)
    
class Andrea(VerTiktok):
    pass
    def verTikTok():
        return 'Ver tiktok de {}'.format(tiktoker2.nombre)
    
visitante1 = Ixar
visitante2 = Andrea
print (visitante1.verTikTok())
print (visitante2.verTikTok())