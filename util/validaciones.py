import re

valCorreo = r"^[a-z][\w.-]+@\w[\w.-]+\.[\w.-]*[a-z][a-z]$"
valCelular = r'^09[0-9]{8}$'
valClave = r"^[0-9]{4}$"
valNombre = r"^[A-zÀ-ÿ\s]{1,40}$"
valCedula=r"^[0-9]{10}$"

def validarCorreo(text):
    val = re.search(valCorreo,text,re.I)
    if val != None:
        return True
    else:
        #print('el texto: '+ text +' ,no es un correo')
        return False


def validarCelular(text):
    val = re.search(valCelular,text,re.I)
    if val != None:
        #print('el texto: '+ text +' ,es un Numero valido')
        return True
    else:
        #print('el texto: '+ text +' ,no es un Numero valido')
        return False



def validarClave(text):
    val = re.search(valClave, text, re.I)
    if val != None:
        #print('el texto: ' + text + ' ,es una clave')
        return True
    else:
        #print('el texto: ' + text + ' ,no es una clave valida')
        return False



def validarNombre(text):
    val = re.search(valNombre, text, re.I)
    if val != None:
        #print('el texto: ' + text + ' ,es un nombre')
        return True
    else:
        #print('el texto: ' + text + ' ,no es un nombre valido')
        return False


def validarCedula(text):
    val= re.search(valCedula,text,re.I)
    if val != None:
        if(0<int(text[0:2])<25):
            #print('el texto: ' + text + ' ,es una cedula valida')
            return True
        else:
            #print('el texto: ' + text + ' ,no es una cedula valida')
            return False
    else:
        #print('el texto: ' + text + ' ,no es una cedula valida')
        return False


