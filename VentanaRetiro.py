import tkinter as tk
import tkinter.font as tk_font
import tkinter.ttk as ttk
from estilos.colores import color_sistema
from util.Cajero import Cajero
import time
color = color_sistema()


class VentanaRetiro(tk.Toplevel):
    en_uso = False

    def __init__(self, *args, numero_cuenta="",ide='', actualizar=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.numero_cuenta = numero_cuenta
        self.ide = ide 
        self.actualizar = actualizar
        self.componentes()

    def componentes(self):
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        x = (ancho_pantalla // 2) - (800 // 2)
        y = (altura_pantalla // 2) - (600 // 2)
        self.geometry(f'{1000}x{700}+{x}+{y}')
        self.title("Retiro")
        self.resizable(False, False)
        self.configure(bg=color.BLANCO)
        self.__class__.en_uso = True
        self.font_style = tk_font.Font(
            family="Cascadia Code", size=25, slant="italic", weight="bold")
        self.font_style2 = tk_font.Font(
            family="Cascadia Code", size=30, slant="italic", weight="bold")

        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=20, y=20, width=30, height=30)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=69, y=69, width=30, height=30)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=64, y=35, width=20, height=20)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=35, y=64, width=20, height=20)
        label = tk.Label(self, bg=color.AZUL_57)
        label.place(x=883, y=52, width=75, height=500)
        label = tk.Label(self, text='Retiro',
                         font=self.font_style2, bg=color.BLANCO)
        label.place(x=400, y=52)

        label = tk.Label(self, text="Otra cantidad:",
                         font=self.font_style, bg=color.BLANCO)
        label.place(x=230, y=470)

        ttk.Style().theme_use('clam')
        fuente = ("Cascadia Code", 15)

        ttk.Style().configure('pad.TEntry', padding='10 1 1 1', selectbackground=color.CELESTE_B9,
                              insertcolor=color.VERDE_3D, bordercolor=color.GRIS_DD)
        ttk.Style().configure('btn_ret.TButton', foreground=color.BLANCO, background=color.VERDE_3D,
                              bordercolor=color.GRIS_DD, font=fuente)
        ttk.Style().configure('btn_r2.TButton', foreground=color.BLANCO, background=color.AZUL_38,
                              bordercolor=color.GRIS_DD, font=fuente)

        ttk.Style().map('btn_ret.TButton', background=[
            ('pressed', color.VERDE_30), ('active', color.VERDE_00)])
        ttk.Style().map('btn_r2.TButton', background=[
            ('pressed', color.VERDE_30), ('active', color.AZUL_57)])
        self.cantidad = ttk.Entry(self, style='pad.TEntry', font=fuente)
        self.cantidad.place(x=550, y=480, width=150, height=40)

        self.mensaje_l = tk.Label(self, bg=color.BLANCO, font=fuente)

        conta = tk.Frame(self, bg=color.BLANCO)
        conta.place(x=230, y=150, width=500)
        btn_monto1 = ttk.Button(conta, text='$5', style='btn_ret.TButton',
                                command=lambda: self.retirar_cantidades(5))
        btn_monto1.grid(column=0, row=0, pady=10, padx=70)
        btn_monto2 = ttk.Button(conta, text='$10', style='btn_ret.TButton',
                                command=lambda: self.retirar_cantidades(10))
        btn_monto2.grid(column=1, row=0, pady=50)

        btn_monto3 = ttk.Button(conta, text='$20', style='btn_ret.TButton',
                                command=lambda: self.retirar_cantidades(20))
        btn_monto3.grid(column=0, row=1)
        btn_monto4 = ttk.Button(conta, text='$50', style='btn_ret.TButton',
                                command=lambda: self.retirar_cantidades(50))
        btn_monto4.grid(column=1, row=1)

        btn_monto5 = ttk.Button(conta, text='$100', style='btn_ret.TButton',
                                command=lambda: self.retirar_cantidades(100))
        btn_monto5.grid(column=0, row=2)
        btn_monto6 = ttk.Button(conta, text='$150', style='btn_ret.TButton',
                                command=lambda: self.retirar_cantidades(150))
        btn_monto6.grid(column=1, row=2, pady=50)

        boton_aceptar = ttk.Button(
            self, text="Aceptar", command=self.retirar, style='btn_ret.TButton')
        boton_aceptar.place(x=230, y=603, width=150, height=40)
        boton_cancelar = ttk.Button(
            self, text="Volver", style='btn_r2.TButton', command=self.cancelar)
        boton_cancelar.place(x=550, y=603, width=150, height=40)

    def retirar_cantidades(self, cant=0):

        res = Cajero().retirar_dinero(self.numero_cuenta, cant)

        if res['std']:
            Cajero().registrar_movimiento(id_b=self.ide,total=cant,tip='1',fecha=time.strftime("%Y-%m-%d"))
            self.mensaje(res['estate'], clor=color.VERDE_40)
            self.actualizar(cant)
        else:
            self.mensaje(res['estate'], clor=color.ROJO_1A)

    def retirar(self):
        c = self.cantidad.get()
        if c != '':
            try:
                c = int(c)
                if c % 5 == 0:
                    if 5 <= c <= 500:
                        res = Cajero().retirar_dinero(self.numero_cuenta, c)
                        if res['std']:
                            Cajero().registrar_movimiento(id_b=self.ide,total=c,tip='1',fecha=time.strftime("%Y-%m-%d"))
                            self.mensaje(res['estate'], clor=color.VERDE_40)
                            self.actualizar(c)
                            self.cantidad.delete('0', 'end')
                        else:
                            self.mensaje(res['estate'], clor=color.ROJO_1A)
                    else:
                        self.mensaje(
                            'El monto tiene que ser de 10 hasta 500', clor=color.AMARILLO_2F)
                else:
                    self.mensaje(
                        'Sistema solo puede procesar cantidades multiplos de 5', clor=color.AMARILLO_2F)

            except ValueError:
                self.mensaje('Ingrese numeros enteros', clor=color.ROJO_1A)

        else:
            self.mensaje('Campo Vacio!', clor=color.ROJO_1A)

    def mensaje(self, m='', clor=''):
        self.mensaje_l['foreground'] = clor
        self.mensaje_l['text'] = m
        i = (self.winfo_width() // 2) - ((len(m) * 12) // 2)
        self.mensaje_l.place(x=i, y=540)

    def cancelar(self):
        self.destroy()

    def destroy(self):
        self.__class__.en_uso = False
        return super().destroy()

# v = VentanaRetiro(numero_cuenta='1001884333273034')
# v.mainloop()
