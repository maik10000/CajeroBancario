class Usuario:

    def __init__(self, nombre,cedula,contra,saldo,correo,numeroTelefono,numeroCuenta,ciudad,provincia):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__contra = contra
        self.__saldo = saldo
        self.__correo = correo
        self.__numeroCuenta = numeroCuenta
        self.__nuemroTelefono = numeroTelefono
        self.__ciudad = ciudad
        self.__provincia = provincia

    def getNombre(self):
        return self.__nombre

    def getCedula(self):
        return self.__cedula

    def getContra(self):
        return self.__contra

    def getSaldo(self):
        return self.__saldo

    def getCorreo(self):
        return self.__correo

    def getNumeroCuenta(self):
        return self.__numeroCuenta

    def getNumeroTelefono(self):
        return self.__nuemroTelefono

    def getProvicia(self):
        return self.__provincia

    def getCiudad(self):
        return self.__ciudad


    def setNumeroTelefono(self,numeroTlefono):
        self.__nuemroTelefono = numeroTlefono

    def setNombre(self, nombre):
        self.__nombre  =nombre

    def setCedula(self, cedula):
        self.__cedula = cedula

    def setContra(self, contra):
        self.__contra = contra

    def setSaldo(self,saldo):
        self.__saldo = saldo

    def setCorreo(self, correo):
        self.__correo = correo

    def setNuemroCuenta(self, numeroCuenta):
        self.__numeroCuenta = numeroCuenta

    def setProvincia(self,prov):
        self.__provincia = prov

    def setCiudad(self,ciudad):
        self.__ciudad = ciudad

