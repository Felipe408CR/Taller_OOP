from abc import ABC, abstractmethod


class Deporte(ABC):
    def __init__(self, Nombre):
        self.nombre = Nombre

    @abstractmethod
    def jugar(self):
        pass

class Futbol(Deporte):
    def jugar(self):
        return "¡Gol!"


class Baloncesto(Deporte):
    def jugar(self):
        return "¡Canasta!"


class Tenis(Deporte):
    def jugar(self):
        return "¡Punto!"

def jugarDeporte(deporte):
    print(deporte.jugar())

class Competencia:
    def __init__(self):
        self.deportes = []

    def agregarDeporte(self, deporte):
        self.deportes.append(deporte)

    def jugarDeportes(self):
        for deporte in self.deportes:
            jugarDeporte(deporte)


# Ejemplo de uso
competencia = Competencia()

futbol = Futbol("Fútbol")
baloncesto = Baloncesto("Baloncesto")
tenis = Tenis("Tenis")

competencia.agregarDeporte(futbol)
competencia.agregarDeporte(baloncesto)
competencia.agregarDeporte(tenis)

competencia.jugarDeportes()
