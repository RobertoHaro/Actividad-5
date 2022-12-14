from algoritmos import distancia_euclidiana

class Particula:
    
    def __init__(self, id=0, origen_x=0<=500, origen_y=0<=500, destino_x=0<=500, destino_y=0<=500, velocidad=0, red=0<=255, green=0<=255, blue=0<=255):

        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x,origen_y,destino_x,destino_y)
    
    def __str__(self):
        return(
            '\nId:        ' + str(self.__id) + '\n' +
            'Origen X:  ' + str(self.__origen_x) + '\n' +
            'Origen Y:  ' + str(self.__origen_y) + '\n' +
            'Destino X: ' + str(self.__destino_x) + '\n' +
            'Destino Y: ' + str(self.__destino_y) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + '\n' +
            'Rojo:      ' + str(self.__red) + '\n' +
            'Verde:     ' + str(self.__green) + '\n' +
            'Azul:      ' + str(self.__blue) + '\n' +
            'Distancia: ' + str(self.__distancia) + '\n' 
        )