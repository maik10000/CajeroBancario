import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tk_font
from estilos.colores import color_sistema


color = color_sistema()


class VentanaAjustes(tk.Toplevel):
    en_uso = False

    def __init__(self, *args,info_usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.infoUser = info_usuario
        self.componentes()

    def componentes(self):
        self.__class__.en_uso = True
        self.title('Ajustes')
        self.geometry('800x600')
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

        label = tk.Label(self, text=self.infoUser.get_numero_cuenta(), font=self.font_style3, bg=color.BLANCO, foreground=color.GRIS_B6)
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

        btn_editar_nombre = tk.Button(self, text="E", command=lambda: self.editar(comp_edit=label_nombre,
                                                                                  btn_change=btn_editar_nombre))
        btn_editar_nombre.place(width=30, height=30, x=550, y=95)
        btn_editar_cedula = tk.Button(self, text="E", command=lambda: self.editar(comp_edit=label_cedula,
                                                                                  btn_change=btn_editar_cedula))
        btn_editar_cedula.place(width=30, height=30, x=460, y=242)
        btn_editar_ciudad = tk.Button(self, text="E", command=lambda: self.editar(comp_edit=label_ciudad,
                                                                                  btn_change=btn_editar_ciudad))
        btn_editar_ciudad.place(width=30, height=30, x=70, y=367)
        btn_editar_provi = tk.Button(self, text="E", command=lambda: self.editar(comp_edit=label_provin,
                                                                                 btn_change=btn_editar_provi))
        btn_editar_provi.place(width=30, height=30, x=610, y=367)
        btn_editar = tk.Button(self, text="E")
        btn_editar.place(width=30, height=30, x=440, y=445)

        btn_regresar = tk.Button(self, text='volver', command=self.destroy)
        btn_regresar.place(x=300, y=520,width=140,height=30)

    def editar(self, comp_edit=None, btn_change=None):
        input_text_x = comp_edit.winfo_x()
        input_text_y = comp_edit.winfo_y()
        input_text_w = comp_edit.winfo_width()
        input_text_h = comp_edit.winfo_height()

        input_btn_x = btn_change.winfo_x()
        input_btn_y = btn_change.winfo_y()
        input_btn_w = btn_change.winfo_width()
        input_btn_h = btn_change.winfo_height()

        intput_edit = ttk.Entry(self, style='pad.TEntry', font=("Cascadia Code", 20))
        intput_edit.place(x=input_text_x, y=input_text_y, width=input_text_w, height=input_text_h)

        btn_change['text'] = '✔'
        btn_change['command'] = self.aceptar

        btn_editar_cancelar = tk.Button(self, command=lambda: self.no_editar(
            label_edit = comp_edit,
            entry_edit=intput_edit,
            btn_1=btn_change,
            btn_2=btn_editar_cancelar), text="x")

        btn_editar_cancelar.place(x=input_btn_x + input_btn_w + 10, y=input_btn_y, width=input_btn_w,
                                  height=input_btn_h)

    def no_editar(self,label_edit =None, entry_edit=None, btn_1=None, btn_2=None):
        entry_edit.destroy()
        btn_2.destroy()

        btn_1['text'] = 'E'
        btn_1['command'] = lambda: self.editar(comp_edit=label_edit,btn_change=btn_1)

    def destroy(self):
        self.__class__.en_uso = False
        return super().destroy()

    def aceptar(self):
        print('Editar!')

