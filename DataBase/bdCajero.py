import mysql.connector as MySQLdb

rutas_de_comandos_sql = {
    'usuario': {
        'insertar': "INSERT INTO usuario (NCuenta,Nombre_Apellido,cedula,telefono,saldo,correo,clave,index_ciudad) "
                    "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
        'buscar': "CALL vaSe(%s,%s)",
        'banear': 'CALL strk(%s)',
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
        'buscar': 'SELECT Nombre_Apellido, correo, ID_USUARIO FROM usuario WHERE NCuenta = %s'
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


class DBCajero:
    def __init__(self):
        self.__host = 'unitbycode.com'
        self.__pass = "Bp]EM1~o"
        self.__bd_usuario = 'u846314360_ConstruyetuSit'
        self.__port = 3306
        self.__db_nombre = 'u846314360_DBBancodillera'
        self.__conexion = None

    def abrir_conexion(self):
        self.__conexion = MySQLdb.connect(host=self.__host, user=self.__bd_usuario, passwd=self.__pass,
                                          port=self.__port, database=self.__db_nombre)

    def insertar_datos(self, data):
        puntero = self.__conexion.cursor()
        comand_sql = rutas_de_comandos_sql[data['apunta']]['insertar']
        puntero.execute(comand_sql, data['valores'])
        self.__conexion.commit()

    def buscar_datos(self, data):
        puntero = self.__conexion.cursor()
        comand_sql = rutas_de_comandos_sql[data['apunta']]['buscar']
        puntero.execute(comand_sql, data['valores'])
        dat = puntero.fetchall()
        return dat

    def procesar_transaccion(self, data):
        puntero = self.__conexion.cursor()
        comand_sql = rutas_de_comandos_sql[data['apunta']]['procesar']
        puntero.execute(comand_sql, data['valores'])
        self.__conexion.commit()

    def cerrar_conexion(self):
        self.__conexion.close()

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

    def cargar_provincias(self):
        puntero = self.__conexion.cursor()
        comand_sql = 'SELECT * FROM provicia '
        puntero.execute(comand_sql)
        dat = puntero.fetchall()
        return dat

    def cargar_ciudades(self):
        puntero = self.__conexion.cursor()
        comand_sql = 'SELECT * FROM ciudad'
        puntero.execute(comand_sql)
        dat = puntero.fetchall()
        return dat

    def val_pass(self, clave, id):
        puntero = self.__conexion.cursor()
        puntero.execute(f'SELECT true  FROM usuario  WHERE cedula ={id}  AND clave = {clave}')
        res = puntero.fetchall()
        if len(res) == 0:
            return [False]
        else:
            return res

    def cambiar_pass(self, clave, id):
        puntero = self.__conexion.cursor()
        comand_sql = f'UPDATE usuario SET clave = {clave} WHERE usuario.cedula = {id}'
        puntero.execute(comand_sql)
        self.__conexion.commit()

    def eliminar_usuario(self, id):
            puntero = self.__conexion.cursor()
            comand_sql = f'DELETE FROM `usuario` WHERE `usuario`.`ID_USUARIO` = {id}'
            puntero.execute(comand_sql)
            self.__conexion.commit()

    #INSERT INTO `reg_mov` (`Id`, `total`, `id_bene`, `id_factor`, `lugar`, `cant_ant`, `can_pos`, `id_t`, `fecha`) VALUES ('15', '15', '15', lugar, '30', '15', '2', '1999-09-15');
    def generar_registro(self,data):
        puntero = self.__conexion.cursor()
        comand_sql = "INSERT INTO reg_mov (id_bene,id_factor, lugar, id_t,fecha,total) VALUES (%s,%s,%s,%s,%s,%s)"
        puntero.execute(comand_sql, data)
        self.__conexion.commit()


#data =('15',None,'bc','2','2023-03-18',300)
#c = DBCajero()
#c.abrir_conexion()
#c.generar_registro(data)
#c.cerrar_conexion()