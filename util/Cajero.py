from util.Usuario import Usuario
from util.Admin import Admin
from DataBase.bdCajero import DBCajero
class Cajero:

    def __init__(self):
        self.__bd_del_cajero = DBCajero()


    def registrar_usuario(self, nombre,cedula,clave,saldo,correo,numero_celular,numero_cuenta,ciudad,provincia):
        self.__bd_del_cajero.abrir_conexion()
        self.__bd_del_cajero.insertar_datos({'apunta': 'usuario', 'valores': (numero_cuenta, nombre, cedula, numero_celular, saldo, correo, clave, self.verificar_ciudad(ciudad, provincia)[0][0])})
        self.__bd_del_cajero.cerrar_conexion()


    def verificar_ciudad(self,ciudad,prov):
        self.__bd_del_cajero.abrir_conexion()
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
        self.__bd_del_cajero.cerrar_conexion()

        if len(res) != 0:
            dataUser = Usuario(res[0][1], res[0][2], res[0][4], res[0][5], res[0][3], res[0][0], res[0][6], res[0][7])
            data = {'estado': True, 'userInfo': dataUser}
            return data

        self.__bd_del_cajero.abrir_conexion()
        credenciales = {'apunta': 'admins', 'valores': (cuenta, passwd)}
        res = self.__bd_del_cajero.buscar_datos(credenciales)
        self.__bd_del_cajero.cerrar_conexion()
        print(res)
        if len(res) != 0:
            dataUset = Admin(res[0][0], res[0][1], res[0][2])
            data = {'estado': True, 'userInfo': dataUset}
            return data

        return {'estado':False,'res':'Contraseña Incorrecta!'}


    def valida_cuentas(self, cuenta):

        self.__bd_del_cajero.abrir_conexion()
        credenciales = {'apunta': 'validar_usuario', 'valores': (cuenta,)}
        res = self.__bd_del_cajero.buscar_datos(credenciales)
        self.__bd_del_cajero.cerrar_conexion()

        if len(res) == 0:
            self.__bd_del_cajero.abrir_conexion()
            credenciales = {'apunta': 'validar_admin', 'valores': (cuenta,)}
            res = self.__bd_del_cajero.buscar_datos(credenciales)
            self.__bd_del_cajero.cerrar_conexion()

            if len(res) == 0:
                return {'estado': False, 'res': "El usuario no existe"}
            else:
                return {'estado': True,'rol':'admin'}
        else:
            return {'estado': True,'rol':'user'}


    def buscar_cuenta(self,numero_cuenta):
        self.__bd_del_cajero.abrir_conexion()
        credencial = {'apunta':'cuentas','valores':(numero_cuenta,)}
        res = self.__bd_del_cajero.buscar_datos(credencial)
        if((len(res)!=0)):
            data = {'estado':True,'userInfo':res[0],'res':'si exite'}
        else:
            data = {'estado': False, 'res': "Esa cuenta no existe"}
        self.__bd_del_cajero.cerrar_conexion()
        return  data


    def depositar(self, monto, cuenta_beneficiaria):
        self.__bd_del_cajero.abrir_conexion()
        data = {'apunta': 'depositar', 'valores': (monto, cuenta_beneficiaria)}
        self.__bd_del_cajero.procesar_transaccion(data)
        self.__bd_del_cajero.cerrar_conexion()

    def transferir(self, cuenta_beneficieria, cuenta_benefactor, monto):
        self.__bd_del_cajero.abrir_conexion()
        data = {'apunta': 'transferencia', 'valores': (cuenta_benefactor,)}
        res = self.__bd_del_cajero.buscar_datos(data)
        if float(res[0][0]) > float(monto):
            data = {'apunta': 'transferencia', 'valores': (cuenta_beneficieria, cuenta_benefactor, monto)}
            self.__bd_del_cajero.procesar_transaccion(data)
            self.__bd_del_cajero.cerrar_conexion()
            return {'estate':'Transaccion exitosa'}

        self.__bd_del_cajero.cerrar_conexion()
        return {'estate': 'Saldo insuficiente'}

    def retirar_dinero(self, cuenta_benefactor, monto):
        self.__bd_del_cajero.abrir_conexion()
        data = {'apunta': 'transferencia', 'valores': (cuenta_benefactor,)}
        res = self.__bd_del_cajero.buscar_datos(data)

        if float(res[0][0]) > monto:
            data = {'apunta': 'retiro', 'valores': (cuenta_benefactor, monto)}
            self.__bd_del_cajero.procesar_transaccion(data)
            self.__bd_del_cajero.cerrar_conexion()
            return {'estate': 'Transaccion exitosa'}

        self.__bd_del_cajero.cerrar_conexion()
        return {'estate': 'Saldo insuficiente'}

    def bloquearUsuario(self,cuenta):
        self.__bd_del_cajero.abrir_conexion()
        data = {'apunta':'usuario','valores':(cuenta,)}
        self.__bd_del_cajero.penalizar(data)
        self.__bd_del_cajero.cerrar_conexion()

    def usuario_bloqueado(self,cuenta):
        self.__bd_del_cajero.abrir_conexion()
        data = {'apunta': 'validar_usuario', 'valores': (cuenta,)}
        res = self.__bd_del_cajero.buscar_datos(data)
        self.__bd_del_cajero.cerrar_conexion()
        if len(res) != 0:
            return res
        else:
            return [('False',1)]

    def editar_usuario(self):
        pass

