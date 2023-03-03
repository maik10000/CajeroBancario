import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tk_font
from estilos.colores import color_sistema

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
        x = (ancho_pantalla // 2) - (800 // 2)
        y = (altura_pantalla // 2) - (600 // 2)
        self.geometry(f'{800}x{600}+{x}+{y}')
        self.title('Ajustes')
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
        label.place(x=683, y=52, width=75, height=500)
        label_nombre = tk.Label(self, text=self.infoUser.get_nombre(), font=self.font_style2, bg=color.BLANCO)
        label_nombre.place(x=210, y=75)

        label = tk.Label(self, text=self.infoUser.get_numero_cuenta(), font=self.font_style3, bg=color.BLANCO,
                         foreground=color.GRIS_B6)
        label.place(x=250, y=150)

        label_cedula = tk.Label(self, text=self.infoUser.get_cedula(), font=self.font_style3, bg=color.BLANCO)
        label_cedula.place(x=270, y=232)

        label = tk.Label(self, text="Ciudad:", font=self.font_style3, bg=color.BLANCO, foreground=color.GRIS_B6)
        label.place(x=128, y=300)
        label_ciudad = tk.Label(self, text=self.infoUser.get_ciudad(), font=self.font_style3, bg=color.BLANCO)
        label_ciudad.place(x=128, y=357)

        label = tk.Label(self, text='Provincia:', font=self.font_style3, bg=color.BLANCO, foreground=color.GRIS_B6)
        label.place(x=437, y=307)
        label_provin = tk.Label(self, text=self.infoUser.get_provicia(), font=self.font_style3, bg=color.BLANCO)
        label_provin.place(x=437, y=357)

        label = tk.Label(self, text="Contraseña", font=self.font_style3, bg=color.BLANCO)
        label.place(x=256, y=436)
        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TButton', foreground=color.BLANCO, background=color.VERDE_3D,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 12))
        ttk.Style().map('pad.TButton', background=[('pressed', color.VERDE_30), ('active', color.VERDE_3B)])

        btn_editar_nombre = ttk.Button(self, text="E", command=lambda: self.editar(comp_edit=label_nombre,
                                                                                   btn_cofirm=btn_editar_nombre)
                                       , style='pad.TButton')
        btn_editar_nombre.place(width=30, height=35, x=550, y=95)
        btn_editar_cedula = ttk.Button(self, text="E", command=lambda: self.editar(comp_edit=label_cedula,
                                                                                   btn_cofirm=btn_editar_cedula), style='pad.TButton')
        btn_editar_cedula.place(width=30, height=35, x=460, y=242)
        btn_editar_ciudad = ttk.Button(self, text="E", command=lambda: self.editar(comp_edit=label_ciudad,
                                                                                   btn_cofirm=btn_editar_ciudad), style='pad.TButton')
        btn_editar_ciudad.place(width=30, height=35, x=70, y=367)
        btn_editar_provi = ttk.Button(self, text="E", command=lambda: self.editar(comp_edit=label_provin,
                                                                                  btn_cofirm=btn_editar_provi), style='pad.TButton')
        btn_editar_provi.place(width=30, height=35, x=610, y=367)
        btn_editar = ttk.Button(self, text="E", style='pad.TButton')
        btn_editar.place(width=30, height=30, x=440, y=445)

        btn_regresar = ttk.Button(self, text='volver', command=self.destroy)
        btn_regresar.place(x=300, y=520, width=140, height=30)

    def editar(self, comp_edit=None, btn_cofirm=None):
        input_text_x = comp_edit.winfo_x()
        input_text_y = comp_edit.winfo_y()
        input_text_w = comp_edit.winfo_width()
        input_text_h = comp_edit.winfo_height()

        input_btn_x = btn_cofirm.winfo_x()
        input_btn_y = btn_cofirm.winfo_y()
        input_btn_w = btn_cofirm.winfo_width()
        input_btn_h = btn_cofirm.winfo_height()

        intput_edit = ttk.Entry(self, style='pad.TEntry', font=("Cascadia Code", 20))
        intput_edit.place(x=input_text_x, y=input_text_y, width=input_text_w, height=input_text_h)

        btn_cofirm['text'] = '✔'
        btn_cofirm['command'] = self.aceptar

        ttk.Style().theme_use('clam')
        ttk.Style().configure('cancelar.TButton', foreground=color.BLANCO, background=color.ROJO_00,
                              bordercolor=color.GRIS_DD, font=("Cascadia Code", 12))
        ttk.Style().map('cancelar.TButton', background=[('pressed', color.VERDE_30), ('active', color.ROJO_1A)])

        btn_editar_cancelar = ttk.Button(self, command=lambda: self.no_editar(
            label_edit=comp_edit,
            entry_edit=intput_edit,
            btn_1=btn_cofirm,
            btn_2=btn_editar_cancelar), text="x",style='cancelar.TButton')

        btn_editar_cancelar.place(x=input_btn_x + input_btn_w + 10, y=input_btn_y, width=input_btn_w,
                                  height=input_btn_h)

    def no_editar(self, label_edit=None, entry_edit=None, btn_1=None, btn_2=None):
        entry_edit.destroy()
        btn_2.destroy()

        btn_1['text'] = 'E'
        btn_1['command'] = lambda: self.editar(comp_edit=label_edit, btn_cofirm=btn_1)

    def destroy(self):
        self.__class__.en_uso = False
        return super().destroy()

    def aceptar(self):
        print('Editar!')
