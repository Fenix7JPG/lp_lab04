import random
from datetime import datetime, timedelta


class Vehiculo():
    def __init__(self, tipo):
        self.tipo = tipo

    def descripcion(self):
        return "Viaje en " + self.tipo


class Avion(Vehiculo):
    def __init__(self):
        Vehiculo.__init__(self, "avion")

    def descripcion(self):
        return "Viaje en avion"


class Bus(Vehiculo):
    def __init__(self):
        Vehiculo.__init__(self, "bus")

    def descripcion(self):
        return "Viaje en bus"


class Viaje():
    def __init__(self, codigo, vehiculo, origen, destino, fecha, capacidad):
        self.codigo = codigo
        self.vehiculo = vehiculo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.capacidad = capacidad
        self.reservas = 0

    def hayCupo(self):
        return self.reservas < self.capacidad

    def empiezaPronto(self):
        return self.fecha <= datetime.now() + timedelta(hours=1)


class Reservas():
    def __init__(self):
        self.viajes = []

    def crearViajesAleatorios(self, cantidad):
        ciudades = ["Arequipa", "Cusco", "Lima", "Puno", "Tacna"]
        tipos = [Avion(), Bus()]
        i = 0
        while i < cantidad:
            origen = random.choice(ciudades)
            destino = random.choice(ciudades)
            if destino == origen:
                continue
            vehiculo = random.choice(tipos)
            fecha = datetime.now() + timedelta(hours=random.randint(0, 72), minutes=random.randint(0, 59))
            capacidad = random.randint(20, 50)
            viaje = Viaje("V" + str(i + 1), vehiculo, origen, destino, fecha, capacidad)
            viaje.reservas = random.randint(0, capacidad)
            self.viajes.append(viaje)
            i = i + 1

    def buscarViaje(self, codigo):
        for viaje in self.viajes:
            if viaje.codigo == codigo:
                return viaje
        return None

    def mostrarDisponibilidad(self):
        for viaje in self.viajes:
            print("Codigo:", viaje.codigo, "|", viaje.vehiculo.descripcion(), "|", viaje.origen, "->", viaje.destino, "|", viaje.fecha.strftime("%d/%m/%Y %H:%M"), "| Cupo:", viaje.reservas, "/", viaje.capacidad)

    def reservarViaje(self, codigo):
        viaje = self.buscarViaje(codigo)
        if viaje is None:
            print("No existe un viaje con el codigo", codigo)
            return None
        if not viaje.hayCupo():
            print("No se puede reservar el viaje", codigo, ": capacidad maxima alcanzada")
            return None
        if viaje.empiezaPronto():
            print("No se puede reservar el viaje", codigo, ": falta menos de una hora para que comience")
            return None
        viaje.reservas = viaje.reservas + 1
        return viaje

    def cancelarReserva(self, codigo):
        viaje = self.buscarViaje(codigo)
        if viaje is None:
            print("No existe un viaje con el codigo", codigo)
            return None
        if viaje.reservas == 0:
            print("El viaje", codigo, "no tiene reservas por cancelar")
            return None
        viaje.reservas = viaje.reservas - 1
        return viaje


class Pasajero():
    def __init__(self, nombre):
        self.nombre = nombre
        self.misViajes = []

    def reservarViaje(self, reservas, codigo):
        viaje = reservas.reservarViaje(codigo)
        if viaje is not None:
            self.misViajes.append(viaje)
            print("Reserva confirmada para", self.nombre, "en el viaje", viaje.codigo)

    def verViajes(self):
        if len(self.misViajes) == 0:
            print(self.nombre, "no tiene viajes reservados")
            return
        for viaje in self.misViajes:
            print("Codigo:", viaje.codigo, "|", viaje.vehiculo.descripcion(), "|", viaje.origen, "->", viaje.destino, "|", viaje.fecha.strftime("%d/%m/%Y %H:%M"))

    def cancelarViaje(self, reservas, codigo):
        viaje = reservas.cancelarReserva(codigo)
        if viaje is not None:
            self.misViajes.remove(viaje)
            print("Reserva cancelada para", self.nombre, "en el viaje", viaje.codigo)


class Menu():
    def __init__(self):
        self.reservas = Reservas()
        self.pasajero = None

    def reservarViaje(self):
        codigo = input("Ingrese el codigo del viaje: ")
        self.pasajero.reservarViaje(self.reservas, codigo)

    def verMisViajes(self):
        self.pasajero.verViajes()

    def cancelarViaje(self):
        codigo = input("Ingrese el codigo del viaje a cancelar: ")
        self.pasajero.cancelarViaje(self.reservas, codigo)

    def iniciar(self):
        nombre = input("Ingrese su nombre: ")
        self.pasajero = Pasajero(nombre)
        self.reservas.crearViajesAleatorios(6)
        while True:
            print("--- MENU RESERVA DE VIAJES ---")
            print("1. Mostrar disponibilidad de viajes")
            print("2. Reservar un viaje")
            print("3. Ver mis viajes")
            print("4. Cancelar un viaje")
            print("5. Salir")
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                self.reservas.mostrarDisponibilidad()
            elif opcion == "2":
                self.reservarViaje()
            elif opcion == "3":
                self.verMisViajes()
            elif opcion == "4":
                self.cancelarViaje()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida")


menu = Menu()
menu.iniciar()
