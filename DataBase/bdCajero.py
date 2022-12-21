import MySQLdb

conexion = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    database = "bdcajerobanco")


puntero  = conexion.cursor()
sql = """INSERT INTO provicia (ID_Prov,PROVINCIA) VALUES(%s,%s)"""

conexion.commit()
conexion.close()


