class Triangulo:
    def __init__(self, Lado1, Lado2, Lado3):
        self.lado1 = Lado1
        self.lado2 = Lado2
        self.lado3 = Lado3

    def imprimirLadoMayor(self):
        ladoMayor = max(self.lado1, self.lado2, self.lado3)
        print("El lado con mayor medida es:", ladoMayor)

    def determinarTipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            tipo = "equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            tipo = "isósceles"
        else:
            tipo = "escaleno"
        print("El triángulo es de tipo:", tipo)


lado1 = float(input("Ingrese el valor del lado 1: "))
lado2 = float(input("Ingrese el valor del lado 2: "))
lado3 = float(input("Ingrese el valor del lado 3: "))

triangulo1 = Triangulo(lado1, lado2, lado3)
triangulo1.imprimirLadoMayor()
triangulo1.determinarTipo()