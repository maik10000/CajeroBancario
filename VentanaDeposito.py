import tkinter as tk
import tkinter.ttk as ttk
class VentanaDeposito(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.componentes()

    def componentes(self):
        self.title("Deposito")
        self.geometry('800x600')
        self.resizable(False,False)
        self.configure(bg="#fff")

