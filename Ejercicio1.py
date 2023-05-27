class Estudiante:
    def __init__(self, Nombre, Nota):
        self.nombre = Nombre
        self.nota = Nota

    def imprimirInformacion(self):
        print("Nombre del estudiante:", self.nombre)
        print("Nota del estudiante:", self.nota)

    def mostrarResultado(self):
        if self.nota >= 5:
            resultado = "Aprobado"
        else:
            resultado = "Reprobado"

        print("Resultado:", resultado)

estudiante1 = Estudiante("Juan", 7.5)
estudiante1.imprimirInformacion()
estudiante1.mostrarResultado()
