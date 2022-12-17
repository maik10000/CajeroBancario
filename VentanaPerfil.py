import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import util.Cajero as caje
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
        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TButton', background="#017175", bordercolor='#eee')
        ttk.Style().configure('pad2.TButton', background="#A68633", bordercolor='#eee')
        ttk.Style().configure('pad3.TButton', foreground="#fff", background="#CCCA3E", bordercolor='#eee', font=("Cascadia Code", 16))
        ttk.Style().map('pad.TButton', background=[('pressed', '#4B6730'), ('active', '#5B7C3B')])
        ttk.Style().map('pad2.TButton', background=[('pressed', '#5E4D21'), ('active', '#8B7230')])
        ttk.Style().map('pad3.TButton', background=[('pressed', '#8D8C2F'), ('active', '#BBB939')])

        botonRetiro = ttk.Button(self,style="pad.TButton")
        botonDeposito = ttk.Button(self,style="pad.TButton")
        botonAjustes = ttk.Button(self,style="pad2.TButton")
        botonServicios = ttk.Button(self,style="pad.TButton")
        botonMovimientos = ttk.Button(self,style="pad.TButton")
        botonSalir = ttk.Button(self,style="pad3.TButton", text="SALIR")

        label = tk.Label(self,text= "Deposito",font= self.fontStyle3,bg=FONDO, foreground="#4D4D4D").place(x= 239, y= 240)
        label = tk.Label(self,text= "Retiro",font= self.fontStyle3,bg=FONDO, foreground="#4D4D4D").place(x= 239, y= 425)
        label = tk.Label(self,text= "Ajustes de Usuario",font= self.fontStyle3,bg=FONDO, foreground="#4D4D4D").place(x= 239, y= 597)
        label = tk.Label(self,text= "Servicios Basicos",font= self.fontStyle3,bg=FONDO, foreground="#4D4D4D").place(x= 815, y= 240)
        label = tk.Label(self,text= "Mis Movimientos",font= self.fontStyle3,bg=FONDO, foreground="#4D4D4D").place(x= 815, y= 425)

        botonRetiro.place(x=60, y=210, width=100, height=100)
        botonDeposito.place(x=60, y=400, width=100, height=100)
        botonAjustes.place(x=60, y=575, width=100, height=100)
        botonServicios.place(x=635, y=210, width=100, height=100)
        botonMovimientos.place(x=635, y=400, width=100, height=100)
        botonSalir.place(x=956, y=620, width=172, height=45)

    def depositar(self):
        print("Deposito")
        pass

    def retirar(self):
        print("Deposito")
        pass

    def ajustarUsuario(self):
        pass

    def pagarServiciosb(self):
        pass

    def verMovimientos(self):
        pass

    def salir(self):
        pass


ca = caje.Cajero()
ca.registrarUsuario("Michael Ortega","1727066332","1234","10000","micha@hotmail.com","0987654321","1324654897465","Quito","Pichincha")
i = ca.buscarUsuario("1727066332")
venP = ventanaPerfil(infoUser= i['userInfo'])
venP.mainloop()