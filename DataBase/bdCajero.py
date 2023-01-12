import MySQLdb

rutas_de_comandos_sql = {
        'usuario': {'insertar':"INSERT INTO usuario (NCuenta,Nombre_Apellido,cedula,telefono,saldo,correo,clave,index_ciudad) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                    'buscar':"CALL filtradoUsuarioXCIoNC(%s,%s)"
                    },

        'ciudad': {'insertar':"INSERT INTO ciudad (CIUDAD,Idf_provincia) VALUES(%s,%s)",
                   'buscar':"SELECT ID_Ciudad  FROM ciudad WHERE CIUDAD = %s"
                   },

        'provincia':{'insertar':"",
                     'buscar':"SELECT ID_Prov FROM provicia WHERE PROVINCIA = %s"
                    },
        'cuentas':{
                    'buscar':'SELECT Nombre_Apellido, correo FROM usuario WHERE NCuenta = %s',
                    'actualizar': 'CALL acutalizacionSaldo(%s,%s)'
                }
}

class DBCajero:
    def __init__(self):
        self.__host = 'unitbycode.com'
        self.__pass = "Bp]EM1~o"
        self.__bd_usuario = 'u846314360_ConstruyetuSit'
        self.__port = 3306
        self.__db_nombre = 'u846314360_DBBancodillera'
        self.__conexion = None

    def abrir_conexion(self):
        self.__conexion = MySQLdb.connect(host = self.__host, user = self.__bd_usuario, passwd = self.__pass, port = self.__port, database = self.__db_nombre)

    def insertar_datos(self,data):
        puntero = self.__conexion.cursor()
        comand_sql = rutas_de_comandos_sql[data['apunta']]['insertar']
        puntero.execute(comand_sql, data['valores'])
        self.__conexion.commit()

    def buscar_datos(self, data):
        puntero = self.__conexion.cursor()
        comand_sql = rutas_de_comandos_sql[data['apunta']]['buscar']
        puntero.execute(comand_sql,data['valores'])
        return puntero.fetchall()

    def actualzar_datos(self, data):
        puntero = self.__conexion.cursor()
        comand_sql = rutas_de_comandos_sql[data['apunta']]['actualizar']
        puntero.execute(comand_sql,data['valores'])
        self.__conexion.commit()

    def cerrar_conexion(self):
        self.__conexion.close()
