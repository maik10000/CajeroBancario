import tkinter as tk
import tkinter.font as tk_font
import tkinter.ttk as ttk
from estilos.colores import color_sistema
color = color_sistema()


class VentanaMovimientos(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.componentes()

    def componentes(self):
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        x = (ancho_pantalla // 2) - (1000 // 2)
        y = (altura_pantalla // 2) - (700 // 2)
        self.geometry(f'{1000}x{700}+{x}+{y}')
        self.title("Retiro")

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
        label = tk.Label(self, text='Movimientos',
                         font=self.font_style2, bg=color.BLANCO)
        label.place(x=400, y=52)

        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TButton', foreground=color.BLANCO, background=color.VERDE_3D,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 15))
        self.lista_movimientos = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.lista_movimientos.config(font=("Cascadia Code", 25))
        self.lista_movimientos.place(x=150, y=150, width=700, height=400)
        self.lista_movimientos.insert(
            0, *('a', 'b', 'c', 'b', 'c', 'b', 'c', 'b', 'c', 'b', 'c', 'b', 'c', 'b', 'c'))


#v = VentanaMovimientos()
#v.mainloop()
