class Padre():
    def __init__(self):
        self.x = 8
        print("Constructor clase padre")

    def metodo(self):
        print("Ejecutando método de clase padre")


class Hija(Padre):
    def __init__(self):
        print("Constructor hija")

    def metHija(self):
        print("Método clase hija")
