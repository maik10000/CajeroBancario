import tkinter as tk
import tkinter.ttk as ttk
from util.Controladores import controller_regsitro
from estilos.colores import color_sistema
color = color_sistema()


class VentanaRegistro(tk.Toplevel):
    en_uso = False

    def __init__(self, *args,callback2=None, callback = None,funete1  = None ,funete2 = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.__callback = callback
        self.__callback2= callback2
        self.fuente1 = funete1
        self.fuente2 = funete2
        self.componentes()
        self.__callback2('disable')
        self.__class__.en_uso = True
        self.flag_prov = False

    def componentes(self):
        self.title("Registro")
        self.geometry("1270x720")
        self.resizable(False,False)
        self.configure(bg= color.BLANCO)
        #label titulo
        labelT = tk.Label(self,text="Registrate",font= self.fuente1,bg= color.BLANCO)
        labelT.place(x =460,y=67)
        #Labels decorativos
        label = tk.Label(self, bg=color.AZUL_57).place(x=55, y=160, width=75, height=500)
        label = tk.Label(self,bg=color.VERDE_3D).place(x=1121,y=50,width=70,height=500)
        # estilos inputs
        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TEntry', selectbackground = color.CELESTE_B9, padding='10 1 1 1', insertcolor=color.VERDE_3D, bordercolor=color.GRIS_DD)
        ttk.Style().configure('pad.TButton', foreground=color.BLANCO, background=color.VERDE_3D, bordercolor=color.GRIS_DD, font=("Cascadia Code", 16))
        ttk.Style().configure('pad.TCombobox',padding='10 1 1 1',bordercolor= color.GRIS_DD,selectbackground=color.BLANCO,selectforeground=color.NEGRO)
        ttk.Style().map('pad.TEntry', lightcolor=[('focus',color.VERDE_3D)])
        ttk.Style().map('pad.TButton', background=[('pressed', color.VERDE_30), ('active', color.VERDE_3B)])
        ttk.Style().map('pad.TCombobox',fieldbackground=[('readonly', color.BLANCO)])
        #contain formulario
        frame_registro = tk.Frame(self,width=520,height=500,bg= color.BLANCO)
        frame_registro.place(x=150,y=160)
        #inputs formulario
        #Nombre y apellido
        label = tk.Label(frame_registro,font= self.fuente2,text="Nombres y Apellidos:",foreground=color.NEGRO_44,bg= color.BLANCO).place(x= 0, y = 0)
        self.input_nombre =  ttk.Entry(frame_registro, style='pad.TEntry', font=("Cascadia Code", 16))
        self.input_nombre.place(x= 0, y = 40, width=470, height=36)
        #cedula
        label = tk.Label(frame_registro, font=self.fuente2, text="Numero de CI:", foreground=color.NEGRO_44, bg= color.BLANCO).place(x= 0, y = 100)
        self.input_cedula = ttk.Entry(frame_registro, style='pad.TEntry', font=("Cascadia Code", 16))
        self.input_cedula.place(x= 0, y = 140,width=470,height=36)
        #Correo
        label = tk.Label(frame_registro,font= self.fuente2,text="Correo:",foreground=color.NEGRO_44,bg= color.BLANCO).place(x= 0, y = 200)
        self.input_correo =  ttk.Entry(frame_registro,style='pad.TEntry',font=("Cascadia Code",16))
        self.input_correo.place(x= 0, y = 240,width=470,height=36)
        #Telefono
        label = tk.Label(frame_registro,font= self.fuente2,text="Telefono:",foreground=color.NEGRO_44,bg=color.BLANCO).place(x=0, y=300)
        self.input_celular =  ttk.Entry(frame_registro,style='pad.TEntry',font=("Cascadia Code",16))
        self.input_celular.place(x= 0, y = 340 ,width=470,height=36)
        #Provincias
        label = tk.Label(frame_registro, font=self.fuente2, text="Provicias:", foreground=color.NEGRO_44, bg=color.BLANCO).place(x=0, y=400)
        self.combo_box_prov = ttk.Combobox(frame_registro, font=("Cascadia Code", 15), style='pad.TCombobox', state="readonly")
        self.combo_box_prov.place(x= 0, y = 440, width=470, height=36)
        self.combo_box_prov['values'] = provincias
        self.combo_box_prov.current(0)
        self.combo_box_prov.bind("<<ComboboxSelected>>", self.cambiar_ciudades)
        #Formulario 2
        frame_registro2 = tk.Frame(self,width=430,height=472,bg=color.BLANCO)
        frame_registro2.place(x=680,y=160)
        #Ciudad
        label = tk.Label(frame_registro2, font=self.fuente2, text="Ciudad:", foreground=color.NEGRO_44, bg=color.BLANCO).place(x=0, y=0)
        self.combo_box_cuidad = ttk.Combobox(frame_registro2, font=("Cascadia Code", 15), style='pad.TCombobox', state="readonly")
        self.combo_box_cuidad.place(x=0, y=60, width=400, height=36)
        self.combo_box_cuidad['values'] = ['Seleccione una cuidad']
        self.combo_box_cuidad.current(0)
        #Claves
        label = tk.Label(frame_registro2, font=self.fuente2, text="Clave de 4 digitos:", foreground=color.NEGRO_44, bg=color.BLANCO).place(x=0, y=100)
        self.input_clave  = ttk.Entry(frame_registro2,style='pad.TEntry',font=("Cascadia Code",16), show = "*")
        self.input_clave.place(x= 0, y = 160,width=300,height=36)
        label = tk.Label(frame_registro2, font=self.fuente2, text="Confirme su clave:", foreground=color.NEGRO_44, bg=color.BLANCO).place(x=0, y=200)
        self.input_clave2  = ttk.Entry(frame_registro2,style='pad.TEntry',font=("Cascadia Code",16), show = "*")
        self.input_clave2.place(x= 0, y = 260,width=300,height=36)

        self.label_aviso = tk.Label(self, text="", foreground=color.ROJO_00, bg=color.BLANCO, font=("Cascadia Code", 12))
        self.label_aviso.place(x=700, y=500)

        self.boton_registrar = ttk.Button(self, text="Registrarse", style="pad.TButton", command= self.registrar)
        self.boton_registrar.place(x=750, y=550, width=172, height=45)

    def destroy(self):
        self.__class__.en_uso = False
        self.__callback2('normal')
        return super().destroy()

    def registrar(self):
        respuesta = controller_regsitro(self.input_nombre.get(), self.input_cedula.get(), self.input_celular.get(), self.input_correo.get(), self.input_clave.get(),self.input_clave2)
        if respuesta[0]:
            if  self.flag_prov:
                self.__callback(self.input_nombre.get(), self.input_cedula.get(), self.input_clave.get(), self.input_correo.get(), self.input_celular.get(), self.combo_box_cuidad.get(), self.combo_box_prov.get())
                self.destroy()
            else:
                self.label_aviso['text']= 'Seleccione una provincia y ciudad'
        else:
            self.label_aviso['text']=respuesta[1]



    def cambiar_ciudades(self, event):
        if self.combo_box_prov.get() != 'Seleccione una Provincia':
            self.combo_box_cuidad['values'] = ciudades[self.combo_box_prov.get()]
            self.combo_box_cuidad.current(0)
            self.flag_prov = True
        else:
            self.combo_box_cuidad['values'] = ['Seleccione una cuidad']
            self.combo_box_cuidad.current(0)
            self.flag_prov = False


provincias = ['Seleccione una Provincia', 'Azuay', 'Bolivar', 'Cañar', 'Carchi', 'Chimborazo', 'Cotopaxi', 'El Oro',
            'Esmeraldas', 'Galápagos', 'Guayas', 'Imbabura', 'Loja', 'Los Ríos', 'Manabí', 'Morona Santiago','Napo',
            'Orellana', 'Pastaza','Pichincha','Santa Elena', 'Santo Domingo de los Tsáchilas', 'Sucumbíos',
            'Tungurahua', 'Zamora Chinchipe']

prov1= ( "Camilo Ponce Enríquez","Chordeleg","Cuenca","El Pan","Girón","Guachapala", "Gualaceo","Nabón","Oña","Paute",
         "Pucará", "San Fernando","Santa Isabel","Sevilla de Oro","Sigsig")
prov2 = ("Caluma","Chillanes","Chimbo","Echeandía","Guaranda","Las Naves","San Miguel")
prov3 = ("Azogues","Biblián","Cañar","Déleg","El Tambo","La Troncal")
prov4 =("Bolívar","Espejo","Mira","Montúfar","Tulcán")
prov5 = ( "Alausí","Chambo","Chunchi","Colta","Cumandá","Guamote","Guano","Pallatanga","Penipe","Riobamba")
prov6 = ("La Maná","Latacunga","Pangua","Pujilí","Salcedo","Saquisilí","Sigchos")
prov7 = ( "Arenillas","Atahualpa","Balsas","Chilla","El Guabo","Huaquillas","Isla Correa","Isla Matapalo","Las Lajas",
          "Machala","Marcabelí","Pasaje","Piñas","Portovelo","Santa","Rosa","Zaruma")
prov8 = ("Atacames","La Concordia","Eloy Alfaro","Esmeraldas","Muisne","Quinindé","Río Verde","San Lorenzo")
prov9 = ("Isabela","San Cristóbal","Santa Cruz")
prov10 = ("Alfredo Baquerizo Moreno (Jujan)","Balao","Balzar","Bucay","Colimes","Coronel Marcelino Mariduena","Cumanda",
          "Daule","Eloy Alfaro (Durán)","El Empalme","El Triunfo","General Antonio Elizalde","Guayaquil","Isidro Ayora",
          "Lomas de Sargentillo","Milagro (Durán)","Naranjal","Naranjito","Narcisa de Jesús (Nobol)","Palestina",
          "Pedro Carbo","Playas (Durán)","General Villamil Playas","Samborondón","Salitre (Durán)",
          "San Jacinto de Yaguachi","Santa Lucía (Durán)","Simón Bolívar (Durán)","Urbina Jado",
          "San Jacinto de Yaguachi","Troncal (Durán)")
prov11 = ("Antonio Ante","Cotacachi","Ibarra","Otavalo","Pimampiro","San Miguel de Urcuquí")
prov12 = ("Calvas","Catamayo Canton","Celica","Chaguarpamba","Espíndola","Gonzanamá","Loja","Macará","Paltas","Pindal",
         "Puyango","Quilanga","Saraguro","Sozoranga","Zapotillo")
prov13 = ("Baba","Babahoyo","Buena Fe","Mocache","Montalvo","Palenque","Pueblo Viejo","Quevedo","Urdaneta","Ventanas",
          "Vinces")
prov14 = ("Bolívar (Ecuador)","Chone","El Carmen (Ecuador)","Flavio Alfaro","Jama","Jaramijó","Jipijapa","Junín",
          "Manta (Ecuador)","Montecristi (Ecuador)","Olmedo (Ecuador)","Paján","Pedernales","Pichincha","Portoviejo",
          "Puerto Lopéz","Rocafuerte","San Vicente","Santa Ana (Ecuador)","Sucre (Ecuador)",
          "Tosagua","Veinticuatro de Mayo")
prov15 =("Gualaquiza","Huamboya","Limón Indanza","Logroño (Ecuador)","Morona","Pablo Sexto","Palora",
         "San Juan Bosco (Ecuador)","Santiago (Ecuador)","Sucúa","Taisha","Tiwinza")
prov16 = ( "Archidona","Carlos Luis Arosemena Tola","El Chaco","Quijos","Tena")
prov17 =("Aguarico","Francisco de Orellana","Joya de los Sachas","Loreto")
prov18 = ("Arajuno","Mera","Pastaza","Santa Clara (Ecuador)")
prov19 = ("Cayambe","Mejía","Pedro Moncayo","Pedro Vicente Maldonado","Puerto Quito","Quito","Rumiñahui",
          "San Miguel de los Bancos")
prov20 = ("La Libertad (Ecuador)","Salinas (Ecuador)","Santa Elena (Ecuador)")
prov21 = "Santo Domingo de los Colorados"
prov22 = ("Cascales","Cuyabeno","Gonzalo Pizarro","Lago Agrio","Putumayo","Shushufindi","Sucumbios")
prov23 = ("Ambato","Baños (Ecuador)","Cevallos","Mocha","Patate","Pelileo")
prov24 = ("Centinela del Cóndor","Chinchipe","El Pangui","Palanda","Paquisha","Nangaritza","Yacuambi","Yantzaza",
          "Zamora (Ecuador)")


ciudades = {
    provincias[1]:prov1,
    provincias[2]:prov2,
    provincias[3]:prov3,
    provincias[4]:prov4,
    provincias[5]:prov5,
    provincias[6]:prov6,
    provincias[7]:prov7,
    provincias[8]:prov8,
    provincias[9]:prov9,
    provincias[10]:prov10,
    provincias[11]:prov11,
    provincias[12]:prov12,
    provincias[13]:prov13,
    provincias[14]:prov14,
    provincias[15]:prov15,
    provincias[16]:prov16,
    provincias[17]:prov17,
    provincias[18]:prov18,
    provincias[19]:prov19,
    provincias[20]:prov20,
    provincias[21]:prov21,
    provincias[22]:prov22,
    provincias[23]:prov23,
    provincias[24]:prov24
}