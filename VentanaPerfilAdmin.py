import tkinter as tk
from VentnanaRegistro import VentanaRegistro
import tkinter.font as tk_font
import tkinter.ttk as ttk
from estilos.colores import color_sistema
import VentanaInicio as venI
import random
from util.Cajero import Cajero
from DataBase.bdCajero import DBCajero

color = color_sistema()
MONTO_INICIAL = 10
list_head = ('NCuenta', 'Nombre', 'Cedula', 'Celular', 'Correo', 'Ciudad', 'Provincia', 'Saldo-Efectivo', 'Contraseña',
             'strike')


class VentanaPerfilAdmin(tk.Tk):
    ANCHO = 1270
    ALTO = 720

    def __init__(self, *args, info_user_a=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.info = info_user_a
        self.componentes()

    def componentes(self):
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        x = (ancho_pantalla // 2) - (self.__class__.ANCHO // 2)
        y = (altura_pantalla // 2) - (self.__class__.ALTO // 2)
        self.geometry(f'{self.__class__.ANCHO}x{self.__class__.ALTO}+{x}+{y}')
        self.title("Administrador")
        self.resizable(False, False)
        self.configure(bg=color.BLANCO)

        font_style3 = tk_font.Font(family="Cascadia Code", size=20, slant="italic", weight="bold")
        font_style2 = tk_font.Font(family="Cascadia Code", size=30, slant="italic")

        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TButton', foreground=color.BLANCO, background=color.VERDE_3D,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 16))
        ttk.Style().map('pad.TButton', background=[('pressed', color.VERDE_30), ('active', color.VERDE_3B)])

        label = tk.Label(self, text='Administrador', bg=color.BLANCO, font=font_style2)
        label.place(x=490, y=30)

        label = tk.Label(self, text='Admin: '+'self.info.get_nombre_a()', font=font_style3, bg=color.BLANCO,
                         foreground=color.GRIS_B6)
        label.place(x=50, y=100)

        btn_registrar = ttk.Button(self, text='Registrar', command=self.abrir_ventana_registro)
        btn_registrar.place(x=205, y=160)

        btn_eliminar = ttk.Button(self, text='Eliminar', command=self.eliminar_usuario)
        btn_eliminar.place(x=441, y=160)

        btn_buscar = ttk.Button(self, text='Buscar',command=self.buscar_usuario)
        btn_buscar.place(x=130, y=600)
        btn_int_b = ttk.Entry(self)
        btn_int_b.place(x=250,y=600,height=35,width=200)
        btn_editar = ttk.Button(self, text='Editar')
        btn_editar.place(x=913, y=160)

        db = DBCajero()
        db.abrir_conexion()
        self.res = db.get_lista_usuarios('CALL uList(%s)', 'maoaAdmin')
        db.cerrar_conexion()

        self.lista_usuarios()

        btn_salir = ttk.Button(self, text='Regresar', style='pad.TButton', command=self.regresar)
        btn_salir.place(x=944, y=655)

    def lista_usuarios(self):
        w = 1000
        h = 250
        frame = tk.Frame(self)
        frame.place(x=130, y=220, width=w, height=h)

        self.__lista_usuarios = ttk.Treeview(frame, columns=list_head)
        self.__lista_usuarios.heading('0', text='ID', anchor='center')

        for i in list_head:
            self.__lista_usuarios.heading(i, text=i, anchor='center')

        for i in self.res:
            self.__lista_usuarios.insert('', 'end', text=i[0],
                                         values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],i[10]))

        self.__lista_usuarios.place(x=0, y=0,height=h,width=w)

        scrollbar_x = ttk.Scrollbar(self.__lista_usuarios,orient='horizontal',command=self.__lista_usuarios.xview)
        self.__lista_usuarios.config(xscrollcommand=scrollbar_x.set)
        scrollbar_x.pack(side='bottom',fill='x')

        scrollbar_y = ttk.Scrollbar(self.__lista_usuarios, orient='vertical', command=self.__lista_usuarios.yview)
        self.__lista_usuarios.config(yscrollcommand=scrollbar_y.set)
        scrollbar_y.pack(side='right', fill='y')

    def actualizar(self):
        self.limpiar_lista()
        self.lista_usuarios()

    def limpiar_lista(self):
        self.__lista_usuarios.destroy()

    def mostrar_aviso_confirmacion(self):
        self.aviso = tk.Label(self, text="Usuario Registrado con exito!", foreground=color.VERDE_00, bg=color.VERDE_4C,
                              font=("Cascadia Code", 12))
        self.aviso.place(x=0, y=0, width=300, height=40)
        btn_cerrar = tk.Label(self.aviso, text="X", foreground=color.VERDE_00, bg=color.VERDE_4C,
                              font=("Cascadia Code", 10))
        btn_cerrar.place(x=280, y=-1, width=20, height=20)
        btn_cerrar.bind('<Button-1>', self.cerrar_ventana_aviso)

    def cerrar_ventana_aviso(self):
        self.aviso.destroy()

    def registrar_usuario(self, nombre, cedula, clave, correo, telefono, ciudad):
        cj = Cajero()

        cj.registrar_usuario(nombre, cedula, clave, MONTO_INICIAL, correo, telefono,
                             self.generar_cuenta(cedula, telefono), ciudad)
        self.mostrar_aviso_confirmacion()

    def generar_cuenta(self, cedula, telefono):
        cd = ""
        while (len(cd) < 13):
            x1 = int(cedula[2:6]) * int(cedula[8:9]) * 1523 * int(telefono[2:5])
            x2 = random.randint(0, 100)
            cd = "100" + str(x1) + str(x2)
        return cd

    def abrir_ventana_registro(self):
        if not VentanaRegistro.en_uso:
            self.ventana_registro = VentanaRegistro(callback=self.registrar_usuario,
                                                    callback2=self.actualizar)

    def regresar(self):
        self.destroy()
        ventana_inicio = venI.VentanaInicio()
        ventana_inicio.mainloop()

    def eliminar_usuario(self):
        s = self.__lista_usuarios.focus()
        s = self.__lista_usuarios.item(s)
        if s['text'] != '':
            d = s['text']
            db = DBCajero()
            db.abrir_conexion()
            db.eliminar_usuario(d)
            db.cerrar_conexion()
            self.actualizar()
            print('Usuario eliminado con exito')
        else:
            print('Seleccione un usuario primero!')

    def buscar_usuario(self,valor='Al'):
        s = self.res
        for u in s:
            if valor in u:
                s = u
                break
        else:
            print(f'No se enconrto "{valor}"')
        print(self.__lista_usuarios['values'])

    def destroy(self):
        return super().destroy()

# v = VentanaPerfilAdmin()
# v.mainloop()