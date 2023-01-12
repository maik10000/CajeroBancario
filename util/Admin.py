class Admin:
    def __init__(self, nombre, cedula, correo):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula

    def get_correo(self):
        return self.__correo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def set_correo(self, correo):
        self.__correo = correo