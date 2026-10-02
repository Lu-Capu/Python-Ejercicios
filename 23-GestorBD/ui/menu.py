from tkinter import Menu
from config import FUENTE


class BarraMenu(Menu):
    """Barra de menú superior.

    `comandos` es un diccionario con las claves: crear_bd, salir, create,
    read, update, delete, license, about.
    """

    def __init__(self, ventana, comandos):
        super().__init__(ventana)
        self.comandos = comandos
        self.create_widgets()
        ventana.config(menu=self)

    def create_widgets(self):
        c = self.comandos

        self.menu_archivo = Menu(self, tearoff=0, font=(FUENTE, 9))
        self.menu_archivo.add_command(label="Crear BD", command=c["crear_bd"])
        self.menu_archivo.add_command(label="Salir", command=c["salir"])

        self.menu_crud = Menu(self, tearoff=0, font=(FUENTE, 9))
        self.menu_crud.add_command(label="Insert", command=c["create"])
        self.menu_crud.add_command(label="Read", command=c["read"])
        self.menu_crud.add_command(label="Update", command=c["update"])
        self.menu_crud.add_command(label="Delete", command=c["delete"])

        self.menu_help = Menu(self, tearoff=0, font=(FUENTE, 9))
        self.menu_help.add_command(label="License", command=c["license"])
        self.menu_help.add_command(label="About me", command=c["about"])

        self.add_cascade(label="   Archivo ", menu=self.menu_archivo, font=(FUENTE, 11))
        self.add_cascade(label="   Crud    ", menu=self.menu_crud, font=(FUENTE, 11))
        self.add_cascade(label="   Help    ", menu=self.menu_help, font=(FUENTE, 11))
