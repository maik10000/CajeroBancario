import MySQLdb

def abrirConexion():
    conexion = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bdcajerobanco")
    return conexion





