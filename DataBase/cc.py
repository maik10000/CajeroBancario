import mysql.connector as MySQLdb

rutas_de_comandos_sql = {
    'usuario': {
        'insertar': "INSERT INTO usuario (NCuenta,Nombre_Apellido,cedula,telefono,saldo,correo,clave,index_ciudad) "
                    "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
        'buscar': "CALL vaSe(%s,%s)",
        'banear': 'CALL penalizar(%s)',
        'actualizar': "CALL acU(%s,%s,%s,%s,%s,%s)"
    },
    'ciudad': {
        'insertar': "INSERT INTO ciudad (CIUDAD,Idf_provincia) VALUES(%s,%s)",
        'buscar': "SELECT ID_Ciudad  FROM ciudad WHERE CIUDAD = %s"
    },

    'provincia': {
        'buscar': "SELECT ID_Prov FROM provicia WHERE PROVINCIA = %s"
    },

    'cuentas': {
        'buscar': 'SELECT Nombre_Apellido, correo FROM usuario WHERE NCuenta = %s'
    },

    'depositar': {
        'procesar': 'CALL deB(%s,%s)'
    },

    'transferencia': {
        'buscar': 'SELECT saldo FROM usuario WHERE NCuenta = %s',
        'procesar': 'CALL trb(%s,%s,%s)'
    },
    'retiro': {
        'procesar': 'CALL reB(%s,%s)'
    },
    'admins': {
        'buscar': 'CALL fad(%s,%s)'
    },
    'validar_usuario': {
        'buscar': 'CALL vu(%s)'

    }, 'validar_admin': {
        'buscar': 'CALL va(%s)'},

    'penalizados': {
        'buscar': 'SELECT strike FROM usuario WHERE NCuenta = %s'
    }
}


class DBCajero2:
    def __init__(self):
        __host = 'unitbycode.com'
        __pass = "Bp]EM1~o"
        __bd_usuario = 'u846314360_ConstruyetuSit'
        __port = 3306
        __db_nombre = 'u846314360_DBBancodillera'
        self.__conexion = MySQLdb.connect(host=__host, user=__bd_usuario, passwd=__pass,
                                          port=__port, database=__db_nombre)

    # def abrir_conexion(self):
    #   self.__conexion = MySQLdb.connect(host=self.__host, user=self.__bd_usuario, passwd=self.__pass,
    #                                    port=self.__port, database=self.__db_nombre)

    def buscar_datos(self):
        puntero = self.__conexion.cursor()
        comand_sql = 'SELECT * FROM provicia '
        puntero.execute(comand_sql)
        dat = puntero.fetchall()
        return dat
    def buscar_datos2(self):
        puntero = self.__conexion.cursor()
        comand_sql = 'SELECT * FROM ciudad '
        puntero.execute(comand_sql)
        dat = puntero.fetchall()
        return dat

    def cerrar_conexion(self):
        self.__conexion.close()


""" def insertar_datos(self, data):
     puntero = self.__conexion.cursor()
     comand_sql = rutas_de_comandos_sql[data['apunta']]['insertar']
     puntero.execute(comand_sql, data['valores'])
     self.__conexion.commit()


 def procesar_transaccion(self, data):
     puntero = self.__conexion.cursor()
     comand_sql = rutas_de_comandos_sql[data['apunta']]['procesar']
     puntero.execute(comand_sql, data['valores'])
     self.__conexion.commit()


 def get_lista_usuarios(self, comando, cuenta):
     puntero = self.__conexion.cursor()
     puntero.execute(comando, (cuenta,))
     return puntero.fetchall()


 def penalizar(self, data):
     puntero = self.__conexion.cursor()
     comand_sql = rutas_de_comandos_sql[data['apunta']]['banear']
     puntero.execute(comand_sql, data['valores'])
     self.__conexion.commit()


 def actualiza_usuario(self, data):
     puntero = self.__conexion.cursor()
     comand_sql = rutas_de_comandos_sql[data['apunta']]['actualizar']
     puntero.execute(comand_sql, data['valores'])
     self.__conexion.commit()
"""
cb = DBCajero2()
p = cb.buscar_datos()
ciu = cb.buscar_datos2()
cb.cerrar_conexion()

def provincias(p):
    prov = []
    for j in p:
        print(j)

def ciudades(index, c):
    ctis = []

    for i in c:
        if i[2] == index:
            print(i[1])


provincias(p)
ciudades(19,ciu)


