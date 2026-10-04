from tkinter import Frame, Button
from config import FUENTE, TAMANIO, BACKB


class BarraBotones(Frame):
    #Diccionario que va arecibir   {"create": self.create_user, "read": self.read, ...}
    def __init__(self, master, comandos):
        super().__init__(master, bg=BACKB)
        self.comandos = comandos
        self.create_widgets()

    def _boton(self, texto, color, comando):
        return Button(
            self, text=texto, relief="flat", bd=0, cursor="hand2", bg=color,
            font=(FUENTE, TAMANIO, "bold"), command=comando
        )

    def create_widgets(self):
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        self.btn_create = self._boton("Insert", "green", self.comandos["create"])
        self.btn_read = self._boton("Read", "yellow", self.comandos["read"])
        self.btn_update = self._boton("Update", "cyan", self.comandos["update"])
        self.btn_delete = self._boton("Delete", "red", self.comandos["delete"])

        self.btn_create.grid(row=0, column=0, padx=15, pady=10, sticky="we")
        self.btn_read.grid(row=0, column=1, padx=15, pady=10, sticky="we")
        self.btn_update.grid(row=0, column=2, padx=15, pady=10, sticky="we")
        self.btn_delete.grid(row=0, column=3, padx=15, pady=10, sticky="we")
