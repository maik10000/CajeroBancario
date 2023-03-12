import time
import threading
import cc

credencial = {'apunta': 'validar_usuario', 'valores': ('1727066332',)}


def f_1(data):

    ca = cc.DBCajero2()
    # ca.abrir_conexion()
    res = ca.buscar_datos(data)
    ca.cerrar_conexion()
    print('1r')
    print(res)

    ca = cc.DBCajero2()
    # ca.abrir_conexion()
    res = ca.buscar_datos(data)
    ca.cerrar_conexion()
    print('4r')
    print(res)


def f_2(data):

    ca = cc.DBCajero2()
    # ca.abrir_conexion()
    res = ca.buscar_datos(data)
    ca.cerrar_conexion()
    print('2')
    print(res)


def f_3(data):

    ca = cc.DBCajero2()
    # ca.abrir_conexion()
    res = ca.buscar_datos(data)
    ca.cerrar_conexion()
    print('3')
    print(res)


def f_4(data):

    ca = cc.DBCajero2()
    # ca.abrir_conexion()
    res = ca.buscar_datos(data)
    ca.cerrar_conexion()
    print('4')
    print(res)


def f_5(data):

    ca = cc.DBCajero2()
    # ca.abrir_conexion()
    res = ca.buscar_datos(data)
    ca.cerrar_conexion()
    print(res)


hilo = threading.Thread(target=lambda:f_1(credencial))
hilo1 = threading.Thread(target=lambda:f_2(credencial))
hilo2 = threading.Thread(target=lambda:f_3(credencial))
hilo3 = threading.Thread(target=lambda:f_4(credencial))

start_time = time.time()
hilo.start()
hilo1.start()
hilo2.start()
hilo3.start()

hilo.join()
hilo1.join()
hilo2.join()
hilo3.join()
end_time = time.time()
total_time = end_time - start_time
print("Tiempo total de ejecución: ", total_time)