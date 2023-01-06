import util.Validaciones as va

def controller_regsitro(nombre,cedula,celular,correo,clave1,clave2):

    if(not va.validar_nombre(nombre)):
        return [False,'Error ingrese un nombre valido']
    if (not va.validar_cedula(cedula)):
        return [False, 'Error ingrese una cedula valida']
    if (not va.validar_correo(correo)):
        return [False, 'Error ingrese un correo valido']
    if (not va.validar_celular(celular)):
        return [False, 'Error ingrese un numero de celular valido']
    if (not va.validar_clave(clave1)):
        if(clave1 == clave2):
            return [False,'Error claves no son iguales']
        return [False, 'Error ingrese una clave valida']
    return [True,'Regitro Exitoso']


def cotroller_sesion(cuenta = "", clave = "" ,callback = None):
    if(cuenta != ''and clave !='' and cuenta != ' ' and clave !=' '):
        res  = callback(cuenta, clave)
        return res
    else:
        return {'estado':False,'res':'Llene todos los campos'}

