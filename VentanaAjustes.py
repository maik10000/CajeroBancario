import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tk_font
from estilos.colores import color_sistema
from util.Validaciones import validar_clave
from util.Cajero import Cajero

color = color_sistema()


class VentanaAjustes(tk.Toplevel):
    en_uso = False

    def __init__(self, *args, info_usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.infoUser = info_usuario
        self.componentes()

    def componentes(self):
        self.__class__.en_uso = True
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        x = (ancho_pantalla // 2) - (1000 // 2)
        y = (altura_pantalla // 2) - (500 // 2)
        self.geometry(f'{1000}x{500}+{x}+{y}')
        self.title('Cambiar Contraseña')
        self.configure(bg=color.BLANCO)
        self.resizable(False, False)

        self.font_style2 = tk_font.Font(family="Cascadia Code", size=25, slant="italic", weight="bold")
        self.font_style3 = tk_font.Font(family="Cascadia Code", size=20, slant="italic", weight="bold")

        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TEntry',
                              padding='10 1 1 1',
                              selectbackground=color.CELESTE_B9,
                              insertcolor=color.VERDE_3D,
                              bordercolor=color.GRIS_DD)

        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=20, y=20, width=30, height=30)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=69, y=69, width=30, height=30)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=64, y=35, width=20, height=20)
        label = tk.Label(self, bg=color.VERDE_3B)
        label.place(x=35, y=64, width=20, height=20)
        label = tk.Label(self, bg=color.AZUL_57)
        label.place(x=850, y=52, width=75, height=400)

        self.label_nombre = tk.Label(self, text=self.infoUser.get_nombre(), font=self.font_style2, bg=color.BLANCO,
                                     fg=color.NEGRO)
        self.centrar_texto(self.infoUser.get_nombre(), self.label_nombre, 18, 50)
        # self.label_nombre.bind('<Enter>', lambda e, lb=self.label_nombre: self.cambiar_color(e, lb))
        # self.label_nombre.bind('<Leave>', lambda e, lb=self.label_nombre: self.cambiar_color(e, lb))
        # self.label_nombre.bind('<Button-1>',
        #                        lambda e, call=self.editar_nombre, c='nombre': self.abrir_ventana(e, call, c))

        label = tk.Label(self, font=self.font_style3, bg=color.BLANCO,
                         foreground=color.GRIS_B6)

        self.centrar_texto(self.infoUser.get_numero_cuenta(), label, 15, 100)

        # self.label_cedula = tk.Label(self, font=self.font_style3, bg=color.BLANCO, fg=color.NEGRO)
        # self.centrar_texto('self.infoUser.get_cedula()', self.label_cedula, 15, 150)
        # self.label_cedula.bind('<Enter>', lambda e, lb=self.label_cedula: self.cambiar_color(e, lb))
        # self.label_cedula.bind('<Leave>', lambda e, lb=self.label_cedula: self.cambiar_color(e, lb))
        # self.label_cedula.bind('<Button-1>',
        #                       lambda e, call=self.editar_cedula, c='cedula': self.abrir_ventana(e, call, c))

        # label = tk.Label(self, font=self.font_style3, bg=color.BLANCO, foreground=color.GRIS_B6)
        # self.centrar_texto("Correo:", label, 15, 250)

        # self.label_correo = tk.Label(self, font=self.font_style3, bg=color.BLANCO, fg=color.NEGRO)
        # self.centrar_texto('self.infoUser.get_correo()', self.label_correo, 15, 300)
        # self.label_correo.bind('<Enter>', lambda e, lb=self.label_correo: self.cambiar_color(e, lb))
        # self.label_correo.bind('<Leave>', lambda e, lb=self.label_correo: self.cambiar_color(e, lb))
        # self.label_correo.bind('<Button-1>',
        #                       lambda e, call=self.editar_correo, c='correo': self.abrir_ventana(e, call, c))

        # label = tk.Label(self, font=self.font_style3, bg=color.BLANCO, foreground=color.GRIS_B6)
        # self.centrar_texto("Provincia:", label, 15, 400)

        # self.combo_box_prov = ttk.Combobox(self, font=("Cascadia Code", 15), style='pad.TCombobox',
        #                                  state="readonly")
        # res = Cajero().prov_ciudades()
        # self.combo_box_prov.place(x=0, y=440, width=470, height=36)
        # self.combo_box_prov['values'] = res['provincia']
        # self.combo_box_prov.current(0)
        # self.combo_box_prov.bind("<<ComboboxSelected>>",
        #                         lambda e, ciudad=res['ciudad']: self.cambiar_ciudades(e, ciudad))
        # self.label_ciudad = tk.Label(self, font=self.font_style3, bg=color.BLANCO, fg=color.NEGRO)
        # self.centrar_texto('self.infoUser.get_ciudad()', self.label_ciudad, 15, 450)
        # self.label_ciudad.bind('<Enter>', lambda e, lb=self.label_ciudad: self.cambiar_color(e, lb))
        # self.label_ciudad.bind('<Leave>', lambda e, lb=self.label_ciudad: self.cambiar_color(e, lb))
        # self.label_ciudad.bind('<Button-1>',
        #                       lambda e, call=self.editar_ciudad, c='ciudad': self.abrir_ventana(e, call, c))

        # label = tk.Label(self, font=self.font_style3, bg=color.BLANCO, foreground=color.GRIS_B6)
        # self.centrar_texto('Ciudad:', label, 15, 550)

        # self.combo_box_cuidad = ttk.Combobox(self, font=("Cascadia Code", 15), style='pad.TCombobox',
        #                                     state="readonly")
        # self.combo_box_cuidad.place(x=300, y=625, width=400, height=36)
        # self.combo_box_cuidad['values'] = ['Seleccione una cuidad']
        # self.combo_box_cuidad.current(0)
        self.style_entry = tk_font.Font(family="Cascadia Code", size=15, slant="italic", weight="bold")
        self.label_pass = tk.Label(self, font=self.font_style3, bg=color.BLANCO, fg=color.NEGRO)
        self.centrar_texto("Contraseña Antigua", self.label_pass, 15, 150)
        self.input1 = ttk.Entry(self, font=self.style_entry,show='*')
        self.input1.place(x=350, y=200, width=350, height=35)
        # self.label_pass.bind('<Enter>', lambda e, lb=self.label_pass: self.cambiar_color(e, lb))
        # self.label_pass.bind('<Leave>', lambda e, lb=self.label_pass: self.cambiar_color(e, lb))
        # self.label_pass.bind('<Button-1>',
        #                       lambda e, call=self.editar_ciudad, c='clave': self.abrir_ventana(e, call, c))

        self.label_pass = tk.Label(self, font=self.font_style3, bg=color.BLANCO, fg=color.NEGRO)
        self.centrar_texto("Nueva Contraseña", self.label_pass, 15, 275)
        self.input2 = ttk.Entry(self, font=self.style_entry,show='*')
        self.input2.place(x=350, y=325, width=350, height=35)

        ttk.Style().configure('volver.TButton', foreground=color.BLANCO, background=color.AMARILLO_3E,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 12))
        ttk.Style().map('volver.TButton', background=[('pressed', color.VERDE_30), ('active', color.AMARILLO_39)])
        btn_guardar = ttk.Button(self, text='Guardar', command=self.cambia_pass, style='volver.TButton')
        btn_guardar.place(x=325, y=425, width=140, height=35)

        btn_cancelar = ttk.Button(self, text='Volver', command=self.destroy, style='volver.TButton')
        btn_cancelar.place(x=575, y=425, width=140, height=35)

        fuente = ("Cascadia Code", 15)
        self.mesaje = tk.Label(self, bg=color.BLANCO, font=fuente)

    # def cambiar_color(self, event, lb):
    #     if lb['foreground'] == color.CELESTE_B9:
    #         lb['foreground'] = color.NEGRO
    #     else:
    #         lb['foreground'] = color.CELESTE_B9

    def centrar_texto(self, texto, lb, size, y):
        lb['text'] = texto
        i = (1000 // 2) - ((len(texto) * size) // 2)
        lb.place(x=i, y=y)

    def cambia_pass(self):
        v = self.input2.get().replace(' ', '')
        v2 = self.input1.get().replace(' ', '')
        if v != '' and v2 != '':
            if validar_clave(v) and validar_clave(v2):
                res = Cajero().editar_pass(v, v2, self.infoUser.get_cedula())
                if res['state']:
                    self.mos_mensaje(res['msj'], color.VERDE_00)
                    self.input1.delete('0','end')
                    self.input2.delete("0","end")
                else:
                    self.mos_mensaje(res['msj'], color.ROJO_1A)
            else:
                self.mos_mensaje('La contraseña solo debe ser de 4 digitos', color.ROJO_1A)
        else:
            self.mos_mensaje('Campos vacíos', color.ROJO_1A)

    def mos_mensaje(self, text, color):
        self.mesaje['foreground'] = color
        self.mesaje['text'] = text
        i = (self.winfo_width() // 2) - ((len(text) * 12) // 2)
        self.mesaje.place(x=i, y=375)

    # def cambiar_ciudades(self, event, ciudades):
    #     s = self.combo_box_prov.current()
    #     ciu = []
    #     self.index_cidades = []
    #     if s != 0:
    #         for j in ciudades:
    #             if j[2] == s:
    #                 ciu.append(j[1])
    #                 self.index_cidades.append(j[0])

    #         self.combo_box_cuidad['values'] = ciu
    #         self.combo_box_cuidad.current(0)
    #         self.flag_prov = True
    #     else:
    #         self.combo_box_cuidad['values'] = ['Seleccione una cuidad']
    #         self.combo_box_cuidad.current(0)
    #         self.flag_prov = False
    #
    # @staticmethod
    # def editar_nombre(value):
    #     print('desde nombre')
    #     print(value)
    #
    # @staticmethod
    # def editar_cedula(value):
    #     print('desde cedula')
    #     print(value)
    #
    # @staticmethod
    # def editar_ciudad(value):
    #     print(value)
    #     print('desde ciudad')
    #
    # @staticmethod
    # def editar_correo(value):
    #     print('desde correo')
    #     print(value)
    #
    # @staticmethod
    # def editar_provincia(value):
    #     print('desde provincia')
    #     print(value)
    #
    # @staticmethod
    # def abrir_ventana(e, call, camp):
    #     if not VentanaEmergente.en_uso:
    #         VentanaEmergente(callback=call, comp=camp)

    def destroy(self):
        self.__class__.en_uso = False
        return super().destroy()


# class VentanaEmergente(tk.Toplevel):
#     en_uso = False
#     val = {
#         'nombre': validar_nombre,
#         'cedula': validar_cedula,
#         'correo': validar_correo,
#         'clave': val_clave,
#     }
#     val_mjs = {
#         'nombre': 'Error ingrese su nombre',
#         'cedula': 'Error ingrese su cedula',
#         'correo': 'Error ingrese su correo',
#         'clave': 'Error la clave debe tener 4 digitos'
#     }
#
#     def __init__(self, *args, callback=None, comp='', **kwargs):
#         super().__init__(*args, **kwargs)
#         self.callback = callback
#         self.comp = comp
#         self.componentes()
#
#     def componentes(self):
#         self.__class__.en_uso = True
#         ancho_pantalla = self.winfo_screenwidth()
#         altura_pantalla = self.winfo_screenheight()
#         x = (ancho_pantalla // 2) - (500 // 2)
#         y = (altura_pantalla // 2) - (250 // 2)
#         self.geometry(f'{500}x{250}+{x}+{y}')
#         self.title('Editar')
#         self.configure(bg=color.BLANCO)
#         self.resizable(False, False)
#
#         self.font_style3 = tk_font.Font(family="Cascadia Code", size=15, slant="italic", weight="bold")
#         lb = tk.Label(self, text=f'Ingrese un nuevo {self.comp}:', font=self.font_style3, background=color.BLANCO)
#         lb.place(x=50, y=50)
#
#         self.input = ttk.Entry(self, font=self.font_style3)
#         self.input.place(x=50, y=100, width=350, height=35)
#
#         btn1 = ttk.Button(self, text='Guardar', command=self.aceptar)
#         btn1.place(x=150, y=150)
#         btn2 = ttk.Button(self, text='Cancelar', command=self.cancelar)
#         btn2.place(x=250, y=150)
#
#         fuente = ("Cascadia Code", 15)
#         self.mesaje = tk.Label(self, bg=color.BLANCO, font=fuente)
#
#     def aceptar(self):
#         v = self.input.get()
#         if v != '':
#             r = self.__class__.val[self.comp](v)
#             if r:
#                 self.callback(v)
#                 self.mos_mensaje('')
#             else:
#                 self.mos_mensaje(self.__class__.val_mjs[self.comp])
#         else:
#             self.mos_mensaje('Campo vacio!')
#
# def mos_mensaje(self, text):
#     self.mesaje['foreground'] = color.ROJO_1A
#     self.mesaje['text'] = text
#     i = (self.winfo_width() // 2) - ((len(text) * 12) // 2)
#     self.mesaje.place(x=i, y=190)
#
#     def cancelar(self):
#         self.destroy()
#
#     def destroy(self):
#         self.__class__.en_uso = False
#         return super().destroy()
