from particula import Particula

class ListaParticulas:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, Particula:Particula):
        self.__particulas.append(Particula)

    def agregar_inicio(self, Particula:Particula):
        self.__particulas.insert(0,Particula)
    
    def mostrar(self):
        for Particula in self.__particulas:
            print(Particula)

    def __str__(self):
        return "".join(
            str(Particula) for Particula in self.__particulas
        )

p1 = Particula(1,65,36,44,52,61,78,84,99)
p2 = Particula(10,112,13,124,15,16,17,18,19)
p3 = Particula(213,250,213,2,25,90,66,43,111)

lista = ListaParticulas()
lista.agregar_inicio(p1)
lista.mostrar()
lista.agregar_inicio(p2)
lista.mostrar()
lista.agregar_final(p3)
lista.mostrar()