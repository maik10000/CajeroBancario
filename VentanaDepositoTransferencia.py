import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tk_font
import time
from estilos.colores import color_sistema
from util.Cajero import Cajero

color = color_sistema()


class VentanaDepositoTransferencia(tk.Toplevel):
    en_uso = False

    def __init__(self, *args, num_cuenta="", mood="",ide='', actualizar=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.en_uso = True
        self.actualizar = actualizar
        self.num_cuenta = num_cuenta
        self.ide = ide
        self.mood = mood
        self.componentes()

    def componentes(self):
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        x = (ancho_pantalla // 2) - (800 // 2)
        y = (altura_pantalla // 2) - (600 // 2)
        self.geometry(f'{800}x{600}+{x}+{y}')
        self.title(self.mood)
        self.resizable(False, False)
        self.configure(bg=color.BLANCO)

        # stilos
        self.font_style = tk_font.Font(
            family="Cascadia Code", size=25, slant="italic", weight="bold")
        self.font_style2 = tk_font.Font(
            family="Cascadia Code", size=30, slant="italic", weight="bold")
        self.font_style3 = tk_font.Font(
            family="Cascadia Code", size=20, slant="italic", weight="bold")

        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=20, y=20, width=30, height=30)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=69, y=69, width=30, height=30)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=64, y=35, width=20, height=20)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=35, y=64, width=20, height=20)
        label = tk.Label(self, bg=color.AZUL_57)
        label.place(x=683, y=20, width=75, height=500)
        label = tk.Label(self, text=self.mood,
                         font=self.font_style2, bg=color.BLANCO)
        label.place(x=332, y=52)

        label = tk.Label(self, text="Numero de cuenta:",
                         font=self.font_style, bg=color.BLANCO)
        label.place(x=70, y=170)
        self.num_cuenta_beneficiario = ttk.Entry(self)
        self.num_cuenta_beneficiario.place(x=70, y=240, width=432, height=40)
        label = tk.Label(self, text="Ingrese el monto:",
                         font=self.font_style, bg=color.BLANCO)
        label.place(x=70, y=324)
        self.cantidad = ttk.Entry(self)
        self.cantidad.place(x=70, y=400, width=250, height=40)

        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TButton', foreground=color.BLANCO, background=color.VERDE_3D,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 15))
        ttk.Style().configure('pad2.TButton', foreground=color.BLANCO, background=color.AZUL_38,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 15))

        ttk.Style().map('pad.TButton', background=[
            ('pressed', color.VERDE_30), ('active', color.VERDE_3B)])
        ttk.Style().map('pad2.TButton', background=[
            ('pressed', color.VERDE_30), ('active', color.AZUL_57)])

        boton_aceptar = ttk.Button(
            self, text="Aceptar", command=self.aceptar_transa, style='pad.TButton')
        boton_aceptar.place(x=430, y=403, width=150, height=40)

        boton_cancelar = ttk.Button(
            self, text="Volver", command=self.destroy, style='pad2.TButton')
        boton_cancelar.place(x=430, y=480, width=150, height=40)

        fuente = ("Cascadia Code", 15)
        self.mensaje_1 = tk.Label(self, bg=color.BLANCO, font=fuente)

    def aceptar_transa(self):
        num_b = self.num_cuenta_beneficiario.get()
        cant = self.cantidad.get()

        if num_b.replace(' ', '') != '' and cant.replace(' ', '') != '':
            if not (num_b == self.num_cuenta and self.mood.lower() == 'transferencia'):
                r = self.validar_cantidad(self.mood, cant=cant)
                if r['state']:
                    if num_b == self.num_cuenta:
                        self.realizar_transaccion(confirm=True,fec=time.strftime("%Y-%m-%d"),mismo='1')
                    else:
                        res = Cajero().buscar_cuenta(num_b)
                        print(res)
                        if not Comprobante.en_uso and res['estado']:
                            self.ide = res['userInfo'][2]
                            cadena_oculta = "xxxxxxxxxx"
                            Comprobante(nombre_beneficiario=res['userInfo'][0],
                                        num_cuenta_beneficiario=num_b.replace(
                                            num_b[6:len(num_b)], cadena_oculta),
                                        monto_efectivo=r['val'],
                                        num_cuenta_usuario=self.num_cuenta.replace(self.num_cuenta[6:len(self.num_cuenta)],
                                                                                cadena_oculta),
                                        correo_beneficiario=res['userInfo'][1],
                                        callback=self.realizar_transaccion,
                                        callback2=self.desabilitar_ventan
                                        )
                            self.mostrar_mense("")
                        else:
                            self.mostrar_mense("No se a encontrado el usuario")
                else:
                        self.mostrar_mense(r['msj'])
 
            else:
                self.mostrar_mense(
                    'No se puede hacer transferencia a su misma cuenta')
        else:
            self.mostrar_mense("Llene todos los campos")

    def mostrar_mense(self, mjs, cl= color.ROJO_1A):
        self.mensaje_1['foreground'] = cl
        self.mensaje_1['text'] = mjs
        i = (self.winfo_width() // 2) - ((len(mjs) * 12) // 2)
        self.mensaje_1.place(x=i, y=540)

    def validar_cantidad(self, modd='', cant=''):

        if modd.lower() == 'depositar':
            try:
                c = int(cant)
                if c % 5 == 0:
                    if 10 < c < 500:
                        return {'state': True, 'msj': 'Valido', 'val': c}
                    else:
                        return {'state': False, 'msj': 'El monto tiene que ser de 10 hasta 500'}
                else:
                    return {'state': False, 'msj': 'Sistema solo puede procesar cantidades multiplos de 5'}

            except ValueError:
                return {'state': False, 'msj': 'Ingrese numeros enteros'}

        elif modd.lower() == 'transferencia':
            num = cant.split('.')
            s = len(num)
            if s == 2:
                if not len(num[1]) < 3:
                    return {'state': False, 'msj': 'No se puede procesar esa cantidad'}

            try:
                c = float(cant)
                if 10 < c < 15000:
                    return {'state': True, 'msj': 'Valido', 'val': c}
                else:
                    return {'state': False, 'msj': 'El monto tiene que ser de 5 hasta 1500'}
            except ValueError:
                return {'state': False, 'msj': 'Ingrese una cantidad numerica'}

        else:
            print('Algo salio mal')

    def realizar_transaccion(self, confirm=False, fec='',mismo=''):
        c = int(self.cantidad.get())

        if self.mood.lower() == 'depositar' and confirm:

            c_bene = self.num_cuenta_beneficiario.get()
            res = Cajero().depositar(c, c_bene)

            if mismo =='1':
                self.actualizar(c)

            Cajero().registrar_movimiento(id_b=self.ide,total=c,tip='2',fecha=fec)
            self.mostrar_mense(res['estate'],cl=color.VERDE_00)

        elif self.mood.lower() == 'transferencia' and confirm:
            res = Cajero().transferir(self.num_cuenta_beneficiario.get(), self.num_cuenta, c)
            if res['std']:
                self.actualizar(c)
            self.mostrar_mense(res['estate'])
        else:
            self.mostrar_mense('Upps! hubo un error')

        self.num_cuenta_beneficiario.delete('0', 'end')
        self.cantidad.delete('0', 'end')

    def destroy(self):
        self.__class__.en_uso = False
        return super().destroy()

    def desabilitar_ventan(self, stado):
        self.num_cuenta_beneficiario['state'] = stado
        self.cantidad['state'] = stado


class Comprobante(tk.Toplevel):
    en_uso = False

    def __init__(self, *args, nombre_beneficiario="", num_cuenta_usuario="", num_cuenta_beneficiario="",
                 correo_beneficiario="", monto_efectivo="", callback=None, callback2=None, titulo="", **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.en_uso = True
        self.boton_confirmar = None
        self.boton_confirmar = None
        self.nombre_beneficiario = nombre_beneficiario
        self.num_origen = num_cuenta_usuario
        self.callback = callback
        self.__callback2 = callback2
        self.titulo = titulo
        self.num_destino = num_cuenta_beneficiario
        self.correo_beneficiario = correo_beneficiario
        self.fecha = time.strftime("%Y-%m-%d")
        self.num_comprobante = ""
        self.monto_efectivo = monto_efectivo
        self.__callback2('disable')
        self.componentes()

    def componentes(self):
        self.title(self.titulo)
        self.geometry('500x800')
        self.resizable(False, False)
        self.configure(bg=color.BLANCO)

        # stilos
        self.font_style = tk_font.Font(
            family="Cascadia Code", size=20, slant="italic", weight="bold")
        self.font_style2 = tk_font.Font(
            family="Cascadia Code", size=30, slant="italic", weight="bold")
        self.font_style3 = tk_font.Font(
            family="Cascadia Code", size=15, slant="italic", weight="bold")

        label = tk.Label(self, bg=color.AZUL_57)
        label.place(x=75, y=10, width=360, height=3)
        label = tk.Label(self, bg=color.BLANCO, text="Bancordillera",
                         font=self.font_style2, foreground=color.VERDE_3B)
        label.place(x=111, y=24)
        label = tk.Label(self, bg=color.AMARILLO_3E)
        label.place(x=100, y=100, width=300, height=2)
        label = tk.Label(self, bg=color.BLANCO, text=self.titulo,
                         font=self.font_style, foreground=color.VERDE_00)
        label.place(x=190, y=102)
        label = tk.Label(self, bg=color.BLANCO_CC)
        label.place(x=65, y=150, width=370, height=2)

        label = tk.Label(self, bg=color.BLANCO, foreground=color.NEGRO_11,
                         text="De la cuenta:", font=self.font_style3)
        label.place(x=73, y=161)
        label = tk.Label(self, bg=color.BLANCO, foreground=color.NEGRO_11,
                         text="A la cuenta:", font=self.font_style3)
        label.place(x=73, y=226)
        label = tk.Label(self, bg=color.BLANCO, foreground=color.NEGRO_11,
                         text="Beneficiario:", font=self.font_style3)
        label.place(x=73, y=292)
        label = tk.Label(self, bg=color.BLANCO, foreground=color.NEGRO_11,
                         text="Email:", font=self.font_style3)
        label.place(x=73, y=357)

        label = tk.Label(self, bg=color.BLANCO, foreground=color.GRIS_4D,
                         text=self.num_origen, font=self.font_style3)
        label.place(x=250, y=161)
        label = tk.Label(self, bg=color.BLANCO, foreground=color.GRIS_4D,
                         text=self.num_destino, font=self.font_style3)
        label.place(x=250, y=226)
        label = tk.Label(self, bg=color.BLANCO, foreground=color.GRIS_4D, text=self.nombre_beneficiario,
                         font=self.font_style3)
        label.place(x=250, y=292)
        label = tk.Label(self, bg=color.BLANCO, foreground=color.GRIS_4D, text=self.correo_beneficiario,
                         font=self.font_style3)
        label.place(x=250, y=357)
        label = tk.Label(self, bg=color.BLANCO_CC)
        label.place(x=65, y=408, width=370, height=2)

        label = tk.Label(self, bg=color.BLANCO, foreground=color.NEGRO_11,
                         text="Fecha:", font=self.font_style3)
        label.place(x=73, y=442)
        label = tk.Label(self, bg=color.BLANCO, foreground=color.NEGRO_11,
                         text="N.Comprobante:", font=self.font_style3)
        label.place(x=73, y=495)

        label = tk.Label(self, bg=color.BLANCO, foreground=color.GRIS_4D,
                         text=self.fecha, font=self.font_style3)
        label.place(x=250, y=442)
        label = tk.Label(self, bg=color.BLANCO, foreground=color.GRIS_4D,
                         text="0002", font=self.font_style3)
        label.place(x=329, y=495)

        label = tk.Label(self, bg=color.BLANCO_CC)
        label.place(x=65, y=541, width=370, height=2)

        label = tk.Label(self, bg=color.BLANCO, foreground=color.NEGRO_11,
                         text="Monto:", font=self.font_style3)
        label.place(x=73, y=564)

        label = tk.Label(self,
                         bg=color.BLANCO, foreground=color.VERDE_00,
                         text="$" + str(self.monto_efectivo),
                         font=self.font_style3)
        label.place(x=329, y=564)

        self.boton_confirmar = ttk.Button(
            self, text="Confirmar", command=self.confirmar)
        self.boton_confirmar.place(x=163, y=640, width=174, height=40)

        self.boton_cancelar = ttk.Button(
            self, text="Cancelar", command=self.destroy)
        self.boton_cancelar.place(x=163, y=700, width=174, height=40)

    def confirmar(self):
        self.destroy()
        self.callback(True, self.fecha)

    def destroy(self):
        self.__class__.en_uso = False
        self.__callback2('normal')
        return super().destroy()

# v = VentanaDepositoTransferencia(num_cuenta='1001884333273034',mood='depositar')
# v.mainloop()
