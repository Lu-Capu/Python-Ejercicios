from tkinter import Menu
from config import FUENTE

class BarraMenu(Menu):

    def __init__(self, master,comando):
        super().__init__(master)
        self.comando=comando
        self._create_menu()
        master.config(menu=self)


    
    def _create_menu(self):
        self.menu_archivo = Menu(self, tearoff=0, font=(FUENTE, 9))
        self.menu_archivo.add_command(label="Salir", command=self.master.quit)

        self.menu_cat = Menu(self, tearoff=0, font=(FUENTE, 9))
        self.menu_cat.add_command(label="Visitar", command= self.comando)

        self.menu_help = Menu(self, tearoff=0, font=(FUENTE, 9))
        self.menu_help.add_command(label="License")
        self.menu_help.add_command(label="About me")

        self.add_cascade(label="   Archivo ", menu=self.menu_archivo, font=(FUENTE, 11))
        self.add_cascade(label="   Categorías    ", menu=self.menu_cat, font=(FUENTE, 11))
        self.add_cascade(label="   Ayuda   ", menu=self.menu_help, font=(FUENTE, 11))