class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print("Soy", self.nombre, "y tengo", self.edad, "años")


class Personal():
    def __init__(self, empresa, sueldo):
        self.empresa = empresa
        self.sueldo = sueldo

    def trabajar(self):
        print("Trabajo en", self.empresa, "y gano", self.sueldo, "soles")


class Mantenimiento(Persona, Personal):
    def __init__(self, nombre, edad, empresa, sueldo):
        Persona.__init__(self, nombre, edad)
        Personal.__init__(self, empresa, sueldo)
