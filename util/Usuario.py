class Usuario:

    def __init__(self, nombre,cedula,saldo,correo,numero_celular,numero_cuenta,ciudad,provincia):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__saldo = saldo
        self.__correo = correo
        self.__numero_cuenta = numero_cuenta
        self.__nuemro_celular = numero_celular
        self.__ciudad = ciudad
        self.__provincia = provincia

    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula

    def get_saldo(self):
        return self.__saldo

    def get_correo(self):
        return self.__correo

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_numero_celular(self):
        return self.__nuemro_celular

    def get_provicia(self):
        return self.__provincia

    def get_ciudad(self):
        return self.__ciudad

    def set_numero_celular(self, numero_celular):
        self.__nuemro_celular = numero_celular

    def set_nombre(self, nombre):
        self.__nombre  =nombre

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def set_saldo(self,saldo):
        self.__saldo = saldo

    def set_correo(self, correo):
        self.__correo = correo

    def set_nuemro_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    def set_provincia(self,prov):
        self.__provincia = prov

    def set_ciudad(self,ciudad):
        self.__ciudad = ciudad

