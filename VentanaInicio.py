import random
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from VentnanaRegistro import VentanaRegistro
from VentanaPerfil import VentanaPerfil
from util.Controladores import controller_sesion
from estilos.colores import color_sistema
import util.Cajero as cajero
MONTO_INICIAL = 10
color = color_sistema()
class VentanaInicio(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ventana_registro = None
        self.cj = cajero.Cajero()
        self.componentes()


    def componentes(self):
        #Ventanta
        self.title("BanCordillera")
        self.resizable(False, False)
        self.geometry("1270x720")
        self.configure(bg = color.BLANCO)
        self.font_style1 = tkFont.Font(family="Cascadia Code", size=44, slant="italic", weight="bold")
        self.font_style2 = tkFont.Font(family="Cascadia Code", size=20, slant="italic")
        self.font_style3 = tkFont.Font(family="Cascadia Code", size=15, slant="italic")


        #Label titulo
        label = tk.Label(self, text="BanCordillera", font=self.font_style1, bg= color.BLANCO)
        label.place(x= 60, y = 40)

        #Laberl decorativos
        label = tk.Label(self,bg=color.AZUL_57).place(x=60,y=125,width=75,height=500)
        label = tk.Label(self,bg= color.AZUL_75).place(x=620,y=65,width=415,height=50)
        label = tk.Label(self,bg=color.AZUL_75).place(x=1052,y=65,width=40,height=50)
        label = tk.Label(self,bg=color.VERDE_67).place(x=1103,y=65,width=30,height=50)
        label = tk.Label(self,bg=color.VERDE_67).place(x=1146,y=65,width=20,height=50)
        label = tk.Label(self,bg=color.VERDE_3D).place(x=1121,y=209,width=50,height=364)
        label = tk.Label(self,bg=color.AMARILLO_3E).place(x=961,y=632,width=114,height=35)
        label = tk.Label(self,bg=color.AMARILLO_3E).place(x=100,y=632,width=229,height=40)

        #formulario de inicio
        frame = tk.Frame(self,width=572,height=447,bg=color.BLANCO)
        frame.place(x=361,y=199)


        #formulario de sesion
        label = tk.Label(frame, text="Numero de cuenta o cedula: ", font=self.font_style2, foreground=color.NEGRO_44, bg= color.BLANCO)
        label.place( x = 82, y =0)
        label = tk.Label(frame, text="Contraseña: ", font=self.font_style2, foreground=color.NEGRO_44, bg= color.BLANCO)
        label.place( x = 82, y =150)


        #estilos inputs
        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TEntry', padding='10 1 1 1',selectbackground = color.CELESTE_B9,insertcolor= color.VERDE_3D,bordercolor= color.GRIS_DD)
        ttk.Style().configure('pad.TButton', foreground=color.BLANCO,background=color.VERDE_3D,bordercolor=color.GRIS_DD,font=("Cascadia Code",16))
        ttk.Style().map('pad.TEntry',lightcolor =[('focus', color.VERDE_3D)])
        ttk.Style().map('pad.TButton',background =[('pressed', color.VERDE_30),('active', color.VERDE_3B)])

        #inputs
        self.input_usuario = ttk.Entry(frame, font=("Cascadia Code", 16), style='pad.TEntry')
        self.input_usuario.place(x=82, y=60, width=432, height=45)
        self.input_pass = ttk.Entry(frame, show="*", font=("Cascadia Code", 16), foreground=color.AMARILLO_3E, style='pad.TEntry')
        self.input_pass.place(x=82, y=209, width=432, height=45)
        #botones
        self.boton_iniciar = ttk.Button(frame, text="Iniciar", style="pad.TButton", command = self.iniciar_sesion)
        self.boton_iniciar.place(x=82, y=370, width=172, height=45)

        self.boton_registrar = ttk.Button(frame, text="Registrarse", style="pad.TButton", command = self.abrir_ventana_registro)
        self.boton_registrar.place(x=350, y=370, width=172, height=45)


    def iniciar_sesion(self):
       res =  controller_sesion(cuenta = self.input_usuario.get(), clave= self.input_pass.get(), callback = self.cj.cargar_usuario)
       if(res['estado']):
           self.destroy()
           ve_p = VentanaPerfil(info_user=res['userInfo'])
           ve_p.mainloop()
       else:
           label_aviso = tk.Label(self, text=res['res'], foreground=color.ROJO_1A,bg= color.BLANCO,font= self.font_style3)
           label_aviso.place(x=550,y=500)

    def registrar_usuario(self, nombre, cedula, clave, correo, telefono, ciudad, provicia):
        print("Usuario Registrado con exito!")
        self.cj.registrar_usuario(nombre, cedula, clave, MONTO_INICIAL, correo, telefono, self.generar_cuenta(cedula, telefono), ciudad, provicia)
        self.mostrar_aviso_confirmacion()

    def generar_cuenta(self, cedula, telefono):
        cd =""
        while(len(cd)<13):
            x1 = int(cedula[2:6])*int(cedula[8:9])*1523*int(telefono[2:5])
            x2 = random.randint(0,100)
            cd = "100"+ str(x1) + str(x2)
        return cd

    def mostrar_aviso_confirmacion(self):
        self.aviso = tk.Label(self, text="Usuario Registrado con exito!", foreground=color.VERDE_00, bg= color.VERDE_4C, font=("Cascadia Code", 12))
        btn_cerrar = tk.Label(self.aviso, text="X", foreground=color.VERDE_00, bg=color.VERDE_4C, font=("Cascadia Code", 10))
        btn_cerrar.place(x=280, y=-1, width=20, height=20)
        btn_cerrar.bind('<Button-1>', self.cerrar_ventana_aviso)
        self.aviso.place(x=0, y=0, width=300, height=40)


    def cerrar_ventana_aviso(self, evento):
        self.aviso.destroy()

    def desabilitar_ventan(self, stado):
        self.input_pass['state'] = stado
        self.input_usuario['state'] = stado
        self.boton_iniciar['state'] = stado

    def abrir_ventana_registro(self):
        if not VentanaRegistro.en_uso:
            self.ventana_registro = VentanaRegistro(callback2=self.desabilitar_ventan,
                                                    callback=self.registrar_usuario,
                                                    funete1=self.font_style1,
                                                    funete2=self.font_style2)

