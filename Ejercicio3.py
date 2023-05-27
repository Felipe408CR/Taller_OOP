import math

class RaizCuadrada:
    def __init__(self, Numero):
        self.numero = Numero

    def calcularRaizCuadrada(self):
        if self.numero < 0:
            print("El número debe ser positivo.")
        else:
            raiz = math.sqrt(self.numero)
            print("La raíz cuadrada de", self.numero, "es:", raiz)


numero1 = float(input("Ingrese un número: "))
raiz_cuadrada1 = RaizCuadrada(numero1)
raiz_cuadrada1.calcularRaizCuadrada()