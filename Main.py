import random
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from VentnanaRegistro import VentanaRegistro
from  VentanaPerfil import ventanaPerfil
from util.Controladores import cotrollerSesion
import util.Cajero as cajero
FONDO = "#fff"
class VentanaMain(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cj = cajero.Cajero()
        self.componentes()


    def componentes(self):
        #Ventanta
        self.title("BanCordillera")
        self.resizable(False, False)
        self.geometry("1270x720")
        self.configure(bg =FONDO)
        self.fontStyle1 = tkFont.Font(family="Cascadia Code",size=44,slant="italic",weight="bold")
        self.fontStyle2 = tkFont.Font(family="Cascadia Code",size=20,slant="italic")


        #Label titulo
        label = tk.Label(self,text="BanCordillera",font=self.fontStyle1,bg=FONDO)
        label.place(x= 60, y = 40)

        #Laberl decorativos
        label = tk.Label(self,bg="#0E4C57").place(x=60,y=125,width=75,height=500)
        label = tk.Label(self,bg="#017175").place(x=620,y=65,width=415,height=50)
        label = tk.Label(self,bg="#017175").place(x=1052,y=65,width=40,height=50)
        label = tk.Label(self,bg="#018A67").place(x=1103,y=65,width=30,height=50)
        label = tk.Label(self,bg="#018A67").place(x=1146,y=65,width=20,height=50)
        label = tk.Label(self,bg="#5E803D").place(x=1121,y=209,width=50,height=364)
        label = tk.Label(self,bg="#CCCA3E").place(x=961,y=632,width=114,height=35)
        label = tk.Label(self,bg="#CCCA3E").place(x=100,y=632,width=229,height=40)

        #formulario de inicio
        frame = tk.Frame(self,width=572,height=447,bg=FONDO)
        frame.place(x=361,y=199)


        #formulario de sesion
        label = tk.Label(frame,text="Numero de cuenta o cedula: ",font=self.fontStyle2,foreground="#444",bg=FONDO)
        label.place( x = 82, y =0)
        label = tk.Label(frame,text="Contraseña: ",font=self.fontStyle2,foreground="#444",bg=FONDO)
        label.place( x = 82, y =150)


        #estilos inputs
        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TEntry', padding='10 1 1 1',selectbackground = '#93DFB9',insertcolor="#5E803D",bordercolor='#ddd')
        ttk.Style().configure('pad.TButton', foreground="#fff",background="#5E803D",bordercolor='#ddd',font=("Cascadia Code",16))
        ttk.Style().map('pad.TEntry',lightcolor =[('focus', '#5E803D')])
        ttk.Style().map('pad.TButton',background =[('pressed', '#4B6730'),('active', '#5B7C3B')])

        #inputs
        self.inputUsuario = ttk.Entry(frame,font=("Cascadia Code",16),style='pad.TEntry')
        self.inputUsuario.place(x=82,y=60,width=432,height=45)
        self.inputPass = ttk.Entry(frame,show="☼",font=("Cascadia Code",16),foreground="#CCCA3E",style='pad.TEntry')
        self.inputPass.place(x=82,y=209,width=432,height=45)
        #botones
        self.botonIniciar = ttk.Button(frame,text="Iniciar",style="pad.TButton",command = self.iniciarSesion)
        self.botonIniciar.place(x=82,y=370,width=172,height=45)

        self.botonRegistrar = ttk.Button(frame,text="Registrarse",style="pad.TButton",command = self.abrirVentanaRegisrto)
        self.botonRegistrar.place(x=350,y=370,width=172,height=45)


    def iniciarSesion(self):

       res =  cotrollerSesion(cuenta = self.inputUsuario.get(),clave= self.inputPass.get(), callback= self.cj.buscarUsuario)
       if(res['estado']):
           self.destroy()
           veP = ventanaPerfil(infoUser=res['userInfo'])
           veP.mainloop()
       else:
           labelAviso = tk.Label(self, text=res['res'], foreground="red",bg= FONDO)
           labelAviso.place(x=570,y=500)

    def registrarUsuario(self,nombre,cedula,clave,correo,telefono,ciudad,provicia):
        print("Usuario Registrado con exito!")
        self.cj.registrarUsuario(nombre,cedula,clave,10,correo,telefono,self.generarCuenta(cedula,telefono),ciudad,provicia)
        self.mostrarAvisoBien()

    def generarCuenta(self, cedula, telefono):
        cd =""
        while(len(cd)<13):
            x1 = int(cedula[2:6])*int(cedula[8:9])*1523*int(telefono[2:5])
            x2 = random.randint(0,100)
            cd = "100"+ str(x1) + str(x2)
        return cd

    def mostrarAvisoBien(self):
        self.aviso = tk.Label(self, text="Usuario Registrado con exito!", foreground="#007D00", bg="#4CFD4C", font=("Cascadia Code", 12))
        btnCerar = tk.Label(self.aviso, text="X", foreground="#007D00", bg="#4CFD4C", font=("Cascadia Code", 10))
        btnCerar.place(x=280, y=-1, width=20, height=20)
        btnCerar.bind('<Button-1>', self.cerrarVentanaAviso)
        self.aviso.place(x=0, y=0, width=300, height=40)


    def cerrarVentanaAviso(self,evento):
        self.aviso.destroy()

    def desabilitarVentan(self,stado):
        self.inputPass['state'] = stado
        self.inputUsuario['state'] = stado
        self.botonIniciar['state'] = stado


    def abrirVentanaRegisrto(self):
        if not VentanaRegistro.en_uso:
            self.ventanaRegistro = VentanaRegistro(callback2=self.desabilitarVentan,callback = self.registrarUsuario,funete1 = self.fontStyle1,funete2= self.fontStyle2, FONDO = FONDO)


#MAIN
venPrincipal = VentanaMain()
venPrincipal.mainloop()