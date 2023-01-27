import tkinter as tk
import tkinter.font as tk_font
import tkinter.ttk as ttk
from estilos.colores import color_sistema
import VentanaInicio as ven_ini
color = color_sistema()

class VentanaLogAdmin(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font_style1 = tk_font.Font(family="Cascadia Code", size=44, slant="italic", weight="bold")
        self.font_style2 = tk_font.Font(family="Cascadia Code", size=20, slant="italic")
        self.font_style3 = tk_font.Font(family="Cascadia Code", size=15, slant="italic")
        self.componetes()


    def componetes(self):
        self.title("Adminstrador-Bancordillera")
        self.resizable(False, False)
        self.geometry("1270x720")
        self.title('Administrador')
        self.configure(bg=color.BLANCO)
        label = tk.Label(self, text="BanCordillera", font=self.font_style1, bg=color.BLANCO)
        label.place(x=60, y=40)

        label = tk.Label(self, bg=color.AZUL_57).place(x=60, y=125, width=75, height=500)
        label = tk.Label(self, bg=color.AZUL_75).place(x=620, y=65, width=415, height=50)
        label = tk.Label(self, bg=color.AZUL_75).place(x=1052, y=65, width=40, height=50)
        label = tk.Label(self, bg=color.VERDE_67).place(x=1103, y=65, width=30, height=50)
        label = tk.Label(self, bg=color.VERDE_67).place(x=1146, y=65, width=20, height=50)
        label = tk.Label(self, bg=color.VERDE_3D).place(x=1121, y=209, width=50, height=364)
        label = tk.Label(self, bg=color.AMARILLO_3E).place(x=961, y=632, width=114, height=35)
        label = tk.Label(self, bg=color.AMARILLO_3E).place(x=100, y=632, width=229, height=40)

        label = tk.Label(self, text='img_admin')
        label.place(x=600, y=150, width=100, height=100)

        label = tk.Label(self,text='Administrador',font= self.font_style2,bg=color.BLANCO)
        label.place(x=550,y=290)

        label = tk.Label(self, text="Usuario: ", font=self.font_style2, foreground=color.NEGRO_44,
                         bg=color.BLANCO)
        label.place(x=340, y=380)
        label = tk.Label(self, text="Contraseña: ", font=self.font_style2, foreground=color.NEGRO_44, bg=color.BLANCO)
        label.place(x=300, y=500)

        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TEntry', padding='10 1 1 1', selectbackground=color.CELESTE_B9,
                              insertcolor=color.VERDE_3D, bordercolor=color.GRIS_DD)
        ttk.Style().configure('pad.TButton', foreground=color.BLANCO, background=color.AZUL_75,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 16))
        ttk.Style().map('pad.TEntry', lightcolor=[('focus', color.VERDE_3D)])
        ttk.Style().map('pad.TButton', background=[('pressed', color.AZUL_38), ('active', color.AZUL_57)])

        # inputs
        self.input_usuario = ttk.Entry(self, font=("Cascadia Code", 16), style='pad.TEntry')
        self.input_usuario.place(x=510, y=380, width=370, height=40)
        self.input_pass = ttk.Entry(self, show="*", font=("Cascadia Code", 16), foreground=color.AMARILLO_3E,
                                    style='pad.TEntry')
        self.input_pass.place(x=510, y=500, width=370, height=40)
        # botones
        self.boton_iniciar = ttk.Button(self, text="Iniciar", style="pad.TButton", command=self.iniciar_sesion)
        self.boton_iniciar.place(x=471, y=587, width=172, height=45)

        boton_regresar = ttk.Button(self,text='Regresar',style="pad.TButton",command=self.regresar)
        boton_regresar.place(x=736, y=587, width=172, height=45)



    def regresar(self):
        self.destroy()
        ventana_inicio = ven_ini.VentanaInicio()
        ventana_inicio.mainloop()

    def destroy(self):
       return super().destroy()


    def iniciar_sesion(self):
        pass



VentanaLogAdmin().mainloop()