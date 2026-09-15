class Tiburon():
    def nadar(self):
        print("El tiburón está nadando.")

    def nadarHaciaAtras(self):
        print("El tiburón no puede nadar hacia atrás, pero puede hundirse hacia atrás.")

    def esqueleto(self):
        print("El esqueleto del tiburón está hecho de cartílago.")


class PezPayaso():
    def nadar(self):
        print("El pez payaso está nadando.")

    def nadarHaciaAtras(self):
        print("El pez payaso puede nadar hacia atrás.")

    def esqueleto(self):
        print("El esqueleto del pez payaso está hecho de hueso.")


###### polimorfismo con métodos de clase ######
sammy = Tiburon()
casey = PezPayaso()

for peces in (sammy, casey):
    peces.nadar()
    peces.nadarHaciaAtras()
    peces.esqueleto()
###### fin polimorfismo con métodos de clase ######
