import tkinter as tk
import tkinter.ttk as ttk
from util.Controladores import controller_regsitro
import tkinter.font as tk_font
from estilos.colores import color_sistema
from util.Cajero import Cajero

color = color_sistema()


class VentanaRegistro(tk.Toplevel):
    en_uso = False
    ANCHO = 1270
    ALTO = 720

    def __init__(self, *args, callback2=None, callback=None,info_user = None,mood='', **kwargs):
        super().__init__(*args, **kwargs)
        self.__callback = callback
        self.__callback2 = callback2
        self.mood = mood
        self.info_user = info_user
        self.componentes()
        self.__class__.en_uso = True


    def componentes(self):
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        x = (ancho_pantalla // 2) - (self.__class__.ANCHO // 2)
        y = (altura_pantalla // 2) - (self.__class__.ALTO // 2)
        self.geometry(f'{self.__class__.ANCHO}x{self.__class__.ALTO}+{x}+{y}')
        self.title(self.mood)
        self.resizable(False, False)
        self.configure(bg=color.BLANCO)

        font_style1 = tk_font.Font(family="Cascadia Code", size=44, slant="italic", weight="bold")
        font_style2 = tk_font.Font(family="Cascadia Code", size=20, slant="italic")

        # label titulo
        labelT = tk.Label(self, text=self.mood, font=font_style1, bg=color.BLANCO)
        labelT.place(x=460, y=67)
        # Labels decorativos
        label = tk.Label(self, bg=color.AZUL_57).place(x=55, y=160, width=75, height=500)
        label = tk.Label(self, bg=color.VERDE_3D).place(x=1121, y=50, width=70, height=500)
        # estilos inputs
        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TEntry', selectbackground=color.CELESTE_B9, padding='10 1 1 1',
                              insertcolor=color.VERDE_3D, bordercolor=color.GRIS_DD)
        ttk.Style().configure('pad.TButton', foreground=color.BLANCO, background=color.VERDE_3D,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 16))
        ttk.Style().configure('pad.TCombobox', padding='10 1 1 1', bordercolor=color.GRIS_DD,
                              selectbackground=color.BLANCO, selectforeground=color.NEGRO)
        ttk.Style().map('pad.TEntry', lightcolor=[('focus', color.VERDE_3D)])
        ttk.Style().map('pad.TButton', background=[('pressed', color.VERDE_30), ('active', color.VERDE_3B)])
        ttk.Style().map('pad.TCombobox', fieldbackground=[('readonly', color.BLANCO)])
        # contain formulario
        frame_registro = tk.Frame(self, width=520, height=500, bg=color.BLANCO)
        frame_registro.place(x=150, y=160)
        # inputs formulario
        # Nombre y apellido
        label = tk.Label(frame_registro, font=font_style2, text="Nombres y Apellidos:", foreground=color.NEGRO_44,
                         bg=color.BLANCO)
        label.place(x=0, y=0)
        self.input_nombre = ttk.Entry(frame_registro, style='pad.TEntry', font=("Cascadia Code", 16))
        self.input_nombre.place(x=0, y=40, width=470, height=36)
        self.input_nombre.insert(0,self.info_user[0])
        # cedula
        label = tk.Label(frame_registro, font=font_style2, text="Numero de CI:", foreground=color.NEGRO_44,
                         bg=color.BLANCO).place(x=0, y=100)
        self.input_cedula = ttk.Entry(frame_registro, style='pad.TEntry', font=("Cascadia Code", 16))
        self.input_cedula.place(x=0, y=140, width=470, height=36)
        self.input_cedula.insert(0,self.info_user[1])
        # Correo
        label = tk.Label(frame_registro, font=font_style2, text="Correo:", foreground=color.NEGRO_44,
                         bg=color.BLANCO).place(x=0, y=200)
        self.input_correo = ttk.Entry(frame_registro, style='pad.TEntry', font=("Cascadia Code", 16))
        self.input_correo.place(x=0, y=240, width=470, height=36)
        self.input_correo.insert(0,self.info_user[2])
        # Telefono
        label = tk.Label(frame_registro, font=font_style2, text="Telefono:", foreground=color.NEGRO_44,
                         bg=color.BLANCO).place(x=0, y=300)
        self.input_celular = ttk.Entry(frame_registro, style='pad.TEntry', font=("Cascadia Code", 16))
        self.input_celular.place(x=0, y=340, width=470, height=36)
        self.input_celular.insert(0,self.info_user[3])
        # Provincias
        label = tk.Label(frame_registro, font=font_style2, text="Provicias:", foreground=color.NEGRO_44,
                         bg=color.BLANCO).place(x=0, y=400)
        self.combo_box_prov = ttk.Combobox(frame_registro, font=("Cascadia Code", 15), style='pad.TCombobox',
                                           state="readonly")

        res = Cajero().prov_ciudades()
        self.combo_box_prov.place(x=0, y=440, width=470, height=36)
        self.combo_box_prov['values'] = res['provincia']
        self.combo_box_prov.current(self.info_user[4])
        self.combo_box_prov.bind("<<ComboboxSelected>>",
                                 lambda e, ciudad=res['ciudad']: self.cambiar_ciudades(event=e, ciudades=ciudad))
        # Formulario 2
        frame_registro2 = tk.Frame(self, width=430, height=472, bg=color.BLANCO)
        frame_registro2.place(x=680, y=160)

        # Ciudad
        label = tk.Label(frame_registro2, font=font_style2, text="Ciudad:", foreground=color.NEGRO_44,
                         bg=color.BLANCO).place(x=0, y=0)
        self.combo_box_cuidad = ttk.Combobox(frame_registro2, font=("Cascadia Code", 15), style='pad.TCombobox',
                                             state="readonly")
        self.combo_box_cuidad.place(x=0, y=60, width=400, height=36)
        if self.info_user[4] != 0:
            print('pasaa')
            self.cambiar_ciudades(ciudades=res['ciudad'])
        else:
            self.combo_box_cuidad['values'] = ['Seleccione una cuidad']
            self.flag_prov = False

        self.combo_box_cuidad.current(self.info_user[5])

        

        # Claves
        label = tk.Label(frame_registro2, font=font_style2, text="Clave de 4 digitos:", foreground=color.NEGRO_44,
                         bg=color.BLANCO)
        label.place(x=0, y=100)
        self.input_clave = ttk.Entry(frame_registro2, style='pad.TEntry', font=("Cascadia Code", 16), show="*")
        self.input_clave.place(x=0, y=160, width=300, height=36)
        self.input_clave.insert(0,self.info_user[7])
        label = tk.Label(frame_registro2, font=font_style2, text="Confirme su clave:", foreground=color.NEGRO_44,
                         bg=color.BLANCO).place(x=0, y=200)
        self.input_clave2 = ttk.Entry(frame_registro2, style='pad.TEntry', font=("Cascadia Code", 16), show="*")
        self.input_clave2.place(x=0, y=260, width=300, height=36)
        self.input_clave2.insert(0,self.info_user[7])
        self.label_aviso = tk.Label(self, text="", foreground=color.ROJO_00, bg=color.BLANCO,
                                    font=("Cascadia Code", 12))
        self.label_aviso.place(x=700, y=500)

        self.boton_registrar = ttk.Button(self, text=self.mood, style="pad.TButton", command=self.registrar)
        self.boton_registrar.place(x=750, y=550, width=172, height=45)

    def destroy(self):
        self.__class__.en_uso = False
        return super().destroy()

    def registrar(self):
        # Valida todos lso campos
       
        respuesta = controller_regsitro(self.input_nombre.get(),
                                        self.input_cedula.get(),
                                        self.input_celular.get(),
                                        self.input_correo.get(),
                                        self.input_clave.get(),
                                        self.input_clave2)
        if respuesta[0] :

            if self.flag_prov:
                selec = self.combo_box_cuidad.current()
                selec = self.index_cidades[0]
                res = Cajero().valida_cuentas( self.input_cedula.get())
                if not res['estado'] or self.mood.lower() == 'editar':
                    if self.mood.lower() == 'registrar':
                        self.__callback(self.input_nombre.get(),
                                        self.input_cedula.get(),
                                        self.input_clave.get(),
                                        self.input_correo.get(),
                                        self.input_celular.get(),
                                        selec)
                    else:
                        self.__callback(self.info_user[6],
                                        self.input_nombre.get(),
                                        self.input_cedula.get(),
                                        self.input_clave.get(),
                                        self.input_correo.get(),
                                        self.input_celular.get(),
                                        selec)
                    self.__callback2()
                    self.destroy()
                else:
                     self.label_aviso['text'] = 'Cedula ya registrada'
            else:
                self.label_aviso['text'] = 'Seleccione una provincia y ciudad'
        else:
            self.label_aviso['text'] = respuesta[1]

    def cambiar_ciudades(self, event=None, ciudades=None):
        s = self.combo_box_prov.current()
        print(s)
        ciu = []
        self.index_cidades = []
        if s != 0:
            for j in ciudades:
                if j[2] == s:
                    ciu.append(j[1])
                    self.index_cidades.append(j[0])

            
            self.combo_box_cuidad['values'] = ciu
            self.combo_box_cuidad.current(self.info_user[5])
            self.flag_prov = True
        else:
            self.combo_box_cuidad['values'] = ['Seleccione una cuidad']
            self.combo_box_cuidad.current(0)
            self.flag_prov = False
