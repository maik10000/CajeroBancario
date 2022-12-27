from util.Usuario import Usuario
from DataBase.bdCajero import DBCajero
class Cajero:

    def __init__(self):
        self.__bdC = DBCajero()

    def registrarUsuario(self, nombre,cedula,clave,saldo,correo,numeroTelefono,numeroCuenta,ciudad,provincia):
        self.__bdC.abrirConexion()
        self.__bdC.insertarDatos({'apunta': 'usuario', 'valores': (numeroCuenta,nombre,cedula,numeroTelefono,saldo,correo,clave,self.varificarCiudad(ciudad,provincia)[0][0])})
        self.__bdC.cerrarConexion()


    def varificarCiudad(self,ciudad,prov):
        if (len(self.__bdC.buscarDatos({'apunta': 'ciudad', 'valores': (ciudad,)})) == 0):
            respuesta = self.__bdC.buscarDatos({'apunta': 'provincia', 'valores': (prov,)})
            self.__bdC.insertarDatos({'apunta': 'ciudad', 'valores': (ciudad, respuesta[0][0])})

        return self.__bdC.buscarDatos({'apunta': 'ciudad', 'valores': (ciudad,)})


    def buscarUsuario(self, cuenta, passwd):
        self.__bdC.abrirConexion()
        credenciales = {'apunta': 'usuario', 'valores': (cuenta, passwd)}
        res = self.__bdC.buscarDatos(credenciales)
        #print(res[0])
        if (len(res)!=0):
            dataUser = Usuario(res[0][1], res[0][2], res[0][4], res[0][5], res[0][3], res[0][0], res[0][6], res[0][7])
            data = {'estado': True, 'userInfo': dataUser, 'res': "Si hay"}
        else:
            data = {'estado': False, 'res': "Usuario o contraseña incorrecta"}
        self.__bdC.cerrarConexion()
        return  data


