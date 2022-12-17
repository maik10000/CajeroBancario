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
        #nombre_Perfil

        label =  tk.Label(self,text =self.informacion.getNombre(), font= self.fontStyle,bg=FONDO,foreground="#393939").place(x=60,y=50)

        labelD = tk.Label(self,bg="#B0DBD0")
        labelD.place(x=761,y=56,width=367,height=50)
        labelPrice =  tk.Label(labelD,text ="$"+self.informacion.getSaldo(), font= self.fontStyle2,bg="#B0DBD0",foreground="#3BD540")

        labelPrice.place(x=60,y=-10)



ca = caje.Cajero()
ca.registrarUsuario("Michael Ortega","1727066332","1234","100000","micha@hotmail.com","0987654321","1324654897465","Quito","Pichincha")
i = ca.buscarUsuario("1727066332")
venP = ventanaPerfil(infoUser= i['userInfo'])
venP.mainloop()