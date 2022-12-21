from util.Usuario import Usuario
class Cajero:

    def __init__(self):
        self.__usuarios = []

    def registrarUsuario(self, nombre,cedula,clave,saldo,correo,numeroTelefono,numeroCuenta,ciudad,provincia):

        nuevoUsuario =  Usuario(nombre,cedula,clave,saldo,correo,numeroTelefono,numeroCuenta,ciudad,provincia)
        self.__usuarios.append(nuevoUsuario)


    def eliminarCuenta(self, index):
        self.__usuarios.pop(index)

    def buscarUsuario(self, cuenta):
        for i in self.__usuarios:
            if (i.getNumeroCuenta() == cuenta or i.getCedula() == cuenta):
                return {'estado': True, 'userInfo': i, 'res': "Si hay"}
        return {'estado': False, 'res': "Usuario o contraseñas incorrectas"}

    def getUsuarios(self):
        return self.__usuarios

    def getNumUsuarios(self):
        return len(self.__usuarios)


