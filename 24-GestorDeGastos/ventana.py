from tkinter import Tk, Label, Frame, Menu, Entry, ttk, Button
from config import FUENTE, BACKGASTO

class ventanaPrincipal(Frame):
    
    def __init__(self, master=None):
        super().__init__(master, bg="#222222")
        self.master = master
        self.pack(fill="both", expand=True)   
        
        for i in range(2):
            self.grid_columnconfigure(i, weight=1)  
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)  
                
        self._create_widgets()
        self._centrar_ventana()
        


    def _centrar_ventana(self):
        self.master.update_idletasks()

        ancho = self.master.winfo_width()
        alto = self.master.winfo_height()

        x = (self.master.winfo_screenwidth() - ancho) // 2
        y = (self.master.winfo_screenheight() - alto) // 2

        self.master.geometry(f"{ancho}x{alto}+{x}+{y}")

    def _create_widgets(self):
        self._create_menu()
        self._create_encabezado()
        self._create_gastos()
    
    def _create_menu(self):
        barra_menu = Menu(self.master)

        self.menu_archivo = Menu(barra_menu, tearoff=0, font=(FUENTE, 9))
        self.menu_archivo.add_command(label="Salir", command=self.master.quit)

        self.menu_cat = Menu(barra_menu, tearoff=0, font=(FUENTE, 9))
        self.menu_cat.add_command(label="Visitar")

        self.menu_help = Menu(barra_menu, tearoff=0, font=(FUENTE, 9))
        self.menu_help.add_command(label="License")
        self.menu_help.add_command(label="About me")

        barra_menu.add_cascade(label="   Archivo ", menu=self.menu_archivo, font=(FUENTE, 11))
        barra_menu.add_cascade(label="   Categorías    ", menu=self.menu_cat, font=(FUENTE, 11))
        barra_menu.add_cascade(label="   Ayuda   ", menu=self.menu_help, font=(FUENTE, 11))

        self.master.config(menu=barra_menu)
            
    def _create_encabezado(self):

        panel = Frame(self, bg="#ded0dd", height=70)
        panel.pack(side="top", fill="x")

        lbl01 = Label(panel, text="Control de gastos", font=(FUENTE, 16), bg="#ded0dd")
        lbl01.place(x=10, y=10)

        lbl02 = Label(panel, text="Registra y clasifica tus gastos", font=(FUENTE, 10), bg="#ded0dd")
        lbl02.place(x=10, y=40)
    
    def _create_gastos(self):
        opciones = ["Comida", "Transporte", "Entretenimiento", "Servicios", "Otros"]        
        panel = Frame(self, bg=BACKGASTO, height=200)
        panel.pack(side="top", fill="x")
        lbl0=Label(panel,text="Descripción", font=(FUENTE,12), bg=BACKGASTO)
        lbl1=Label(panel,text="Monto", font=(FUENTE,12), bg=BACKGASTO)
        lbl2=Label(panel,text="Categoría", font=(FUENTE,12), bg=BACKGASTO)
        lbl3=Label(panel,text="Fecha", font=(FUENTE,12), bg=BACKGASTO)
        
        self.txt_des = Entry(panel, font=(FUENTE,12))
        self.txt_monto = Entry(panel, font=(FUENTE,12))
        self.cbo_cat = ttk.Combobox(panel, values=opciones, state="readonly", font=(FUENTE,12))
        self.cbo_cat.current(0)
        self.txt_fecha = Entry(panel, font=(FUENTE,12))
        
        lbl0.grid(row=0,column=0, padx=10, pady=10, sticky="nswe")
        lbl1.grid(row=1,column=0, padx=10, pady=10, sticky="nswe")
        lbl2.grid(row=2,column=0, padx=10, pady=10, sticky="nswe")
        lbl3.grid(row=3,column=0, padx=10, pady=10, sticky="nswe")
        
        self.txt_des.grid(row=0, column=1, padx=10, pady=10, sticky="wnswe")
        self.txt_monto.grid(row=1, column=1, padx=10, pady=10, sticky="wnswe")
        self.cbo_cat.grid(row=2, column=1, padx=10, pady=10, sticky="wnswe")
        self.txt_fecha.grid(row=3, column=1, padx=10, pady=10, sticky="wnswe")
        
        self.btnAgregar = Button(panel, text="Agregar", font=(FUENTE,12), bg="cyan", fg="black")
        self.btnLimpiar = Button(panel, text="Limpiar", font=(FUENTE,12), bg="gray", fg="black")
        
        self.btnAgregar.grid(row=4, column=0, padx=10, pady=10 , sticky="nwse")
        self.btnLimpiar.grid(row=4, column=1, padx=10, pady=10 , sticky="nwse")
        


