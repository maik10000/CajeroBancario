import util.Validaciones as va

def controllerRegsitro(nombre,cedula,celular,correo,clave):

    if(not va.validarNombre(nombre)):
        return [False,'Error ingrese un nombre valido']
    if (not va.validarCedula(cedula)):
        return [False, 'Error ingrese una cedula valida']
    if (not va.validarCorreo(correo)):
        return [False, 'Error ingrese un correo valido']
    if (not va.validarCelular(celular)):
        return [False, 'Error ingrese un numero de celular valido']
    if (not va.validarClave(clave)):
        return [False, 'Error ingrese una clave valida']
    return [True,'Regitro Exitoso']


def cotrollerSesion(cuenta = "", clave = "" ,callback = None):
    if(cuenta != ''and clave !='' and cuenta != ' ' and clave !=' '):
        res  = callback(cuenta, clave)
        return res
    else:
        return {'estado':False,'res':'Llene todos los campos'}

