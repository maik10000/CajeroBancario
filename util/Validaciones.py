import re

val_correo = r"^[a-z][\w.-]+@\w[\w.-]+\.[\w.-]*[a-z][a-z]$"
val_celular = r'^09[0-9]{8}$'
val_clave = r"^[0-9]{4}$"
val_nombre = r"^[A-zÀ-ÿ\s]{1,40}$"
val_cedula = r"^[0-9]{10}$"


def validar_correo(text):

    if re.search(val_correo, text, re.I) is not None:
        return True
    else:
        # print('el texto: '+ text +' ,no es un correo')
        return False


def validar_celular(text):

    if re.search(val_celular, text, re.I) is not None:
        # print('el texto: '+ text +' ,es un Numero valido')
        return True
    else:
        # print('el texto: '+ text +' ,no es un Numero valido')
        return False


def validar_clave(text):

    if re.search(val_clave, text, re.I) is not None:
        # print('el texto: ' + text + ' ,es una clave')
        return True
    else:
        # print('el texto: ' + text + ' ,no es una clave valida')
        return False


def validar_nombre(text):

    if re.search(val_nombre, text, re.I) is not None:
        # print('el texto: ' + text + ' ,es un nombre')
        return True
    else:
        # print('el texto: ' + text + ' ,no es un nombre valido')
        return False


def validar_cedula(text):

    if re.search(val_cedula, text, re.I) is not None:
        if 0 < int(text[0:2]) < 25:
            # print('el texto: ' + text + ' ,es una cedula valida')
            return True
        else:
            # print('el texto: ' + text + ' ,no es una cedula valida')
            return False
    else:
        # print('el texto: ' + text + ' ,no es una cedula valida')
        return False
