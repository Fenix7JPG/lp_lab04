class Persona():
    def __init__(self, identificacion, nombre, apellido):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__apellido = apellido

    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido

    identificacion = property(get_identificacion, set_identificacion)
    nombre = property(get_nombre, set_nombre)
    apellido = property(get_apellido, set_apellido)


class EstudianteIS(Persona):
    def __init__(self, identificacion, nombre, apellido, semestre):
        Persona.__init__(self, identificacion, nombre, apellido)
        self.__semestre = semestre

    def get_semestre(self):
        return self.__semestre

    def set_semestre(self, semestre):
        self.__semestre = semestre

    semestre = property(get_semestre, set_semestre)

    def __str__(self):
        return "EstudianteIS: " + self.nombre + " " + self.apellido + ", ID: " + str(self.identificacion) + ", Semestre: " + str(self.semestre)


class Cliente(Persona):
    def __init__(self, identificacion, nombre, apellido, direccion_fiscal, codigo_postal, estado):
        Persona.__init__(self, identificacion, nombre, apellido)
        self.__direccion_fiscal = direccion_fiscal
        self.__codigo_postal = codigo_postal
        self.__estado = estado

    def get_direccion_fiscal(self):
        return self.__direccion_fiscal

    def set_direccion_fiscal(self, direccion_fiscal):
        self.__direccion_fiscal = direccion_fiscal

    direccion_fiscal = property(get_direccion_fiscal, set_direccion_fiscal)

    def get_codigo_postal(self):
        return self.__codigo_postal

    def set_codigo_postal(self, codigo_postal):
        self.__codigo_postal = codigo_postal

    codigo_postal = property(get_codigo_postal, set_codigo_postal)

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    estado = property(get_estado, set_estado)

    def __del__(self):
        print("Cliente", self.nombre, "eliminado")


class Empleado(Persona):
    def __init__(self, identificacion, nombre, apellido, fecha_ingreso, cargo, sueldo=2500):
        Persona.__init__(self, identificacion, nombre, apellido)
        self.__fecha_ingreso = fecha_ingreso
        self.__cargo = cargo
        self.__sueldo = sueldo

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    def set_fecha_ingreso(self, fecha_ingreso):
        self.__fecha_ingreso = fecha_ingreso

    fecha_ingreso = property(get_fecha_ingreso, set_fecha_ingreso)

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo

    cargo = property(get_cargo, set_cargo)

    def get_sueldo(self):
        return self.__sueldo

    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo

    sueldo = property(get_sueldo, set_sueldo)

    def __str__(self):
        return "Empleado: " + self.nombre + " " + self.apellido + ", Cargo: " + self.cargo + ", Sueldo: " + str(self.sueldo)
