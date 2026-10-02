from tkinter import Frame, Label, Entry, Text, messagebox
from config import FUENTE, TAMANIO, BACKLBL


class FormularioUsuario(Frame):
    """Panel con los campos Name, Last Name, Password y Address."""

    def __init__(self, master):
        super().__init__(master, bg="#ffffff", bd=0.5, relief="solid")
        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.lbl_name = Label(self, text="Name: ", font=(FUENTE, TAMANIO), bg=BACKLBL)
        self.lbl_last_name = Label(self, text="Last Name: ", font=(FUENTE, TAMANIO), bg=BACKLBL)
        self.lbl_password = Label(self, text="Password: ", font=(FUENTE, TAMANIO), bg=BACKLBL)
        self.lbl_addres = Label(self, text="Address: ", font=(FUENTE, TAMANIO), bg=BACKLBL)

        self.lbl_name.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")
        self.lbl_last_name.grid(row=1, column=0, padx=10, pady=10, sticky="nswe")
        self.lbl_password.grid(row=2, column=0, padx=10, pady=10, sticky="nswe")
        self.lbl_addres.grid(row=3, column=0, padx=10, pady=10, sticky="nswe")

        # Entry y Text
        self.txt_name = Entry(self, width=30, font=(FUENTE, TAMANIO))
        self.txt_last_name = Entry(self, width=30, font=(FUENTE, TAMANIO))
        self.txt_password = Entry(self, width=30, font=(FUENTE, TAMANIO), show="*")
        self.text_addres = Text(self, width=23, height=5, font=(FUENTE, TAMANIO))

        self.txt_name.grid(row=0, column=1, padx=10, pady=10, sticky="we")
        self.txt_last_name.grid(row=1, column=1, padx=10, pady=10, sticky="we")
        self.txt_password.grid(row=2, column=1, padx=10, pady=10, sticky="we")
        self.text_addres.grid(row=3, column=1, padx=10, pady=10, sticky="we")

    def get_datos(self):
        """Devuelve (nombre, apellido, password, address) o None si falta algo."""
        nombre = self.txt_name.get().strip()
        apellido = self.txt_last_name.get().strip()
        password = self.txt_password.get().strip()
        # El Text siempre agrega un salto de línea final; "end-1c" lo quita
        address = self.text_addres.get("1.0", "end-1c").strip()

        if not nombre or not apellido or not password or not address:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return None
        return nombre, apellido, password, address

    def limpiar(self):
        self.txt_name.delete(0, "end")
        self.txt_last_name.delete(0, "end")
        self.txt_password.delete(0, "end")
        self.text_addres.delete("1.0", "end")

    def cargar(self, nombre, apellido, password, address):
        self.limpiar()
        self.txt_name.insert(0, nombre)
        self.txt_last_name.insert(0, apellido)
        self.txt_password.insert(0, password)
        self.text_addres.insert("1.0", address)
