class Admin:
    def __init__(self, nombre, nombre_usuario, correo_ad):
        self.__nombre = nombre
        self.__nombre_usuario = nombre_usuario
        self.__correo_ad = correo_ad

    def get_correo_a(self):
        return self.__correo_ad

    def get_nombre_a(self):
        return self.__nombre

    def get_nombre_usuario(self):
        return self.__nombre_usuario

    def set_correo_a(self, correo_a):
        self.__correo_ad = correo_a

    def set_nombre_a(self, nombre):
        self.__nombre = nombre

    def set_nombre_usuario(self, nombre_usuario):
        self.__nombre_usuario = nombre_usuario
