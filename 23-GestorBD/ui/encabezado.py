from tkinter import Frame, Label
from config import BACKB


class Encabezado(Frame):
    def __init__(self, master):
        super().__init__(master, bg=BACKB)
        self.create_widgets()

    def create_widgets(self):
        self.label_titulo = Label(
            self,
            text="Gestión de usuarios",
            font=("Segoe UI", 14, "bold"),
            bg=BACKB,
            fg="#111827",
            anchor="w"
        )
        self.label_subtitulo = Label(
            self,
            text="Administra los datos de los usuarios",
            font=("Segoe UI", 9),
            bg=BACKB,
            fg="#6b7280",
            anchor="w"
        )
        self.label_titulo.pack(fill="x", padx=15, pady=(10, 2))
        self.label_subtitulo.pack(fill="x", padx=15, pady=(0, 10))
