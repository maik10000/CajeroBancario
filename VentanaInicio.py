import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from VentanaPerfil import VentanaPerfil
from VentanaPerfilAdmin import VentanaPerfilAdmin
from estilos.colores import color_sistema
import util.Cajero as cajero

color = color_sistema()


class VentanaInicio(tk.Tk):
    ANCHO = 1270
    ALTO = 720
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ventana_registro = None
        self.intentos = 3
        self.cj = cajero.Cajero()
        self.componentes()

    def componentes(self):
        # Ventanta
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        x = (ancho_pantalla // 2) - (self.__class__.ANCHO // 2)
        y = (altura_pantalla // 2) - (self.__class__.ALTO // 2)
        self.geometry(f'{self.__class__.ANCHO}x{self.__class__.ALTO}+{x}+{y}')
        self.title("BanCordillera")
        self.resizable(False, False)


        self.configure(bg=color.BLANCO)
        self.font_style1 = tkFont.Font(family="Cascadia Code", size=44, slant="italic", weight="bold")
        self.font_style2 = tkFont.Font(family="Cascadia Code", size=20, slant="italic")
        self.font_style3 = tkFont.Font(family="Cascadia Code", size=15, slant="italic")

        # Label titulo
        label = tk.Label(self, text="BanCordillera", font=self.font_style1, bg=color.BLANCO)
        label.place(x=60, y=40)

        # Laberl decorativos
        label = tk.Label(self, bg=color.AZUL_57)
        label.place(x=60, y=125, width=75, height=500)
        label = tk.Label(self, bg=color.AZUL_75)
        label.place(x=620, y=65, width=415, height=50)
        label = tk.Label(self, bg=color.AZUL_75)
        label.place(x=1052, y=65, width=40, height=50)
        label = tk.Label(self, bg=color.VERDE_67).place(x=1103, y=65, width=30, height=50)
        label = tk.Label(self, bg=color.VERDE_67).place(x=1146, y=65, width=20, height=50)
        label = tk.Label(self, bg=color.VERDE_3D).place(x=1121, y=209, width=50, height=364)
        label = tk.Label(self, bg=color.AMARILLO_3E).place(x=961, y=632, width=114, height=35)
        label = tk.Label(self, bg=color.AMARILLO_3E).place(x=100, y=632, width=229, height=40)

        # formulario de inicio
        frame = tk.Frame(self, width=572, height=447, bg=color.BLANCO)
        frame.place(x=361, y=199)

        # formulario de sesion
        label = tk.Label(frame, text="Numero de cuenta o cedula: ", font=self.font_style2, foreground=color.NEGRO_44,
                         bg=color.BLANCO)
        label.place(x=82, y=0)
        label = tk.Label(frame, text="Contraseña: ", font=self.font_style2, foreground=color.NEGRO_44, bg=color.BLANCO)
        label.place(x=82, y=150)

        # estilos inputs
        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TEntry', padding='10 1 1 1', selectbackground=color.CELESTE_B9,
                              insertcolor=color.VERDE_3D, bordercolor=color.GRIS_DD)
        ttk.Style().configure('pad.TButton', foreground=color.BLANCO, background=color.VERDE_3D,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 16))
        ttk.Style().map('pad.TEntry', lightcolor=[('focus', color.VERDE_3D)])
        ttk.Style().map('pad.TButton', background=[('pressed', color.VERDE_30), ('active', color.VERDE_3B)])

        # inputs
        self.input_usuario = ttk.Entry(frame, font=("Cascadia Code", 16), style='pad.TEntry')
        self.input_usuario.place(x=82, y=60, width=432, height=45)
        self.input_pass = ttk.Entry(frame, show="*", font=("Cascadia Code", 16), foreground=color.AMARILLO_3E,
                                    style='pad.TEntry')
        self.input_pass.place(x=82, y=209, width=432, height=45)
        # botones
        self.boton_iniciar = ttk.Button(frame, text="Iniciar", style="pad.TButton", command=self.iniciar_sesion)
        self.boton_iniciar.place(x=200, y=370, width=172, height=45)
        self.boton_iniciar.bind_all('<KeyPress>', self.eventos_teclado)
        self.label_aviso = tk.Label(self, foreground=color.ROJO_1A, bg=color.BLANCO,
                                    font=self.font_style3)

    def eventos_teclado(self, e):
        if e.char == '\r':
            self.iniciar_sesion()

    def iniciar_sesion(self):
        usuario = self.input_usuario.get().replace(' ', '')
        pwss = self.input_pass.get().replace(' ', '')

        if usuario != '' and pwss != '':
            val_c = self.cj.valida_cuentas(usuario)
            # print(val)
            if val_c['estado']:
                val = self.cj.usuario_bloqueado(usuario,val_c['rol'])
                # print(val)
                if val[0][1] != 1:
                    val = self.cj.cargar_usuario(usuario, pwss)
                    # print(val)
                    if val['estado'] and val_c['rol'] == 'user':
                        self.destroy()
                        ve_p = VentanaPerfil(info_user=val['userInfo'])
                        ve_p.mainloop()
                    elif val['estado'] and val_c['rol'] == 'admin':
                        self.destroy()
                        ven_a = VentanaPerfilAdmin(info_user_a=val['userInfo'])
                        ven_a.mainloop()
                    else:
                        self.aviso(res=val,rol=val_c['rol'])
                else:
                    self.intentos = 0
                    self.aviso()
            else:
                self.label_aviso['text'] = val_c['res']
                self.label_aviso.place(x=520, y=500)
        else:
            self.label_aviso['text'] = 'Llene los campos'
            self.label_aviso.place(x=520, y=500)

    def aviso(self, res=None,rol=''):
        #print(res)
        if self.intentos > 0:
            if rol == 'user':
                self.intentos -= 1
                self.label_aviso['text'] = res['res'] + ', le quedan ' + str(self.intentos)
                self.label_aviso.place(x=420, y=500)
            else:
                self.label_aviso['text'] = res['res']
                self.label_aviso.place(x=420, y=500)

        elif self.intentos == 0:
            self.label_aviso['text'] = 'Lo sentimos, cuenta bloqueda'
            self.label_aviso.place(x=460, y=500)
            self.input_usuario['state'] = 'disable'
            self.input_pass['state'] = 'disable'
            self.cj.bloquearUsuario(self.input_usuario.get())

