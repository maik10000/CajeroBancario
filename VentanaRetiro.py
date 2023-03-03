import tkinter as tk
import tkinter.font as tk_font
import tkinter.ttk as ttk
from estilos.colores import color_sistema
from util.Cajero import Cajero

color = color_sistema()


class VentanaRetiro(tk.Toplevel):
    en_uso = False

    def __init__(self, *args, numero_cuenta="", **kwargs):
        super().__init__(*args, **kwargs)
        self.numero_cuenta = numero_cuenta
        self.cantidad = None
        self.componentes()

    def componentes(self):
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        x = (ancho_pantalla // 2) - (800 // 2)
        y = (altura_pantalla // 2) - (600 // 2)
        self.geometry(f'{800}x{600}+{x}+{y}')
        self.title("Retiro")
        self.resizable(False, False)
        self.configure(bg=color.BLANCO)
        self.__class__.en_uso = True
        self.font_style = tk_font.Font(family="Cascadia Code", size=25, slant="italic", weight="bold")
        self.font_style2 = tk_font.Font(family="Cascadia Code", size=30, slant="italic", weight="bold")

        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=20, y=20, width=30, height=30)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=69, y=69, width=30, height=30)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=64, y=35, width=20, height=20)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=35, y=64, width=20, height=20)
        label = tk.Label(self, bg=color.AZUL_57)
        label.place(x=683, y=52, width=75, height=500)
        label = tk.Label(self, text='Retiro', font=self.font_style2, bg=color.BLANCO)
        label.place(x=332, y=52)

        label = tk.Label(self, text="Monto a retirar:", font=self.font_style, bg=color.BLANCO)
        label.place(x=70, y=224)
        self.cantidad = ttk.Entry(self)
        self.cantidad.place(x=70, y=300, width=250, height=40)

        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TButton', foreground=color.BLANCO, background=color.VERDE_3D,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 15))
        ttk.Style().configure('pad2.TButton', foreground=color.BLANCO, background=color.AZUL_38,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 15))

        ttk.Style().map('pad.TButton', background=[('pressed', color.VERDE_30), ('active', color.VERDE_3B)])
        ttk.Style().map('pad2.TButton', background=[('pressed', color.VERDE_30), ('active', color.AZUL_57)])

        boton_aceptar = ttk.Button(self, text="Aceptar", command=self.retirar, style="pad.TButton")
        boton_aceptar.place(x=130, y=403, width=150, height=40)
        boton_cancelar = ttk.Button(self, text="Cancelar", style="pad2.TButton")
        boton_cancelar.place(x=430, y=403, width=150, height=40)

    def retirar(self):

        c = self.cantidad.get()
        if c != '':
            try:
                res = Cajero().retirar_dinero(self.numero_cuenta, float(c))
                self.mensaje(res['estate'],clor= color.VERDE_40)
            except ValueError:
                self.mensaje('Ingrese numeros!',clor=color.ROJO_1A)

        else:
            self.mensaje('Campo Vacio!',clor=color.ROJO_1A)

    def mensaje(self, m='',clor=''):
        font_style = tk_font.Font(family="Cascadia Code", size=12, slant="italic", weight="bold")
        label = tk.Label(self, text=m, bg=color.BLANCO, foreground=clor, font=font_style)
        label.place(x=325, y=305)

    def cancelar(self):
        self.destroy()

    def destroy(self):
        self.__class__.en_uso = False
        return super().destroy()


#v = VentanaRetiro(numero_cuenta='1001884333273034')
#v.mainloop()
