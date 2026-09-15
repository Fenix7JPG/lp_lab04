from vehiculo import Coche, Moto, Vehiculo

c = Coche("Porsche", "944")
m = Moto("Honda", "Goldwin")

print("Coche:", c.marca, c.modelo)
print("Moto:", m.marca, m.modelo)

c.n_ruedas = 4
m.n_ruedas = 2

print("Ruedas del coche:", c.n_ruedas)
print("Ruedas de la moto:", m.n_ruedas)
print("Ruedas de la clase Vehiculo:", Vehiculo.n_ruedas)
print("El coche es un Vehiculo:", isinstance(c, Vehiculo))
print("Moto hereda de Vehiculo:", issubclass(Moto, Vehiculo))
