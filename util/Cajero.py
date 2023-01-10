from util.Usuario import Usuario
from DataBase.bdCajero import DBCajero
class Cajero:

    def __init__(self):
        self.__bd_del_cajero = DBCajero()

    def registrar_usuario(self, nombre,cedula,clave,saldo,correo,numero_celular,numero_cuenta,ciudad,provincia):
        self.__bd_del_cajero.abrirConexion()
        self.__bd_del_cajero.insertarDatos({'apunta': 'usuario', 'valores': (numero_cuenta, nombre, cedula, numero_celular, saldo, correo, clave, self.verificar_ciudad(ciudad, provincia)[0][0])})


        self.__bd_del_cajero.cerrarConexion()


    def verificar_ciudad(self,ciudad,prov):
        #verifica si la ciudad ya existe
        if (len(self.__bd_del_cajero.buscar_datos({'apunta': 'ciudad', 'valores': (ciudad,)})) == 0):
            #sino existe inserta la ciodad y la provincia en la que esta
            respuesta = self.__bd_del_cajero.buscar_datos({'apunta': 'provincia', 'valores': (prov,)})
            self.__bd_del_cajero.insertar_datos({'apunta': 'ciudad', 'valores': (ciudad, respuesta[0][0])})
        #retorna la ciudad
        return self.__bd_del_cajero.buscar_datos({'apunta': 'ciudad', 'valores': (ciudad,)})


    def cargar_usuario(self, cuenta, passwd):
        self.__bd_del_cajero.abrir_conexion()
        credenciales = {'apunta': 'usuario', 'valores': (cuenta, passwd)}
        res = self.__bd_del_cajero.buscar_datos(credenciales)
        #print(res[0])
        if (len(res)!=0):
            dataUser = Usuario(res[0][1], res[0][2], res[0][4], res[0][5], res[0][3], res[0][0], res[0][6], res[0][7])
            data = {'estado': True, 'userInfo': dataUser, 'res': "Si hay"}
        else:
            data = {'estado': False, 'res': "Usuario o contraseña incorrecta"}
        self.__bd_del_cajero.cerrar_conexion()
        return  data

    def buscar_cuenta(self,numero_cuenta):
        self.__bd_del_cajero.abrir_conexion()
        credencial = {'apunta':'cuentas','valores':(numero_cuenta,)}
        res = self.__bd_del_cajero.buscar_datos(credencial)
        if((len(res)!=0)):
            data = {'estado':True,'userInfo':res[0],'res':'si hay'}
        else:
            data = {'estado': False, 'res': "Esa cuenta no existe"}
        self.__bd_del_cajero.cerrar_conexion()
        return  data

    def modo(self, modo = ""):
        if modo.lower() == 'depositar':
            return self.depositar
        else:
            return self.transferir

    def depositar(self):
        print('deposito')

    def transferir(self):
        print('transfirio')


