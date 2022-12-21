import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from PIL import ImageTk,Image
import util.Cajero as caje
from VentanaDeposito import VentanaDeposito

FONDO = "#fff"
class ventanaPerfil(tk.Tk):

    def __init__(self, *args, infoUser = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.informacion = infoUser
        self.componentes()
    def componentes(self):
        self.title("Bienvenido "+self.informacion.getNombre())
        self.geometry("1270x720")
        self.resizable(False, False)
        self.configure(bg= FONDO)

        #font style
        self.fontStyle = tkFont.Font(family="Cascadia Code", size=25, slant="italic",weight="bold")
        self.fontStyle2 = tkFont.Font(family="Cascadia Code", size=30, slant="italic",weight="bold")
        self.fontStyle3 = tkFont.Font(family="Cascadia Code", size=20, slant="italic",weight="bold")
        #nombre_Perfil
        labelNombre = tk.Label(self,text =self.informacion.getNombre(), font= self.fontStyle,bg=FONDO,foreground="#393939").place(x=60,y=50)
        label = tk.Label(self,text= self.informacion.getNumeroCuenta(),font= self.fontStyle3,bg=FONDO, foreground="#B6B6B6").place(x= 75, y= 100)
        labelPrice =  tk.Label(self,text ="$"+self.informacion.getSaldo(), font= self.fontStyle2,bg=FONDO,foreground="#3BD540")
        labelPrice.place(x=761,y=56,width=367,height=50)

        #Botones de perfil
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
        ttk.Style().configure('pad.TButton', background="#017175", bordercolor='#eee')
        ttk.Style().configure('pad2.TButton', background="#A68633", bordercolor='#eee')
        ttk.Style().configure('pad3.TButton', foreground="#fff", background="#CCCA3E", bordercolor='#eee', font=("Cascadia Code", 16))
        ttk.Style().map('pad.TButton', background=[('pressed', '#4B6730'), ('active', '#5B7C3B')])
        ttk.Style().map('pad2.TButton', background=[('pressed', '#5E4D21'), ('active', '#8B7230')])
        ttk.Style().map('pad3.TButton', background=[('pressed', '#8D8C2F'), ('active', '#BBB939')])


        botonDeposito = ttk.Button(self,style="pad.TButton",image=icono1, command= self.depositar)
        botonDeposito.imagen = icono1
        botonRetiro = ttk.Button(self,style="pad.TButton",image= icono2, command= self.retirar)
        botonRetiro.image = icono2
        botonAjustes = ttk.Button(self,style="pad2.TButton",image= icono3, command= self.ajustarUsuario)
        botonAjustes.image  = icono3
        botonTransferencia= ttk.Button(self,style="pad.TButton",image= icono4, command= self.transferir)
        botonTransferencia.image = icono4
        botonMovimientos = ttk.Button(self,style="pad.TButton",image= icono5, command= self.verMovimientos)
        botonMovimientos.image = icono5

        botonSalir = ttk.Button(self,style="pad3.TButton", text="SALIR", command= self.salir)

        label = tk.Label(self,text= "Deposito",font= self.fontStyle3,bg=FONDO, foreground="#4D4D4D").place(x= 239, y= 240)
        label = tk.Label(self,text= "Retiro",font= self.fontStyle3,bg=FONDO, foreground="#4D4D4D").place(x= 239, y= 425)
        label = tk.Label(self,text= "Ajustes de Usuario",font= self.fontStyle3,bg=FONDO, foreground="#4D4D4D").place(x= 239, y= 597)
        label = tk.Label(self,text= "Transferencias",font= self.fontStyle3,bg=FONDO, foreground="#4D4D4D").place(x= 815, y= 240)
        label = tk.Label(self,text= "Mis Movimientos",font= self.fontStyle3,bg=FONDO, foreground="#4D4D4D").place(x= 815, y= 425)


        botonDeposito.place(x=60, y=210, width=100, height=100)
        botonRetiro.place(x=60, y=400, width=100, height=100)
        botonAjustes.place(x=60, y=575, width=100, height=100)
        botonTransferencia.place(x=635, y=210, width=100, height=100)
        botonMovimientos.place(x=635, y=400, width=100, height=100)
        botonSalir.place(x=956, y=620, width=172, height=45)

    def depositar(self):
        venDeposito = VentanaDeposito()
        print("Deposito")

    def retirar(self):
        print("Retiro")

    def ajustarUsuario(self):
        print("Configurar")

    def transferir(self):
        print("Trasnfirio")

    def verMovimientos(self):
        print("lista Movimientos")

    def salir(self):
        print("Cerro Sesion")
        self.destroy()


