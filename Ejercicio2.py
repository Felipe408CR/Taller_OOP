class Personas:
    def __init__(self, Nombre, Edad):
        self.nombre = Nombre
        self.edad = Edad

    def mostrarDatos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

    def mayorEdad(self):
        if self.edad >= 18:
            print("La persona es mayor de edad")
        else:
            print("La persona es menor de edad")

persona1 = Personas("Juan", 5)
persona1.mostrarDatos()
persona1.mayorEdad()
