import tkinter as tk
import tkinter.ttk as ttk
from util.Controladores import controllerRegsitro
class VentanaRegistro(tk.Toplevel):
    en_uso = False
    def __init__(self, *args,callback2=None, callback = None,funete1  = None ,funete2 = None,FONDO= None, **kwargs):
        super().__init__(*args, **kwargs)
        self.__callback = callback
        self.__callback2= callback2
        self.fuente1 = funete1
        self.fuente2 = funete2
        self.FONDO = FONDO
        self.componentes()
        self.__callback2('disable')
        self.__class__.en_uso = True
        self.flagProv = False
    def componentes(self):
        self.title("Registro")
        self.geometry("1270x720")
        self.resizable(False,False)
        self.configure(bg=self.FONDO)
        #label titulo
        labelT = tk.Label(self,text="Registrate",font= self.fuente1,bg=self.FONDO)
        labelT.place(x =460,y=67)
        #Labels decorativos
        label = tk.Label(self, bg="#0E4C57").place(x=55, y=160, width=75, height=500)
        label = tk.Label(self,bg="#5E803D").place(x=1121,y=50,width=70,height=500)
        # estilos inputs
        ttk.Style().theme_use('clam')
        ttk.Style().configure('pad.TEntry', selectbackground = '#93DFB9', padding='10 1 1 1', insertcolor="#5E803D", bordercolor='#ddd')
        ttk.Style().configure('pad.TButton', foreground="#fff", background="#5E803D", bordercolor='#ddd', font=("Cascadia Code", 16))
        ttk.Style().configure('pad.TCombobox',padding='10 1 1 1',bordercolor='#ddd',selectbackground='#fff',selectforeground='#000')
        ttk.Style().map('pad.TEntry', lightcolor=[('focus', '#5E803D')])
        ttk.Style().map('pad.TButton', background=[('pressed', '#4B6730'), ('active', '#5B7C3B')])
        ttk.Style().map('pad.TCombobox',fieldbackground=[('readonly', self.FONDO)])
        #contain formulario
        frameRegistro = tk.Frame(self,width=520,height=500,bg=self.FONDO)
        frameRegistro.place(x=150,y=160)
        #inputs formulario
        #Nombre y apellido
        label = tk.Label(frameRegistro,font= self.fuente2,text="Nombres y Apellidos:",foreground="#444",bg=self.FONDO).place(x= 0, y = 0)
        self.inputNombre =  ttk.Entry(frameRegistro,style='pad.TEntry',font=("Cascadia Code",16))
        self.inputNombre.place(x= 0, y = 40,width=470,height=36)
        #cedula
        label = tk.Label(frameRegistro, font=self.fuente2, text="Numero de CI:", foreground="#444", bg=self.FONDO).place(x= 0, y = 100)
        self.inputCedula = ttk.Entry(frameRegistro, style='pad.TEntry', font=("Cascadia Code", 16))
        self.inputCedula.place(x= 0, y = 140,width=470,height=36)
        #Correo
        label = tk.Label(frameRegistro,font= self.fuente2,text="Correo:",foreground="#444",bg=self.FONDO).place(x= 0, y = 200)
        self.inputCorreo =  ttk.Entry(frameRegistro,style='pad.TEntry',font=("Cascadia Code",16))
        self.inputCorreo.place(x= 0, y = 240,width=470,height=36)
        #Telefono
        label = tk.Label(frameRegistro,font= self.fuente2,text="Telefono:",foreground="#444",bg=self.FONDO).place(x=0, y=300)
        self.inputTelefono =  ttk.Entry(frameRegistro,style='pad.TEntry',font=("Cascadia Code",16))
        self.inputTelefono.place(x= 0, y = 340 ,width=470,height=36)
        #Provincias
        label = tk.Label(frameRegistro, font=self.fuente2, text="Provicias:", foreground="#444", bg=self.FONDO).place(x=0, y=400)
        self.comboBoxProv = ttk.Combobox(frameRegistro,font=("Cascadia Code", 15),style='pad.TCombobox' ,state="readonly")
        self.comboBoxProv.place(x= 0, y = 440 ,width=470,height=36)
        self.comboBoxProv['values'] = provincias
        self.comboBoxProv.current(0)
        self.comboBoxProv.bind("<<ComboboxSelected>>",self.cambiarCiudades)
        #Formulario 2
        frameRegistro2 = tk.Frame(self,width=430,height=472,bg=self.FONDO)
        frameRegistro2.place(x=680,y=160)
        #Ciudad
        label = tk.Label(frameRegistro2, font=self.fuente2, text="Ciudad:", foreground="#444", bg=self.FONDO).place(x=0, y=0)
        self.comboBoxCuidad = ttk.Combobox(frameRegistro2, font=("Cascadia Code", 15), style='pad.TCombobox', state="readonly")
        self.comboBoxCuidad.place(x=0, y=60, width=400, height=36)
        self.comboBoxCuidad['values'] = ['Seleccione una cuidad']
        self.comboBoxCuidad.current(0)
        #Claves
        label = tk.Label(frameRegistro2, font=self.fuente2, text="Clave de 4 digitos:", foreground="#444", bg=self.FONDO).place(x=0, y=100)
        self.inputCave  = ttk.Entry(frameRegistro2,style='pad.TEntry',font=("Cascadia Code",16), show = "*")
        self.inputCave.place(x= 0, y = 160,width=300,height=36)
        label = tk.Label(frameRegistro2, font=self.fuente2, text="Confirme su clave:", foreground="#444", bg=self.FONDO).place(x=0, y=200)
        self.inputCave2  = ttk.Entry(frameRegistro2,style='pad.TEntry',font=("Cascadia Code",16), show = "*")
        self.inputCave2.place(x= 0, y = 260,width=300,height=36)

        self.labelAviso = tk.Label(self,text="",foreground="#B80000",bg="#fff",font=("Cascadia Code",12))
        self.labelAviso.place(x=700,y=500)

        self.botonRegistrar = ttk.Button(self,text="Registrarse",style="pad.TButton", command= self.registrar)
        self.botonRegistrar.place(x=750,y=550,width=172,height=45)

    def destroy(self):
        self.__class__.en_uso = False
        self.__callback2('normal')
        return super().destroy()

    def registrar(self):
        respuesta = controllerRegsitro(self.inputNombre.get(),self.inputCedula.get(),self.inputTelefono.get(),self.inputCorreo.get(),self.inputCave.get())
        if respuesta[0]:
            if  self.flagProv:
                self.__callback(self.inputNombre.get(),self.inputCedula.get(),self.inputCave.get(),self.inputCorreo.get(),self.inputTelefono.get(),self.comboBoxCuidad.get(),self.comboBoxProv.get())
                self.destroy()
            else:
                self.labelAviso['text']='Seleccione una provincia y ciudad'
        else:
            self.labelAviso['text']=respuesta[1]



    def cambiarCiudades(self,event):
        if self.comboBoxProv.get() != 'Seleccione una Provincia':
            self.comboBoxCuidad['values'] = ciudades[self.comboBoxProv.get()]
            self.comboBoxCuidad.current(0)
            self.flagProv = True
        else:
            self.comboBoxCuidad['values'] = ['Seleccione una cuidad']
            self.comboBoxCuidad.current(0)
            self.flagProv = False

provincias = ['Seleccione una Provincia', 'Azuay',  'Bolivar','Cañar', 'Carchi', 'Chimborazo','Cotopaxi', 'El Oro',
                'Esmeraldas', 'Galápagos', 'Guayas','Imbabura', 'Loja', 'Los Ríos','Manabí', 'Morona Santiago','Napo',
                'Orellana','Pastaza','Pichincha','Santa Elena','Santo Domingo de los Tsáchilas','Sucumbíos', 'Tungurahua','Zamora Chinchipe']

prov1= ( "Camilo Ponce Enríquez","Chordeleg","Cuenca","El Pan","Girón","Guachapala", "Gualaceo","Nabón","Oña","Paute","Pucará", "San Fernando"," Santa Isabel","Sevilla de Oro","Sigsig")
prov2 = ("Caluma","Chillanes","Chimbo","Echeandía","Guaranda","Las Naves","San Miguel")
prov3 = ("Azogues","Biblián","Cañar","Déleg","El Tambo","La Troncal")
prov4 =("Bolívar","Espejo","Mira","Montúfar","Tulcán")
prov5 = ( "Alausí","Chambo","Chunchi","Colta","Cumandá","Guamote","Guano","Pallatanga","Penipe","Riobamba")
prov6 = ("La Maná","Latacunga","Pangua","Pujilí","Salcedo","Saquisilí","Sigchos")
prov7 = ( "Arenillas","Atahualpa","Balsas","Chilla","El Guabo","Huaquillas","Isla Correa","Isla Matapalo","Las Lajas","Machala","Marcabelí","Pasaje","Piñas","Portovelo","Santa","Rosa","Zaruma")
prov8 = ("Atacames","La Concordia","Eloy Alfaro","Esmeraldas","Muisne","Quinindé","Río Verde","San Lorenzo")
prov9 = ("Isabela","San Cristóbal","Santa Cruz")
prov10 = ("Alfredo Baquerizo Moreno (Jujan)","Balao","Balzar","Bucay","Colimes","Coronel Marcelino Mariduena","Cumanda","Daule","Eloy Alfaro (Durán)","El Empalme","El Triunfo","General Antonio Elizalde","Guayaquil","Isidro Ayora","Lomas de Sargentillo","Milagro (Durán)","Naranjal","Naranjito","Narcisa de Jesús (Nobol)","Palestina","Pedro Carbo","Playas (Durán)","General Villamil Playas","Samborondón","Salitre (Durán)","San Jacinto de Yaguachi","Santa Lucía (Durán)","Simón Bolívar (Durán)","Urbina Jado","San Jacinto de Yaguachi","Troncal (Durán)")
prov11 = ("Antonio Ante","Cotacachi","Ibarra","Otavalo","Pimampiro","San Miguel de Urcuquí")
prov12 =("Calvas","Catamayo Canton","Celica","Chaguarpamba","Espíndola","Gonzanamá","Loja","Macará","Paltas","Pindal","Puyango","Quilanga","Saraguro","Sozoranga","Zapotillo")
prov13 = ("Baba","Babahoyo","Buena Fe","Mocache","Montalvo","Palenque","Pueblo Viejo","Quevedo","Urdaneta","Ventanas","Vinces")
prov14 = ("Bolívar (Ecuador)","Chone","El Carmen (Ecuador)","Flavio Alfaro","Jama","Jaramijó","Jipijapa","Junín","Manta (Ecuador)","Montecristi (Ecuador)","Olmedo (Ecuador)","Paján","Pedernales","Pichincha","Portoviejo","Puerto Lopéz","Rocafuerte","San Vicente","Santa Ana (Ecuador)","Sucre (Ecuador)","Tosagua","Veinticuatro de Mayo")
prov15 =("Gualaquiza","Huamboya","Limón Indanza","Logroño (Ecuador)","Morona","Pablo Sexto","Palora","San Juan Bosco (Ecuador)","Santiago (Ecuador)","Sucúa","Taisha","Tiwinza")
prov16 = ( "Archidona","Carlos Luis Arosemena Tola","El Chaco","Quijos","Tena")
prov17 =("Aguarico","Francisco de Orellana","Joya de los Sachas","Loreto")
prov18 = ("Arajuno","Mera","Pastaza","Santa Clara (Ecuador)")
prov19 = ("Cayambe","Mejía","Pedro Moncayo","Pedro Vicente Maldonado","Puerto Quito","Quito","Rumiñahui","San Miguel de los Bancos")
prov20 = ( "La Libertad (Ecuador)","Salinas (Ecuador)","Santa Elena (Ecuador)")
prov21 = ("Santo Domingo de los Colorados")
prov22 = ("Cascales","Cuyabeno","Gonzalo Pizarro","Lago Agrio","Putumayo","Shushufindi","Sucumbios")
prov23 = ("Ambato","Baños (Ecuador)","Cevallos","Mocha","Patate","Pelileo")
prov24 = ("Centinela del Cóndor","Chinchipe","El Pangui","Palanda","Paquisha","Nangaritza","Yacuambi","Yantzaza","Zamora (Ecuador)")


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