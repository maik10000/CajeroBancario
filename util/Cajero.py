from util.Usuario import Usuario
from DataBase.bdCajero import DBCajero
class Cajero:

    def __init__(self):
        self.__usuarios = None
        self.__bdC = DBCajero()

    def registrarUsuario(self, nombre,cedula,clave,saldo,correo,numeroTelefono,numeroCuenta,ciudad,provincia):
        self.__bdC.abrirConexion()
        self.__bdC.insertarDatos({'apunta': 'usuario', 'valores': (numeroCuenta,nombre,cedula,numeroTelefono,saldo,correo,clave,self.varificarCiudad(ciudad,provincia)[0][0])})
        nuevoUsuario =  Usuario(nombre,cedula,clave,saldo,correo,numeroTelefono,numeroCuenta,ciudad,provincia)
        self.__bdC.cerrarConexion()

    def varificarCiudad(self,ciudad,prov):
        if (len(self.__bdC.buscarDatos({'apunta': 'ciudad', 'valores': (ciudad,)})) == 0):
            respuesta = self.__bdC.buscarDatos({'apunta': 'provincia', 'valores': (prov,)})
            self.__bdC.insertarDatos({'apunta': 'ciudad', 'valores': (ciudad, respuesta[0][0])})

        return self.__bdC.buscarDatos({'apunta': 'ciudad', 'valores': (ciudad,)})


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

