from tkinter import Tk, Frame, messagebox, Label, Button, Entry, Text, Menu, simpledialog
import sqlite3
import textwrap
from pathlib import Path

class Application(Frame):
    
    FUENTE = "Century Gothic"
    TAMANIO = 9
    BACKB="#f4f6fb"
    BACKLBL= "#ffffff"
    CARPETA_DESTINO = Path.home() / "Downloads" / "MiApp_BD"
    RUTA_BD = CARPETA_DESTINO / "Users_BD.db"
    
    def __init__(self, master=None):
        super().__init__(master, bg=self.BACKB)
        self.master = master
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
        #-----------Menu_Bar-----------------
        self.menu_bar= Menu(self)
        #-----------Menu_ARCHIVO-----------------
        self.menu_archivo = Menu(self.menu_bar, tearoff=0, font=(self.FUENTE,9))
        self.menu_archivo.add_command(label="Crear BD",command= self.createBD)
        self.menu_archivo.add_command(label="Salir", command= self.quit)
        #-----------Menu_CRUD-----------------
        self.menu_crud = Menu(self.menu_bar,tearoff=0, font=(self.FUENTE,9))
        self.menu_crud.add_command(label="Create", command=self.create_user)
        self.menu_crud.add_command(label="Read", command=self.read)
        self.menu_crud.add_command(label="Update", command=self.update_user)
        self.menu_crud.add_command(label="Delete", command=self.delete)
        #-----------Menu_HELP-----------------
        self.menu_help = Menu(self.menu_bar, tearoff=0, font=(self.FUENTE,9))
        self.menu_help.add_command(label="License", command=self.licens)
        self.menu_help.add_command(label="About me", command=self.about_me)
        #AGREGAR LOS MENUS
        self.menu_bar.add_cascade(label="   Archivo ", menu=self.menu_archivo, font=(self.FUENTE,11))
        self.menu_bar.add_cascade(label="   Crud    ", menu=self.menu_crud, font=(self.FUENTE,11))
        self.menu_bar.add_cascade(label="   Help    ", menu=self.menu_help, font=(self.FUENTE,11))
        self.master.config(menu=self.menu_bar)
        #LABEL TITULO y Contenedor
        self.frame_titulo = Frame(self, bg=self.BACKB)
        self.frame_titulo.pack(fill="x", side="top")
        self.label_titulo = Label(
            self.frame_titulo,
            text="Gestión de usuarios",
            font=("Segoe UI", 14, "bold"),
            bg=self.BACKB,
            fg="#111827",
            anchor="w"
        )
        self.label_subtitulo = Label(
            self.frame_titulo,
            text="Administra los datos de los usuarios",
            font=("Segoe UI", 9),
            bg=self.BACKB,
            fg="#6b7280",
            anchor="w"
        )
        self.label_titulo.pack(fill="x", padx=15, pady=(10, 2))
        self.label_subtitulo.pack(fill="x", padx=15, pady=(0, 10))
        #---------Contenedor de Label, Entry, Text------
        self.frame_panel = Frame(self, bg="#ffffff", bd=0.5, relief="solid")
        self.frame_panel.pack(fill="x", padx=15, pady=10)
        #Label
        self.lbl_name = Label(self.frame_panel, text="Name: ", font=(self.FUENTE, self.TAMANIO), bg=self.BACKLBL)
        self.lbl_last_name = Label(self.frame_panel, text="Last Name: ", font=(self.FUENTE, self.TAMANIO), bg=self.BACKLBL)
        self.lbl_password = Label(self.frame_panel, text="Password: ", font=(self.FUENTE, self.TAMANIO), bg=self.BACKLBL)
        self.lbl_addres = Label(self.frame_panel, text="Address: ", font=(self.FUENTE, self.TAMANIO), bg=self.BACKLBL)
        
        self.lbl_name.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")
        self.lbl_last_name.grid(row=1, column=0, padx=10, pady=10, sticky="nswe")
        self.lbl_password.grid(row=2, column=0, padx=10, pady=10, sticky="nswe")
        self.lbl_addres.grid(row=3, column=0, padx=10, pady=10, sticky="nswe")
        #Entry y Text
        self.txt_name = Entry(self.frame_panel, width=30, font=(self.FUENTE, self.TAMANIO))
        self.txt_last_name = Entry(self.frame_panel, width=30, font=(self.FUENTE, self.TAMANIO))
        self.txt_password = Entry(self.frame_panel, width=30, font=(self.FUENTE, self.TAMANIO))
        self.text_addres = Text(self.frame_panel, width=23, height=5, font=(self.FUENTE, self.TAMANIO))
        
        self.txt_name.grid(row=0, column=1, padx=10, pady=10, sticky="we")
        self.txt_last_name.grid(row=1, column=1, padx=10, pady=10, sticky="we")
        self.txt_password.grid(row=2, column=1, padx=10, pady=10, sticky="we")
        self.text_addres.grid(row=3, column=1, padx=10, pady=10, sticky="we")
        
        
        #---------Contenedor de Butons------
        self.frame_button = Frame(self, bg=self.BACKB)
        self.frame_button.pack(fill="both", expand=True)
        for i in range(4):
            self.frame_button.grid_columnconfigure(i, weight=1)
        #Button
        self.btn_create = Button(self.frame_button, text="Create", relief="flat", bd=0, cursor="hand2", bg="green", font=(self.FUENTE, self.TAMANIO, "bold"), command=self.create_user)
        self.btn_read = Button(self.frame_button, text="Read", relief="flat", bd=0, cursor="hand2", bg="yellow", font=(self.FUENTE, self.TAMANIO, "bold"), command=self.read)
        self.btn_update = Button(self.frame_button, text="Update", relief="flat", bd=0, cursor="hand2", bg="cyan", font=(self.FUENTE, self.TAMANIO, "bold"), command=self.update_user)
        self.btn_delete = Button(self.frame_button, text="Delete", relief="flat", bd=0, cursor="hand2", bg="red", font=(self.FUENTE, self.TAMANIO, "bold"), command=self.delete)
        
        self.btn_create.grid(row=0,column=0, padx=15, pady=10, sticky="we")
        self.btn_read.grid(row=0,column=1, padx=15, pady=10, sticky="we")
        self.btn_update.grid(row=0,column=2, padx=15, pady=10, sticky="we")
        self.btn_delete.grid(row=0,column=3, padx=15, pady=10, sticky="we")

    def createBD(self):
            try:
                #crea la carpeta si no existe
                #parents=True crea carpetas anidadas
                #xist_ok=True verifica si existe, sino crea las carpeta
                self.CARPETA_DESTINO.mkdir(parents=True, exist_ok=True)
            
                self.myconexion = sqlite3.connect(self.RUTA_BD)
                self.mycursor = self.myconexion.cursor()
                
                self.mycursor.execute("""
                    CREATE TABLE IF NOT EXISTS USER (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre VARCHAR(50) NOT NULL,
                        apellido VARCHAR(50) NOT NULL,
                        password VARCHAR(50) NOT NULL,
                        addres VARCHAR(50) NOT NULL
                    )
                """)
                
                self.myconexion.commit()
                messagebox.showinfo("BBDD", f"Base de datos creada/conectada en:\n{self.RUTA_BD}")
                
            except sqlite3.Error as err:
                messagebox.showerror("Error BBDD", f"Ocurrió un error al crear la base de datos:\n{err}")
                
            finally:
                #hasattr evalua si existe el atributo (objeto, atributo a buscar dentro del objeto dado)
                if hasattr(self, 'myconexion') and self.myconexion:
                    self.myconexion.close()
        
    def insertBD(self, nombre, apellido, password, addres):
            try:
                self.myconexion = sqlite3.connect(self.RUTA_BD)
                self.mycursor = self.myconexion.cursor()
                
                sql = """
                    INSERT INTO USER (nombre, apellido, password, addres)
                    VALUES (?, ?, ?, ?)
                """
                datos = (nombre, apellido, password, addres)
                
                self.mycursor.execute(sql, datos)
                self.myconexion.commit()
                
                messagebox.showinfo("Éxito", "Usuario registrado correctamente")
                self.limpiar_campos()
                
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Ocurrió un error al insertar datos:\n{e}")
                
            finally:
                if hasattr(self, 'myconexion') and self.myconexion:
                    self.myconexion.close()
                    
    def getDatos(self):
        nombre = self.txt_name.get().strip()
        apellido = self.txt_last_name.get().strip()
        password = self.txt_password.get().strip()
            # El txtArea por defecto simepre hace un salto de linea por eso el "end-1c" para quitar ese caracter
        address = self.text_addres.get("1.0", "end-1c").strip()
        
        if not nombre or not apellido or not password or not address:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return
        return nombre, apellido, password, address
    
    def create_user(self):
        datos = self.getDatos()
        if datos is None:
            return
        nombre, apellido, password, address = datos
        self.insertBD(nombre, apellido, password, address)

    def limpiar_campos(self):
            self.txt_name.delete(0, "end")
            self.txt_last_name.delete(0, "end")
            self.txt_password.delete(0, "end")
            self.text_addres.delete("1.0", "end")
    
    def update(self, nombre, apellido, password, addres, id):
        try:
            self.myconexion = sqlite3.connect(self.RUTA_BD)
            self.mycursor = self.myconexion.cursor()
            datos = (nombre,apellido,password,addres,id)
            sql = """
            UPDATE USER SET 
            nombre=?, apellido=?, password=?, addres=? WHERE id=?
            """
            self.mycursor.execute(sql,datos)
            self.myconexion.commit()
            #Saber si la fila fue afectada
            if self.mycursor.rowcount > 0:
                messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
                self.limpiar_campos()
            else:
                messagebox.showwarning("Advertencia", f"No existe ningún usuario con el ID: {id}")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar datos:\n{e}")
        finally:
            if hasattr (self, 'myconexion') and self.myconexion:
                self.myconexion.close()
    
    def update_user(self):

        datos = self.getDatos()
        if datos is None:
            return
        nombre, apellido, password, address = datos
        self.id=simpledialog.askinteger("Buscar ID","Ingrese el id del usuario")
        if id is None:
            return
        self.update( nombre, apellido, password, address, self.id)
        
        pass

    def read(self):
        id = simpledialog.askinteger("Buscar","Ingrese el Id del Usuario a buscar: ")
        if id is None:
            return
        try:               
            self.myconexion = sqlite3.connect(self.RUTA_BD)
            self.mycursor=self.myconexion.cursor()
            sql="""
            SELECT * FROM USER
            WHERE id=? 
            """
            self.mycursor.execute(sql,(id,))
            usuario=self.mycursor.fetchone()
            if usuario:
                id,nombre, apellido, password, address=usuario
                self.limpiar_campos()
                self.txt_name.insert(0, nombre)
                self.txt_last_name.insert(0, apellido)
                self.txt_password.insert(0, password)
                self.text_addres.insert("1.0", address)
                messagebox.showinfo("Éxito", f"Usuario con ID {id} cargado correctamente.")
                self.myconexion.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar los datos:\n{e}")
        finally:
            if hasattr(self,'myconexion') and self.myconexion:
                self.myconexion.close()
    
    def delete(self):
        try:
            id = simpledialog.askinteger("Buscar ID","Ingrese el Id del Usuario a eliminar: ")
            if id is None:
                return
            self.myconexion = sqlite3.connect(self.RUTA_BD)
            self.mycursor = self.myconexion.cursor()
            sql="""
            DELETE FROM USER WHERE id=? 
            """
            self.mycursor.execute(sql,(id,))
            self.myconexion.commit()
            if self.mycursor.rowcount >0:
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente") 
            else:
                messagebox.showwarning("Advertencia", f"No existe ningún usuario con el ID: {id}")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar al Usuario:\n{e}")
        finally:
            if hasattr(self,'myconexion') and self.myconexion:
                self.myconexion.close()
   
    def about_me(self):
        mensaje = textwrap.dedent("""\
            Soy estudiante de la carrera Ingeniería de Sistemas.
            Actualmente (02/10/2026) me encuentro cursando el V ciclo.
            
            Este es uno de los proyectos que he desarrollado. Puedes visitar
            mis demás repositorios en mi GitHub:
            https://github.com/Lu-Capu/
            
            ...Ah y me gusta una chica de Amauta a la fecha de este proyecto (Esto se editará)
        """)
        messagebox.showinfo("About me", mensaje)

    def licens(self):
        mensaje = textwrap.dedent("""\
            Este es un mini-proyecto desarrollado en Python con la librería Tkinter.
            Se trata de un gestor/CRUD de usuarios respaldado por la base de datos 'SQLite',
            cuyo archivo .db se genera automáticamente en la carpeta 'Descargas'
            para su libre manipulación.
            
            © Todos los derechos reservados por el autor Lu-Capu.
        """)
        messagebox.showinfo("License", mensaje)
    
root= Tk()
root.title("CRUD")
root.geometry("500x400")
root.resizable(False,False)


app = Application(root)
app.mainloop()
