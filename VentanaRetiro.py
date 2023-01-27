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
        self.title("Retiro")
        self.geometry("800x600")
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

        boton_aceptar = ttk.Button(self, text="Aceptar", command=self.retirar)
        boton_aceptar.place(x=130, y=403, width=150, height=40)
        boton_cancelar = ttk.Button(self, text="Cancelar")
        boton_cancelar.place(x=430, y=403, width=150, height=40)

    def retirar(self):
        res = Cajero().retirar_dinero(self.numero_cuenta, self.cantidad.get())
        print(res['estate'])

    def destroy(self):
        self.__class__.en_uso = False
        return super().destroy()
