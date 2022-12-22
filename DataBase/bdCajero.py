import MySQLdb

rutas = {
    'usuario': {'insertar':"INSERT INTO usuario (NCuenta,Nombre_Apellido,cedula,telefono,saldo,correo,clave,ciudad) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                'buscar':""
                },

    'ciudad': {'insertar':"INSERT INTO ciudad (CIUDAD,Idf_provincia) VALUES(%s,%s)",
               'buscar':"SELECT ID_Ciudad  FROM ciudad WHERE CIUDAD = %s"
               },
    'provincia':{'insertar':"",
                 'buscar':"SELECT ID_Prov FROM provicia WHERE PROVINCIA = %s"
                }
}
class DBCajero:
    def __init__(self):
        self.__host = 'localHost'
        self.__pass = ""
        self.__bdUsuario = 'root'
        self.__dbNombre = 'bdcajerobanco'
        self.__conexion = None

    def abrirConexion(self):
        self.__conexion = MySQLdb.connect(host=self.__host,user=self.__bdUsuario, passwd=self.__pass,database = self.__dbNombre)

    def insertarDatos(self,data):
        puntero = self.__conexion.cursor()
        comandSql = rutas[data['apunta']]['insertar']
        puntero.execute(comandSql, data['valores'])
        self.__conexion.commit()

    def buscarDatos(self, data):
        puntero = self.__conexion.cursor()
        comandSql = rutas[data['apunta']]['buscar']
        puntero.execute(comandSql,data['valores'])
        return puntero.fetchall()


    def cerrarConexion(self):
        self.__conexion.close()