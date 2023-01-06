import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tk_font
import time
from estilos.colores import color_sistema
from util.Cajero import Cajero
color = color_sistema()


class VentanaDeposito(tk.Toplevel):
    en_uso = False
    def __init__(self, *args,num_cuenta = "", **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.en_uso = True
        self.nume_cuenta = num_cuenta
        self.componentes()

    def componentes(self):
        self.title("Deposito")
        self.geometry('800x600')
        self.resizable(False,False)
        self.configure(bg= color.BLANCO)

        #stilos
        self.font_style = tk_font.Font(family="Cascadia Code", size=25, slant="italic", weight="bold")
        self.font_style2 = tk_font.Font(family="Cascadia Code", size=30, slant="italic", weight="bold")
        self.font_style3 = tk_font.Font(family="Cascadia Code", size=20, slant="italic", weight="bold")

        label = tk.Label(self, bg= color.VERDE_3B).place(x=20,y= 20, width=30, height=30)
        label = tk.Label(self, bg= color.VERDE_3B).place(x=69,y= 69, width=30, height=30)
        label = tk.Label(self, bg= color.VERDE_3B).place(x=64,y= 35, width=20, height=20)
        label = tk.Label(self, bg= color.VERDE_3B).place(x=35,y= 64, width=20, height=20)
        label = tk.Label(self, bg= color.AZUL_57).place(x=683,y= 52, width=75, height=500)
        label = tk.Label(self, text="Deposito", font= self.font_style2, bg= color.BLANCO).place(x=332, y= 52)


        label = tk.Label(self, text="Numero de cuenta:", font= self.font_style, bg=color.BLANCO).place(x=70, y=170)
        self.num_cuenta_beneficiario = ttk.Entry(self)
        self.num_cuenta_beneficiario.place(x=70,y = 240, width= 432, height= 40)
        label = tk.Label(self, text="Monto a depositar:", font= self.font_style, bg=color.BLANCO).place(x=70, y=324)
        self.cantidad  =ttk.Entry(self)
        self.cantidad.place(x=70,y=400,width=250, height=40)

        boton_aceptar = ttk.Button(self,text="Aceptar",command=self.aceptarTransaccion)
        boton_aceptar.place(x=430, y= 403,width=150,height=40)
        boton_cancelar = ttk.Button(self, text="Regresar")
        boton_cancelar.place(x=430, y=480, width=150, height=40)

    def aceptarTransaccion(self):
        num_b = self.num_cuenta_beneficiario.get()
        cant = self.cantidad.get()
        cj = Cajero()
        res = cj.buscar_cuenta(num_b)
        if num_b !='' and cant != '':
            if not Comprobante.en_uso and res['estado']:
                cadena_oculta = "xxxxxxxxxx"
                Comprobante(nombre_beneficiario=res['userInfo'][0],
                            num_cuenta_beneficiario=num_b.replace(num_b[6:len(num_b)], cadena_oculta),
                            monto_efectivo=cant,
                            num_cuenta_usuario=self.nume_cuenta.replace(self.nume_cuenta[6:len(self.nume_cuenta)],
                                                                        cadena_oculta),
                            correo_beneficiario=res['userInfo'][1]
                            )
            else:
                print("Error usuario no encontrado")
        else:
            print("LLene los campos")




class Comprobante(tk.Toplevel):
    en_uso = False
    def __init__(self, *args, nombre_beneficiario="", num_cuenta_usuario="", num_cuenta_beneficiario="", correo_beneficiario="", monto_efectivo="", **kwargs):
        super().__init__(*args,**kwargs)
        self.__class__.en_uso = True
        self.nombre_beneficiario = nombre_beneficiario
        self.num_origen= num_cuenta_usuario
        self.num_destino = num_cuenta_beneficiario
        self.correo_beneficiario = correo_beneficiario
        self.fecha = time.strftime("%Y-%m-%d")
        self.num_comprobante = ""
        self.monto_efectivo  = monto_efectivo
        self.componentes()

    def componentes(self):
        self.title("Deposito")
        self.geometry('500x800')
        self.resizable(False, False)
        self.configure(bg= color.BLANCO)

        # stilos
        self.font_style = tk_font.Font(family="Cascadia Code", size=20, slant="italic", weight="bold")
        self.font_style2 = tk_font.Font(family="Cascadia Code", size=30, slant="italic", weight="bold")
        self.font_style3 = tk_font.Font(family="Cascadia Code", size=15, slant="italic", weight="bold")

        label = tk.Label(self, bg=color.AZUL_57).place(x=75, y=10, width=360, height=3)
        label = tk.Label(self, bg=color.BLANCO, text="Bancordillera", font= self.font_style2, foreground=color.VERDE_3B).place(x=111, y=24)
        label = tk.Label(self,bg=color.AMARILLO_3E).place(x= 100, y = 100, width=300,height=2)
        label = tk.Label(self, bg= color.BLANCO,text="Depositar", font= self.font_style, foreground= color.VERDE_00).place(x=190, y=102)
        label = tk.Label(self, bg= color.BLANCO_CC).place(x=65, y=150,width=370, height=2)

        label = tk.Label(self,bg= color.BLANCO, foreground= color.NEGRO_11, text="De la cuenta:",font= self.font_style3).place(x=73,y=161)
        label = tk.Label(self,bg= color.BLANCO, foreground= color.NEGRO_11, text="A la cuenta:",font= self.font_style3).place(x=73,y=226)
        label = tk.Label(self,bg= color.BLANCO, foreground= color.NEGRO_11, text="Beneficiario:",font= self.font_style3).place(x=73,y=292)
        label = tk.Label(self,bg= color.BLANCO, foreground= color.NEGRO_11, text="Email:",font= self.font_style3).place(x=73,y=357)

        label = tk.Label(self,bg= color.BLANCO, foreground=color.GRIS_4D, text=self.num_origen,font= self.font_style3).place(x=250,y=161)
        label = tk.Label(self,bg= color.BLANCO, foreground=color.GRIS_4D, text=self.num_destino,font= self.font_style3).place(x=250,y=226)
        label = tk.Label(self,bg= color.BLANCO, foreground=color.GRIS_4D, text=self.nombre_beneficiario,font= self.font_style3).place(x=250,y=292)
        label = tk.Label(self,bg= color.BLANCO, foreground=color.GRIS_4D, text=self.correo_beneficiario,font= self.font_style3).place(x=250,y=357)
        label = tk.Label(self, bg= color.BLANCO_CC).place(x=65, y=408,width=370, height=2)

        label = tk.Label(self,bg= color.BLANCO, foreground= color.NEGRO_11, text="Fecha:",font= self.font_style3).place(x=73,y=442)
        label = tk.Label(self,bg= color.BLANCO, foreground= color.NEGRO_11, text="N. Comprobante:",font= self.font_style3).place(x=73,y=495)

        label = tk.Label(self,bg= color.BLANCO, foreground=color.GRIS_4D, text= self.fecha,font= self.font_style3).place(x=250,y=442)
        label = tk.Label(self,bg= color.BLANCO, foreground=color.GRIS_4D, text="0002",font= self.font_style3).place(x=329,y=495)

        label = tk.Label(self, bg= color.BLANCO_CC).place(x=65, y=541,width=370, height=2)

        label = tk.Label(self,bg= color.BLANCO, foreground= color.NEGRO_11, text="Monto:",font= self.font_style3).place(x=73,y=564)

        label = tk.Label(self,bg= color.BLANCO, foreground=color.VERDE_00, text="$"+ self.monto_efectivo,font= self.font_style3).place(x=329,y=564)

        boton_confirmar =  ttk.Button(self,text="Confirmar").place(x=163,y=640,width=174,height=40)
        boton_cancelar =  ttk.Button(self,text="Cancelar").place(x=163,y=700,width=174,height=40)
