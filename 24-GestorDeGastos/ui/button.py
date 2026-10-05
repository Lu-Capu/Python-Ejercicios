from tkinter import Button, Frame
from config import FUENTE, TAMANIO, BACKGASTO

class Botones(Frame):

    def __init__(self, master, comandos):
        super().__init__(master, bg= BACKGASTO)
        self.comandos = comandos
        for i in range(4):
            self.columnconfigure(i, weight=1)
        
        self._create_widgets()


    def _boton(self, texto, color, comando):
        return Button(
            self, text=texto, relief="flat", bd=0, cursor="hand2", bg=color,
            font=(FUENTE, TAMANIO, "bold"), command=comando
        )

    def _create_widgets(self):
        self.btn_create = self._boton("Insert", "green", self.comandos["create"])
        self.btn_update = self._boton("Update", "cyan", self.comandos["update"])
        self.btn_delete = self._boton("Delete", "red", self.comandos["delete"])
        self.btn_limpiar = self._boton("Limpiar", "gray", self.comandos["clear"])

        self.btn_create.grid(row=0, column=0, padx=10, sticky="we")
        self.btn_update.grid(row=0, column=1, padx=10, sticky="we")
        self.btn_delete.grid(row=0, column=2, padx=10, sticky="we")
        self.btn_limpiar.grid(row=0, column=3, padx=10, sticky="we")
   