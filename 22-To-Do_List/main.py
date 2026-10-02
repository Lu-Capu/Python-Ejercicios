from tkinter import Tk, Label, Button, Frame, Entry, messagebox, Listbox, SINGLE, END
from tkinter import ttk


BG = "#1e1e1e"
PANEL = "#252526"
CAMPO = "#2d2d30"
BORDE = "#3c3c3c"
TEXTO = "#f0f0f0"
TEXTO_SUAVE = "#9d9d9d"
ACENTO = "#00bcd4"
ACENTO_HOVER = "#26d0e6"
AMARILLO = "#f5b942"
AMARILLO_HOVER = "#ffcc66"
ROJO = "#e5484d"
ROJO_HOVER = "#ff6369"
SELECCION = "#00838f"
FUENTE = "Segoe UI"


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg=BG)
        self.master = master
        self.pack(fill="both", expand=True)
        self.columnconfigure(0, weight=1)
        self.create_widgets()
        self.tareas = []
        self.centrar_ventana()
    

    def centrar_ventana(self):
        self.master.update_idletasks()

        ancho = self.master.winfo_width()
        alto = self.master.winfo_height()
        #saber el tamaño del escritorio--> winfo_screenwidth() o winfo_screenheight()
        #hallamos las coordenadas
        x = (self.master.winfo_screenwidth() - ancho) // 2
        y = (self.master.winfo_screenheight() - alto) // 2

        self.master.geometry(f"{ancho}x{alto}+{x}+{y}")
        #Aqui le decimos que renderize a partir de estas coordenadas
      
    def listar(self):
        tarea=self.txt_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.lista_tareas.insert(END,tarea)
            self.txt_tarea.delete(0, "end")
        else:
            messagebox.showinfo("Información","No deje el campo vacio")
    
    def eliminar(self):
        if self.tareas:
            seleccion = self.lista_tareas.curselection()
            if seleccion:
                index = seleccion[0]
                del self.tareas[index]
                self.lista_tareas.delete(index)
            else:
                messagebox.showinfo("Información", "Seleccione una tarea")
        else:
            messagebox.showinfo("Información", "Lista vacía\nNo hay nada por eliminar")

        
    def mostrar(self, event=None):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            elemento = self.lista_tareas.get(seleccion[0])
            self.txt_tarea.delete(0, END)
            self.txt_tarea.insert(0, elemento)        
    
    def editar(self):
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            index = seleccion[0]
            nueva_tarea = self.txt_tarea.get()
            if nueva_tarea:
                self.tareas[index] = nueva_tarea

                self.lista_tareas.delete(index)
                self.lista_tareas.insert(index, nueva_tarea)

                self.txt_tarea.delete(0, END)

                messagebox.showinfo("Información", "Se ha editado correctamente")
            else:
                messagebox.showinfo("Información", "Campo de Entrada vacío")

        else:
            messagebox.showinfo("Información", "Seleccione una tarea")


    def _hover(self, boton, normal, resaltado):
        boton.bind("<Enter>", lambda e: boton.config(bg=resaltado))
        boton.bind("<Leave>", lambda e: boton.config(bg=normal))

    def _crear_boton(self, parent, texto, bg, bg_hover, fg, comando):
        boton = Button(
            parent,
            text=texto,
            bg=bg,
            fg=fg,
            font=(FUENTE, 11, "bold"),
            bd=0,
            relief="flat",
            cursor="hand2",
            activebackground=bg_hover,
            activeforeground=fg,
            command=comando
        )
        self._hover(boton, bg, bg_hover)
        return boton
        
    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        
        self.frame_titulo = Frame(self, bg=BG)
        self.frame_titulo.grid(row=0, column=0, columnspan=2, padx=30, pady=(28, 10), sticky="ew")

        self.lbl_titulo = Label(
            self.frame_titulo,
            text="Organiza tus tareas",
            bg=BG,
            fg=TEXTO,
            font=(FUENTE, 22, "bold"),
            anchor="w"
        )
        self.lbl_titulo.pack(fill="x")

        self.lbl_subtitulo = Label(
            self.frame_titulo,
            text="Agrega, edita y elimina tus pendientes",
            bg=BG,
            fg=TEXTO_SUAVE,
            font=(FUENTE, 10),
            anchor="w"
        )
        self.lbl_subtitulo.pack(fill="x", pady=(2, 0))

       
        self.txt_tarea = Entry(
            self, 
            bg=CAMPO, 
            fg=TEXTO, 
            font=(FUENTE, 12),
            bd=0,
            relief="flat",
            insertbackground=TEXTO,
            insertwidth=2,
            highlightthickness=2,
            highlightbackground=BORDE,
            highlightcolor=ACENTO
        )
        self.txt_tarea.grid(row=1, column=0, padx=(30, 10), pady=15, ipady=9, sticky="ew")
        
        self.btn_agregar = self._crear_boton(
            self, "Agregar", ACENTO, ACENTO_HOVER, "#00252b", self.listar
        )
        self.btn_agregar.grid(row=1, column=1, padx=(0, 30), pady=15, ipady=8, ipadx=14, sticky="ew")

        #
        self.frame_lista = Frame(
            self, bg=CAMPO,
            highlightthickness=1, highlightbackground=BORDE
        )
        self.frame_lista.grid(row=2, column=0, columnspan=2, padx=30, pady=(5, 15), sticky="nsew")

        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "Oscuro.Vertical.TScrollbar",
            background="#4a4a4f",
            troughcolor=CAMPO,
            bordercolor=CAMPO,
            lightcolor="#4a4a4f",
            darkcolor="#4a4a4f",
            arrowcolor=TEXTO_SUAVE,
            relief="flat"
        )
        estilo.map(
            "Oscuro.Vertical.TScrollbar",
            background=[("active", "#6a6a70")]
        )

        self.scrollbar = ttk.Scrollbar(
            self.frame_lista, orient="vertical", style="Oscuro.Vertical.TScrollbar"
        )
        self.scrollbar.pack(side="right", fill="y")
              
        self.lista_tareas = Listbox(
            self.frame_lista,
            bg=CAMPO,
            fg=TEXTO,
            font=(FUENTE, 12),
            bd=0,
            highlightthickness=0,
            activestyle="none",
            selectbackground=SELECCION,
            selectforeground="white",
            selectmode=SINGLE,#Permite la selecion solo una vez
            exportselection=False,
            yscrollcommand=self.scrollbar.set #el scroll se mueve al ritmo del panel
        )
        self.lista_tareas.bind("<<ListboxSelect>>", self.mostrar)
        self.lista_tareas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        self.scrollbar.config(command=self.lista_tareas.yview)#Se mueve si se jala con el mouse

        
        self.frame_botones = Frame(self, bg=BG)
        self.frame_botones.grid(row=3, column=0, columnspan=2, padx=30, pady=(0, 28), sticky="ew")
        self.frame_botones.columnconfigure(0, weight=1, uniform="acciones")
        self.frame_botones.columnconfigure(1, weight=1, uniform="acciones")

        self.btn_editar = self._crear_boton(
            self.frame_botones, "Editar", AMARILLO, AMARILLO_HOVER, "#2b2000", self.editar
        )
        self.btn_editar.grid(row=0, column=0, padx=(0, 8), ipady=9, sticky="ew")

        self.btn_eliminar = self._crear_boton(
            self.frame_botones, "Eliminar", ROJO, ROJO_HOVER, "white", self.eliminar
        )
        self.btn_eliminar.grid(row=0, column=1, padx=(8, 0), ipady=9, sticky="ew")
        


root = Tk()
root.title("To-do List")
root.geometry("600x700")
root.resizable(False, False)
root.configure(bg=BG)

app = Application(root)
app.mainloop()