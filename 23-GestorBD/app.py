"""Ventana principal: une la interfaz (ui/) con la base de datos (database.py)."""
import sqlite3
from tkinter import Frame, messagebox, simpledialog

from config import BACKB, RUTA_BD
from textos import ABOUT_ME, LICENCIA
from ui.menu import BarraMenu
from ui.encabezado import Encabezado
from ui.formulario import FormularioUsuario
from ui.botones import BarraBotones


class Application(Frame):

    def __init__(self, master, repositorio):
        super().__init__(master, bg=BACKB)
        self.master = master
        self.repo = repositorio
        self.pack(fill="both", expand=True)

        self.create_widgets()
        self.centrar_ventana()

    def centrar_ventana(self):
        self.master.update_idletasks()

        ancho = self.master.winfo_width()
        alto = self.master.winfo_height()

        x = (self.master.winfo_screenwidth() - ancho) // 2
        y = (self.master.winfo_screenheight() - alto) // 2

        self.master.geometry(f"{ancho}x{alto}+{x}+{y}")

    def create_widgets(self):
        self.menu_bar = BarraMenu(self.master, {
            "crear_bd": self.crear_bd,
            "salir": self.quit,
            "create": self.create_user,
            "read": self.read,
            "update": self.update_user,
            "delete": self.delete,
            "license": self.licens,
            "about": self.about_me,
        })

        self.encabezado = Encabezado(self)
        self.encabezado.pack(fill="x", side="top")

        self.formulario = FormularioUsuario(self)
        self.formulario.pack(fill="x", padx=15, pady=10)

        self.barra_botones = BarraBotones(self, {
            "create": self.create_user,
            "read": self.read,
            "update": self.update_user,
            "delete": self.delete,
        })
        self.barra_botones.pack(fill="both", expand=True)

    # ---------- Acciones (conectan interfaz y base de datos) ----------
    def crear_bd(self):
        try:
            self.repo.crear_bd()
            messagebox.showinfo("BBDD", f"Base de datos creada/conectada en:\n{RUTA_BD}")
        except sqlite3.Error as err:
            messagebox.showerror("Error BBDD", f"Ocurrió un error al crear la base de datos:\n{err}")

    def create_user(self):
        datos = self.formulario.get_datos()
        if datos is None:
            return
        try:
            self.repo.insertar(*datos)
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")
            self.formulario.limpiar()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error al insertar datos:\n{e}")

    def read(self):
        id_usuario = simpledialog.askinteger("Buscar", "Ingrese el Id del Usuario a buscar: ")
        if id_usuario is None:
            return
        try:
            usuario = self.repo.buscar_por_id(id_usuario)
            if usuario:
                usuario_id, nombre, apellido, password, address = usuario
                self.formulario.cargar(nombre, apellido, password, address)
                messagebox.showinfo("Éxito", f"Usuario con ID {usuario_id} cargado correctamente.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar los datos:\n{e}")

    def update_user(self):
        datos = self.formulario.get_datos()
        if datos is None:
            return
        id_usuario = simpledialog.askinteger("Buscar ID", "Ingrese el id del usuario")
        if id_usuario is None:
            return
        try:
            if self.repo.actualizar(*datos, id_usuario):
                messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
                self.formulario.limpiar()
            else:
                messagebox.showwarning("Advertencia", f"No existe ningún usuario con el ID: {id_usuario}")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar datos:\n{e}")

    def delete(self):
        id_usuario = simpledialog.askinteger("Buscar ID", "Ingrese el Id del Usuario a eliminar: ")
        if id_usuario is None:
            return
        try:
            if self.repo.eliminar(id_usuario):
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
            else:
                messagebox.showwarning("Advertencia", f"No existe ningún usuario con el ID: {id_usuario}")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar al Usuario:\n{e}")

    def about_me(self):
        messagebox.showinfo("About me", ABOUT_ME)

    def licens(self):
        messagebox.showinfo("License", LICENCIA)
