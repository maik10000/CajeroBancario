import tkinter as tk
import tkinter.font as tk_font
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from VentanaDepositoTransferencia import VentanaDepositoTransferencia
from VentanaAjustes import VentanaAjustes
import VentanaInicio as venI
from estilos.colores import color_sistema
color = color_sistema()


class VentanaPerfil(tk.Tk):

    def __init__(self, *args, info_user=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.info_usuario = info_user

        # font style
        self.fontStyle = tk_font.Font(family="Cascadia Code", size=25, slant="italic", weight="bold")
        self.fontStyle2 = tk_font.Font(family="Cascadia Code", size=30, slant="italic", weight="bold")
        self.fontStyle3 = tk_font.Font(family="Cascadia Code", size=20, slant="italic", weight="bold")
        self.componentes()

    def componentes(self):

        self.title("Bienvenido " + self.info_usuario.get_nombre())
        self.geometry("1270x720")
        self.resizable(False, False)
        self.configure(bg=color.BLANCO)

        # nombre_Perfil

        label_nombre = tk.Label(self, text=self.info_usuario.get_nombre(), font=self.fontStyle, bg=color.BLANCO,
                                foreground=color.NEGRO_39)
        label_nombre.place(x=60, y=50)

        label = tk.Label(self, text=self.info_usuario.get_numero_cuenta(), font=self.fontStyle3, bg=color.BLANCO,
                         foreground=color.GRIS_B6)
        label.place(x=75, y=100)

        label_price = tk.Label(self, text ="$"+str(self.info_usuario.get_saldo()), font=self.fontStyle2, bg=color.BLANCO,
                               foreground=color.VERDE_40)

        label_price.place(x=761, y=56, width=367, height=50)

        # Botones de perfil

        img = Image.open(r'iconos\coin-dollar.png')
        img = img.resize((50, 50))
        icono1 = ImageTk.PhotoImage(img)

        img = Image.open(r'iconos\download2.png')
        img = img.resize((50, 50))
        icono2 = ImageTk.PhotoImage(img)

        img = Image.open(r'iconos\cog.png')
        img = img.resize((50, 50))
        icono3 = ImageTk.PhotoImage(img)

        img = Image.open(r'iconos\loop.png')
        img = img.resize((50, 50))
        icono4 = ImageTk.PhotoImage(img)

        img = Image.open(r'iconos\file-text2.png')
        img = img.resize((50, 50))
        icono5 = ImageTk.PhotoImage(img)

        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TButton', background=color.AZUL_75, bordercolor=color.VERDE_3D)
        ttk.Style().configure('pad2.TButton', background=color.AMARILLO_33, bordercolor=color.BLANCO_EE)
        ttk.Style().configure('pad3.TButton', foreground=color.BLANCO, background=color.AMARILLO_3E, bordercolor=color.BLANCO_EE, font=("Cascadia Code", 16))
        ttk.Style().map('pad.TButton', background=[('pressed', color.VERDE_30), ('active', color.VERDE_3B)]   )
        ttk.Style().map('pad2.TButton', background=[('pressed', color.AMARILLO_21), ('active', color.AMARILLO_30)])
        ttk.Style().map('pad3.TButton', background=[('pressed', color.AMARILLO_2F), ('active', color.AMARILLO_39)])

        boton_deposito = ttk.Button(self,style="pad.TButton",image=icono1, command= self.depositar)
        boton_deposito.imagen = icono1
        boton_retiro = ttk.Button(self,style="pad.TButton",image= icono2, command= self.retirar)
        boton_retiro.image = icono2
        boton_ajustes = ttk.Button(self,style="pad2.TButton",image= icono3, command= self.ajustarUsuario)
        boton_ajustes.image = icono3
        boton_transferencia = ttk.Button(self,style="pad.TButton",image= icono4, command= self.transferir)
        boton_transferencia.image = icono4
        boton_movimientos = ttk.Button(self, style="pad.TButton", image= icono5, command= self.ver_movimientos)
        boton_movimientos.image = icono5

        botonSalir = ttk.Button(self,style="pad3.TButton", text="SALIR", command= self.salir)

        label = tk.Label(self,text= "Deposito",font= self.fontStyle3,bg=color.BLANCO, foreground=color.GRIS_4D).place(x= 239, y= 240)
        label = tk.Label(self,text= "Retiro",font= self.fontStyle3,bg=color.BLANCO, foreground=color.GRIS_4D).place(x= 239, y= 425)
        label = tk.Label(self,text= "Ajustes de Usuario",font= self.fontStyle3,bg=color.BLANCO, foreground=color.GRIS_4D).place(x= 239, y= 597)
        label = tk.Label(self,text= "Transferencias",font= self.fontStyle3,bg=color.BLANCO, foreground=color.GRIS_4D).place(x= 815, y= 240)
        label = tk.Label(self,text= "Mis Movimientos",font= self.fontStyle3,bg=color.BLANCO, foreground=color.GRIS_4D).place(x= 815, y= 425)

        boton_deposito.place(x=60, y=210, width=100, height=100)
        boton_retiro.place(x=60, y=400, width=100, height=100)
        boton_ajustes.place(x=60, y=575, width=100, height=100)
        boton_transferencia.place(x=635, y=210, width=100, height=100)
        boton_movimientos.place(x=635, y=400, width=100, height=100)
        botonSalir.place(x=956, y=620, width=172, height=45)

    def depositar(self):
        if not VentanaDepositoTransferencia.en_uso:
            VentanaDepositoTransferencia(num_cuenta=self.info_usuario.get_numero_cuenta(), mood='Depositar')

    def retirar(self):
        print("Retiro")

    def ajustarUsuario(self):
        if not VentanaAjustes.en_uso:
            VentanaAjustes(info_usuario=self.info_usuario)
        print("Configurar")


    def transferir(self):
        if not VentanaDepositoTransferencia.en_uso:
            VentanaDepositoTransferencia(num_cuenta=self.info_usuario.get_numero_cuenta(), mood='Transferencia')

    def ver_movimientos(self):
        print("lista Movimientos")



    def salir(self):
        self.destroy()
        ventana_inicio = venI.VentanaInicio()
        ventana_inicio.mainloop()




