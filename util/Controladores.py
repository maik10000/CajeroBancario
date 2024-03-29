import util.Validaciones as Validaciones
from util.Cajero import Cajero

def controller_regsitro(nombre, cedula, celular, correo, clave1, clave2):

    if not Validaciones.validar_nombre(nombre):

        return [False, 'Error ingrese un nombre valido']

    if not Validaciones.validar_cedula(cedula):

        return [False, 'Error ingrese una cedula valida']

    if not Validaciones.validar_correo(correo):

        return [False, 'Error ingrese un correo valido']

    if not Validaciones.validar_celular(celular):

        return [False, 'Error ingrese un numero de celular valido']

    if not Validaciones.validar_clave(clave1):

        if clave1 == clave2:

            return [False, 'Error claves no son iguales']

        return [False, 'Error ingrese una clave valida']
    

    return [True, 'Regitro Exitoso']
