
from colorama import  Fore, Style, init, Back
import os,time, random, colorama


def logo():
     print(Fore.LIGHTYELLOW_EX+"""
            ===========================================================================
                /////////////  //////////   ///        ////////  ////     ///
                     ///       ///          ///        //        /////    ///
                     ///       ///          ///        //        /// //   ///
                     ///       //////////   ///        ///////   ///  //  ///
                //   ///              ///   ///        //        ///   // ///
                ////////       //////////   /////////  ////////  ///    /////
            ============================================================================    
        """)


# Crear una lista con los símbolos a encontrar
simbolos = ['*', '/', '+', '-']

# Duplicar los símbolos para formar parejas
parejas = simbolos * 8
flag = "NO CAMBIAR"
rol_jugador = "JUGADOR"
# Barajar las parejas
random.shuffle(parejas) #El shuffle método toma una secuencia, como una lista, y reorganiza el orden de los elementos 

puntaje_jugador = puntaje_maquina = 0

# Crear un tablero vacío
tablero = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10', '11', '12', '13', '14', '15', '16']


# Función para mostrar el tablero
def print_tablero():
    global puntaje_jugador, puntaje_maquina 

    print(""" 
            | > PUNTAJE JUGADOR {}                  | > PUNTAJE MAQUINA {}

    """.format(puntaje_jugador, puntaje_maquina))

    print(Fore.LIGHTGREEN_EX+'________________________________')
    print('|'+tablero[0] + '\t|' + tablero[1] + '\t|' + tablero[2]+'\t|' + tablero[3]+'\t|')
    print('________________________________') 
    print('|'+tablero[4] + '\t|' + tablero[5] +'\t|' + tablero[6]+'\t|' + tablero[7]+'\t|')
    print('________________________________')
    print('|'+tablero[8] +'\t|' + tablero[9] +'\t|' + tablero[10]+'\t|' + tablero[11]+'\t|')
    print('________________________________') 
    print('|'+tablero[12] +'\t|' + tablero[13] +'\t|' + tablero[14]+'\t|' + tablero[15]+'\t|')
    print('________________________________') 
    


# Función para voltear una carta
indice = []
def voltear_carta1():
    global indice,tablero

    while True:
        os.system("cls")
        logo ()
        print(Fore.RESET+"""\t\t========================================================
        \t\t     BIENVENIDO AL JUEGO DE ENCONTRAR PARES     
        \t========================================================""")
        print_tablero()
        
        try:
            print(colorama.Fore.RESET+colorama.Back.RESET)
            cartaj = input('|| INSERTA TU PRIMER NUMERO: ')
           
            if(cartaj == " " or cartaj.isspace()):
                input(colorama.Fore.LIGHTWHITE_EX+colorama.Back.LIGHTRED_EX+"No debe estar vacio la entrada, presiona Enter...")
                print(colorama.Back.RESET+colorama.Fore.RESET)
            else:
                if(not cartaj.isdigit()):
                    input(colorama.Fore.LIGHTWHITE_EX+colorama.Back.LIGHTRED_EX+"La entrada debe ser numerica....")
                    print(colorama.Back.RESET+colorama.Fore.RESET)
                else:
                    if(tablero[int(cartaj)-1].isdigit()):
                        return cartaj
                    else:
                        input(colorama.Fore.LIGHTWHITE_EX+colorama.Back.LIGHTRED_EX+"La entrada esta ocupada...")
                        print(colorama.Back.RESET+colorama.Fore.RESET)
                
        except IndexError:
            input(colorama.Fore.LIGHTWHITE_EX+colorama.Back.LIGHTRED_EX+"Posicion incorrecta....")   
            print(colorama.Back.RESET+colorama.Fore.RESET) 
    
        break 


# Función para voltear una carta
def voltear_carta2():
    global indice, flag 

    while True:
        os.system("cls")
        logo ()
        print(Fore.RESET+"""\t\t========================================================
        \t\t     BIENVENIDO AL JUEGO DE ENCONTRAR PARES     
        \t========================================================""")
        print_tablero()
        
        try:
            print(colorama.Fore.RESET+colorama.Back.RESET)
            cartam = input('|| INSERTA TU SEGUNDO NUMERO (1-16): ')
            
            if(cartam == " " or cartam.isspace()):
                input(colorama.Fore.LIGHTWHITE_EX+colorama.Back.LIGHTRED_EX+"No debe estar vacio la entrada, presiona Enter...")
                print(colorama.Back.RESET+colorama.Fore.RESET)
            else:
                if(not cartam.isdigit()):
                    input(colorama.Fore.LIGHTWHITE_EX+colorama.Back.LIGHTRED_EX+"La entrada debe ser numerica....")
                    print(colorama.Back.RESET+colorama.Fore.RESET)
                else:
                    if(tablero[int(cartam)-1].isdigit()):
                        return cartam
                    else:
                        input(colorama.Fore.LIGHTWHITE_EX+colorama.Back.LIGHTRED_EX+"Posicion ocupada...")
                        print(colorama.Back.RESET+colorama.Fore.RESET)

        except IndexError:
            input(colorama.Fore.LIGHTWHITE_EX+colorama.Back.LIGHTRED_EX+"Posicion incorrecta....")
            print(colorama.Back.RESET+colorama.Fore.RESET)
        
        break 

def voltear_carta_maquina():
    #haremos que el primero numero eleguido sea libre....
    #el segundo que sea un simbolo parecido al del primero...
    global indice, parejas
    while(True):
        posicion_uno = random.randint(0, len(tablero)-1)
        if(tablero[posicion_uno].isdigit()):
            simbolo_identificado = parejas[posicion_uno]
           

            match(simbolo_identificado):
                case "+":
                    
                    while(True):
                        posicion_dos = random.randint(0, len(tablero)-1)
                        simbolo_identificado2 = parejas[posicion_dos]

                        if(tablero[posicion_dos].isdigit()):
                            if(simbolo_identificado2 == "+"):
                            
                                if(posicion_uno != posicion_dos):
                                    indice.extend([posicion_uno, posicion_dos])
                                    break
                            else:
                                posicion_dos = random.randint(0, len(tablero)-1)
                        else:
                            posicion_dos = random.randint(0, len(tablero)-1)
                
                case "*":
                    while(True):
                        posicion_dos = random.randint(0, len(tablero)-1)
                        simbolo_identificado2 = parejas[posicion_dos]

                        if(tablero[posicion_dos].isdigit()):
                            if(simbolo_identificado2 == "*"):
                            
                                if(posicion_uno != posicion_dos):
                                    indice.extend([posicion_uno, posicion_dos])
                                    break
                            else:
                                posicion_dos = random.randint(0, len(tablero)-1)
                        else:
                            posicion_dos = random.randint(0, len(tablero)-1)
                

                case _:
                    while(True):
                        posicion_dos = random.randint(0, len(tablero)-1)
                        
                        if(tablero[posicion_dos].isdigit()):
                        
                            if(posicion_uno != posicion_dos):
                                indice.extend([posicion_uno, posicion_dos])
                                break
                        else:
                            posicion_dos = random.randint(0, len(tablero)-1)
                
            break 
        else:
            posicion_uno = random.randint(0, len(tablero)-1)

# Función para comprobar si dos cartas son iguales
def son_iguales(posiciones):
    global puntaje_jugador, puntaje_maquina, flag, indice, rol_jugador
    
    if(parejas[posiciones[0]] != parejas[posiciones[1]]):
        #cuando nuestros valores no son iguales.
        for i in posiciones:
            tablero[i] = parejas[i]
        flag = "CAMBIAR"
    else:
        for i in posiciones:
            tablero[i] = parejas[i]

        indice = []
        if(rol_jugador == "JUGADOR"):
            puntaje_jugador += 1
        elif(rol_jugador == "MAQUINA"):
            puntaje_maquina += 1


def verificando_pares():
    contando_pares = 0
    contando_posicion = 0
    for i in tablero:
        if(not i.isdigit()):
            contando_pares += 1
        else:
            contando_posicion += 1

    if(contando_pares > contando_posicion):
        #solo quedan .... 
        x = []
        for i in range(len(tablero)):
            if(tablero[i].isdigit()):
                x.append(parejas[i])
            
        if(tuple(x).count('+') > 1 or tuple(x).count('-') > 1 or tuple(x).count('+') > 1 or tuple(x).count('/') > 1):
            return True 
        else:

            return False 
    else: 
        return True 

# Juego principal
while True:
    print(colorama.Back.RESET)
    os.system("cls")
    logo ()
    print(Fore.RESET+"""\t\t========================================================
    \t\t     BIENVENIDO AL JUEGO DE ENCONTRAR PARES     
    \t========================================================""")
    
    
    resultado = verificando_pares() #esta funcion verifica por si aun existe pares que se pueda adivinar...

    if(resultado):
        print_tablero()

        if(flag == "CAMBIAR"): #esta parte funciona tanto para jugador y maquina.
            tablero[indice[0]] = str(indice[0]+1)
            tablero[indice[1]] = str(indice[1]+1)
            flag = "NO CAMBIAR"    
            indice = []
            time.sleep(2)
        else:
            if(rol_jugador == "JUGADOR"):

                number1 = voltear_carta1()
                if(number1 != None):       
                    while(True):
                        numer2 = voltear_carta2()
                        if(numer2 != None):

                            if(int(number1) == int(numer2)):
                                input(colorama.Fore.LIGHTWHITE_EX+colorama.Back.LIGHTRED_EX+"Las posiciones no deben ser iguales..., presiona enter para intentarlo otra vez.")
                                print(colorama.Back.RESET+colorama.Fore.RESET)
                                break 
                            else:
                                indice.extend([int(number1)-1, int(numer2)-1])
                                son_iguales(indice)
                                time.sleep(1) 
                                rol_jugador = "MAQUINA"
                                break     

                            
            elif(rol_jugador == "MAQUINA"):
                print(colorama.Fore.LIGHTWHITE_EX+"\n TURNO DE LA MAQUINA...")
                time.sleep(3)
                voltear_carta_maquina()
                
                son_iguales(indice)
                rol_jugador = "JUGADOR"
                
    else:

        if(puntaje_jugador > puntaje_maquina):
            print(colorama.Fore.LIGHTYELLOW_EX+"\n|>> JUGADOR GANA...")
            rol_jugador = "MAQUINA"
        
        elif(puntaje_maquina > puntaje_jugador):
            print(colorama.Fore.LIGHTYELLOW_EX+"\n|>> MAQUINA GANA....")
            rol_jugador = "JUGADOR"
        
        elif(puntaje_jugador == puntaje_maquina):
            print(colorama.Fore.LIGHTYELLOW_EX+"\n|>> EMPATES!")
        
        else:
            jugador = ["JUGADOR", "MAQUINA"]
            p = random.randint(0, len(jugador)-1)
            rol_jugador = jugador[p]

        puntaje_jugador = puntaje_maquina = 0
        tablero = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10', '11', '12', '13', '14', '15', '16']
        input(colorama.Fore.LIGHTWHITE_EX+colorama.Back.LIGHTRED_EX+"No hay mas coincidencias, presiona enter para jugar otra vez...")
        