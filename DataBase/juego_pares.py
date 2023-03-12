import os
import random
import sys
import time
from math import sqrt

import pwinput
from colorama import Fore

espacio = 2
sep_fila = Fore.CYAN+"+" + "-" * 8+Fore.RESET
separador_columna_0 = Fore.BLUE+"|" + " " * espacio+Fore.RESET


class JueguitoPares:

    def __init__(self):
        self.tabla = []
        self.mask_tabla = []
        self.jugadas = []

        self.puntuacion = 0
        self.jugadas_valida = True

    def iniciar_jueguito(self):
        size = 0
        while True:
            os.system('cls')
            print('\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t Bienvenido al jueguito de pares')
            time.sleep(1.5)
            os.system('cls')
            # print('\n\n\t\t\t\tIngrese un modo')
            # print(f'   {Fore.RED}  \t1.- Dificil\n\n  {Fore.YELLOW}   \t2.- Normal\n\n  {Fore.GREEN}   \t3.- Facil\n\n'+
            #       Fore.RESET)
            # op = input(Fore.CYAN+'\t     ->'+Fore.RESET)
            # if op == '1':
            #     size = 40
            # elif op == '2':
            #     size = 36
            # elif op == '3':
            #     size = 16
            #
            # else:
            #     print('Ingrese una opcion correcta')
            self.generar_tabla(16)
            self.empezar_partida(16)

    def empezar_partida(self, sizes):
        turno = True
        total_jugadas = 0
        p_maquina = 0
        try:
            t = self.mask_tabla
            while True:
                # print(total_jugadas)
                os.system('cls')
                print('             Puntuacion:' + f'Jugador:{self.puntuacion}  Maquina: {p_maquina}')
                print(self.dibujar_tabla(t))
                if self.jugadas_valida and len(self.jugadas) != 0:
                    time.sleep(1.3)
                    if not turno:
                        self.puntuacion += 1
                    else:
                        p_maquina += 1
                    os.system('cls')
                    print('             Puntuacion:' + f'Jugador:{self.puntuacion}  Maquina: {p_maquina}')
                    print(self.dibujar_tabla(t))
                elif not self.jugadas_valida and len(self.jugadas) != 0:
                    time.sleep(1.3)
                    os.system('cls')
                    print('             Puntuacion:' + f'Jugador:{self.puntuacion}  Maquina: {p_maquina}')
                    self.ocultar()
                    print(self.dibujar_tabla(t))

                if turno:
                    print(Fore.CYAN+'     <r para reiniciar>'+Fore.RESET)
                    u = input('     Seleccione dos casillas: \n     ->')
                    if u == 's':
                        return
                    u = u.split(' ')
                    if len(u) == 2:
                        try:
                            a = int(u[0])
                            b = int(u[1])
                            # print(sizes)
                            if 0 < a <= sizes and 0 < b <= sizes:
                                self.jugadas = []
                                # print(u)
                                g = self.val_datos([a, b])
                                # print(g)
                                if g['state']:
                                    # print('Pawsaa noma')
                                    self.revelar_item([a, b])
                                    turno = False
                                    total_jugadas += 1
                                else:
                                    print(Fore.RED +f'La posicion{g["dato"]} ya fue jugada'+ Fore.RESET)
                                    time.sleep(2)
                            else:
                                print(Fore.RED + 'Fuera de rango!' + Fore.RESET)
                                time.sleep(2)
                        except ValueError:
                            print(Fore.RED + 'Ingrese solo las posiciones!' + Fore.RESET)
                            time.sleep(2)
                    else:
                        print(Fore.RED + 'Ingrese dos posiciones!' + Fore.RESET)
                        time.sleep(2)
                else:

                        print('Turno de la maquina...')
                        time.sleep(2)
                        self.jugadas = []
                        r = self.jugar_bot(sizes)
                        # print(r)
                        g = self.val_datos(r)
                        # print(g)
                        if g['state']:
                            # print('pasaaa')
                            self.revelar_item(r)
                            turno = True
                            total_jugadas += 1
                        # else:
                            # print(f'La posicion {g["dato"]} ya fue seleccionada')
                        # os.system('pause')

                if self.puntuacion > 4:
                    print('\n\n     Juego terminado Ganador: Jugador 1')
                    pwinput.pwinput('\n\n Presione Enter para reiniciar',mask='')
                    return
                elif p_maquina > 4:
                    print('\n\n      Juego terminado Ganador: Maquina')
                    pwinput.pwinput('\n\n Presione Enter para reiniciar',mask='')
                    return
                elif p_maquina == 4 and self.puntuacion == 4:
                    print('\n\n      Juego terminado Ganador: Empate')
                    pwinput.pwinput('\n\n Presione Enter para reiniciar',mask='')
                    return
        except Exception:
            print(sys.exc_info())
            os.system('pause')


    def val_datos(self,s):
        for o in s:
            for j in self.tabla:
                # print(o)
                if o in j:
                    return {'dato': o,'state':False}
        else:
            return {'state': True}

    def ocultar(self):
        for o in self.jugadas:
            for i, j in zip(self.tabla,self.mask_tabla):
                if o in i:
                    dex = i.index(o)
                    c = i[dex]
                    i[dex] = j[dex]
                    j[dex] = c

    def jugar_bot(self, sz):
        while True:
            n = random.randint(1, sz)
            m = random.randint(1, sz)
            if n != m:
                if not n in self.jugadas and not m in self.jugadas:
                    break

        return [m, n]

    def revelar_item(self, x):
        a= []
        # print(self.jugadas)
        # print(x)
        # print(self.mask_tabla)
        # print(self.tabla)
        # os.system('pause')
        try:
            for o in x:
                for i, j in zip(self.mask_tabla, self.tabla):
                    if o in i:
                        dex = i.index(o)
                        c = i[dex]
                        i[dex] = j[dex]
                        j[dex] = c
                        a.append(i[dex])
                        self.jugadas.append(j[dex])
            # print(self.jugadas)
            # print(a)
            # print('holaa')
            # os.system('pause')
            self.jugadas_valida = a[0] == a[1]


        except Exception:
            print(sys.exc_info())
            os.system('pause')

    def generar_tabla(self, num):
        simbolos = ['/', '*', '+', '-']
        sq = int(sqrt(num))

        s1 = 0
        s2 = 0
        s3 = 0
        s4 = 0

        for i in range(sq):
            sib = []
            for j in range(sq):
                while True:
                    pos = simbolos[random.randint(0, 3)]
                    if pos == '/' and s1 <= 4:
                        sib.append(pos)
                        s1 +=1
                        break
                    elif pos == '+' and s2 <= 4:
                        sib.append(pos)
                        s2 +=1
                        break
                    elif pos == '*' and s3 <= 4:
                        sib.append(pos)
                        s3 += 1
                        break
                    elif pos == '-' and s4 <= 4:
                        sib.append(pos)
                        s4 += 1
                        break
            # print(sib)
            self.tabla.append(sib)

        # print(self.tabla)
        # os.system('pause')
        c = 0
        for i in range(sq):
            aux = []
            for j in range(sq):
                c += 1
                aux.append(c)
            self.mask_tabla.append(aux)

    def dibujar_tabla(self, tb):
        info = ""
        num = len(tb)
        for i in range(num):
            info += "     "+sep_fila * num + '+' + '\n' +"     "+separador_columna_0
            for j in range(num):
                es = 8 - (len(str(tb[i][j])) + espacio)
                info += str(tb[i][j]) + " " * es + separador_columna_0

            info += '\n'
        info +="     "+sep_fila * num + '+'
        return info


juego = JueguitoPares()
juego.iniciar_jueguito()
