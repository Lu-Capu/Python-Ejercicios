from tkinter import Tk, Label, Frame, Menu, Entry, ttk, Button
from config import FUENTE, BACKGASTO, BACKB, BACKENCABEZADO, FG, FG_ENTRY

class ventanaPrincipal(Frame):
    
    def __init__(self, master=None):
        super().__init__(master, bg=BACKB)
        self.master = master
        self.pack(fill="both", expand=True)   
        
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)  
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)  
                
        self._create_widgets()
        self._centrar_ventana()
    
    def fuction_limpiar(self):
        self.txt_des.delete(0, "end")
        self.txt_fecha.delete(0, "end")
        self.txt_monto.delete(0, "end")
        self.cbo_cat.current(0)
        self.txt_des.focus()
     
    def _create_widgets(self):
        self._create_menu()
        self._create_encabezado()
        self._create_gastos()
        self._create_tabla()
    
    def _centrar_ventana(self):
        self.master.update_idletasks()

        ancho = self.master.winfo_width()
        alto = self.master.winfo_height()

        x = (self.master.winfo_screenwidth() - ancho) // 2
        y = (self.master.winfo_screenheight() - alto) // 2

        self.master.geometry(f"{ancho}x{alto}+{x}+{y}")
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

        panel = Frame(self, bg=BACKENCABEZADO, height=70)
        panel.pack(side="top", fill="x")

        lbl01 = Label(panel, text="Control de gastos", font=(FUENTE, 16), bg=BACKENCABEZADO, fg=FG)
        lbl01.place(x=10, y=10)

        lbl02 = Label(panel, text="Registra y clasifica tus gastos", font=(FUENTE, 10), bg=BACKENCABEZADO, fg=FG)
        lbl02.place(x=10, y=40)
    
    def _create_gastos(self):
        opciones = ["Comida", "Transporte", "Entretenimiento", "Servicios", "Otros"]

        panel = Frame(self, bg=BACKB)
        panel.pack(side="top", fill="x")

        form = Frame(panel, bg=BACKGASTO, relief="solid", highlightbackground="#00bcd4",highlightthickness=2)
        form.pack(pady=15)

        lbl0 = Label(form, text="Descripción: ", font=(FUENTE, 12), bg=BACKGASTO, fg=FG)
        lbl1 = Label(form, text="Monto: ", font=(FUENTE, 12), bg=BACKGASTO, fg=FG)
        lbl2 = Label(form, text="Categoría: ", font=(FUENTE, 12), bg=BACKGASTO, fg=FG)
        lbl3 = Label(form, text="Fecha: ", font=(FUENTE, 12), bg=BACKGASTO, fg=FG)

        self.txt_des = Entry(form, width=30, font=(FUENTE, 12), fg=FG_ENTRY)
        self.txt_monto = Entry(form, width=30, font=(FUENTE, 12), fg=FG_ENTRY)
        self.cbo_cat = ttk.Combobox(form, values=opciones, state="readonly", font=(FUENTE, 12))
        self.cbo_cat.current(0)
        self.txt_fecha = Entry(form, width=30, font=(FUENTE, 12), fg=FG_ENTRY)


        lbl0.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        lbl1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        lbl2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        lbl3.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.txt_des.grid(row=0, column=1, padx=10, pady=10, sticky="we")
        self.txt_monto.grid(row=1, column=1, padx=10, pady=10, sticky="we")
        self.cbo_cat.grid(row=2, column=1, padx=10, pady=10, sticky="we")
        self.txt_fecha.grid(row=3, column=1, padx=10, pady=10, sticky="we")

        # Los botones van juntos en su propio frame, centrado bajo el formulario
        frame_botones = Frame(form, bg=BACKGASTO)
        frame_botones.grid(row=4, column=0, columnspan=2, pady=10)

        self.btnAgregar = Button(frame_botones, text="Agregar", font=(FUENTE, 12), bg="#00bcd4", fg=FG)
        self.btnLimpiar = Button(frame_botones, text="Limpiar", font=(FUENTE, 12), bg="#4a4a4f", fg=FG, 
        command=self.fuction_limpiar)

        self.btnAgregar.grid(row=0, column=0, padx=10)
        self.btnLimpiar.grid(row=0, column=1, padx=10)

    def _create_tabla(self):
        opciones = ["Comida", "Transporte", "Entretenimiento", "Servicios", "Otros"]
        meses = ["Todos", "Mes Anterior"]
        
        panel = Frame(self, bg=BACKB)
        panel.pack(side="top", fill="x")
        form = Frame(panel, bg=BACKGASTO)    
        form.pack(pady=10)
        
        lbl0=Label(form, text="Categoría: ", bg=BACKGASTO, fg=FG, font=(FUENTE,12))
        lbl1=Label(form, text="Mes: ", bg=BACKGASTO, fg=FG, font=(FUENTE,12))
        self.cboCAT_filtro = ttk.Combobox(form, values=opciones, state="readonly", font=(FUENTE, 12))
        self.cboMES_filtro = ttk.Combobox(form, values=meses, state="readonly", font=(FUENTE, 12))
        
        lbl0.grid(row=0, column=0, padx=10, pady=5, sticky="nsw")
        self.cboCAT_filtro.grid(row=0, column=1, padx=10, pady=(15, 10), sticky="w")
        self.cboCAT_filtro.current(0)
        lbl1.grid(row=1, column=0, padx=10, pady=5, sticky="nsw")
        self.cboMES_filtro.grid(row=1, column=1, padx=10, pady=(5, 10), sticky="w")
        self.cboMES_filtro.current(0)
        
        
        lla=Label(form, text="AQUI VA LA TABLA", font=(FUENTE,20))
        lla.grid(row=2, column=1)
    

        