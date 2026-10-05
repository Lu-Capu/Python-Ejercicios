from tkinter import Label, Frame, Button, Entry, ttk
from config import FUENTE, BACKGASTO, BACKB, BACKENCABEZADO, FG, FG_ENTRY
from ui.button import Botones

class Ventana02(Frame):
    def __init__(self, master=None, ventana_anterior=None):
        super().__init__(master)
        self.master = master
        # Guardamos la referencia de la ventana principal/anterior
        self.ventana_anterior = ventana_anterior
        self.pack(fill="both", expand=True)
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)  
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)      
        self.grid_rowconfigure(2, weight=1)  
        
        self.centrar_ventana()
        self._create_widgets()
        
    
    def back_ventana(self):
        if self.ventana_anterior:
            # 1. Volvemos a hacer visible la ventana anterior
            self.ventana_anterior.deiconify()
        
        # 2. Cerramos/destruimos la ventana actual (Toplevel)
        self.master.destroy()
        
    def _create_widgets(self):
        self._create_encabezado()
        self._create_categoria()
        self._create_filtro()
        self.create_tabla()

    def centrar_ventana(self):
        self.master.update_idletasks()

        ancho = self.master.winfo_width()
        alto = self.master.winfo_height()

        x = (self.master.winfo_screenwidth() - ancho) // 2
        y = (self.master.winfo_screenheight() - alto) // 2

        self.master.geometry(f"{ancho}x{alto}+{x}+{y}")
    
    def clear(self):
        self.txt_nombre.delete(0, "end")
    
    def _create_encabezado(self):

        panel = Frame(self, bg=BACKENCABEZADO)
        panel.grid(row=0,column=0,ipady=10, sticky="nwe", columnspan=4)

        lbl01 = Label(panel, text="Categoría", font=(FUENTE, 18, "bold"), bg=BACKENCABEZADO, fg=FG)
        lbl01.pack(anchor="center", padx=10, pady=(5,0),side="left" )

        btn_back = Button(panel, text="Volver",relief="flat", bd=0 ,command=self.back_ventana)
        btn_back.pack(anchor="center", padx=(0,10), pady=10,side="right", ipady=10, ipadx=10)
        
    def _create_categoria(self):
    
            panel = Frame(self, bg=BACKGASTO)
            panel.grid(row=1,column=0, sticky="nswe")
    
            form = Frame(panel, bg=BACKGASTO, relief="solid", highlightbackground="#00bcd4",highlightthickness=2)
            form.pack(padx=10,pady=10, side="left")
    
            lbl0 = Label(form, text="Nombre ", font=(FUENTE, 12), bg=BACKGASTO, fg=FG)    
            self.txt_nombre = Entry(form, width=30, font=(FUENTE, 12), fg=FG_ENTRY)
    
            lbl0.grid(row=0, column=0, padx=10, pady=10, sticky="w")    
            self.txt_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="we")

    
            # Los botones van juntos en su propio frame, centrado bajo el formulario
            frame_botones = Frame(form, bg=BACKGASTO)
            frame_botones.grid(row=1, column=0, columnspan=3,pady=10, sticky="nswe")
    
            self.buton = Botones(frame_botones, {
                "create" : print("create"),
                "update" : print("update"),
                "delete" : print("delete"),
                "clear"  : self.clear
            })
            self.buton.pack(fill="both", expand=True)    
            
    def _create_filtro(self):
        opciones = ["Sebastian", "Capu", "LuCapu", "Luna"]
        
        panel = Frame(self, bg=BACKGASTO)
        panel.grid(row=2,column=0, sticky="nswe")
        form = Frame(panel, bg=BACKGASTO)    
        form.pack(padx=10,pady=5, side="left")
        
        lbl_nombre=Label(form, text="Nombre: ", bg=BACKGASTO, fg=FG, font=(FUENTE,12))
        self.cboNombre_filtro = ttk.Combobox(form, values=opciones, state="readonly", font=(FUENTE, 12))
        
        lbl_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="nsw")
        self.cboNombre_filtro.grid(row=0, column=1, padx=10, pady=(15, 10), sticky="w")
        self.cboNombre_filtro.current(0)
        
    def create_tabla(self):
        
        panel = Frame(self, bg="gray")
        panel.grid(row=1, column=1, sticky="nsew", rowspan=2)

        self.tabla = ttk.Treeview(panel, columns=("col1"))

        self.tabla.column("#0", width=50, anchor="center")
        self.tabla.column("col1", width=200, anchor="center")


        self.tabla.heading("#0", text="Id", anchor="center")
        self.tabla.heading("col1", text="Nombre", anchor="center")


        scroll = ttk.Scrollbar(panel, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)

        scroll.pack(side="right", fill="y")
        self.tabla.pack(side="left", fill="both", expand=True)
 