from tkinter import Label, Frame, Entry, ttk, Toplevel, messagebox
from config import FUENTE, BACKGASTO, BACKB, BACKENCABEZADO, FG, FG_ENTRY, RUTA_BD
from ui.button import Botones
from ui.BarraMenu import BarraMenu
from ventanaCAT import Ventana02
from database import GastosRepository
import sqlite3
from datetime import datetime

class ventanaPrincipal(Frame):

    def __init__(self, master=None):
        super().__init__(master, bg=BACKB)
        self.master = master
        self.pack(fill="both", expand=True)  
         
        self.d = GastosRepository(RUTA_BD)
        self.id_gasto = None

        self.grid_columnconfigure(0, weight=0)   # columna izquierda: solo su ancho
        self.grid_columnconfigure(1, weight=1)   # tabla: absorbe el resto
        self.grid_rowconfigure(0, weight=0)      # encabezado: solo su altura
        self.grid_rowconfigure(1, weight=1)      
        self.grid_rowconfigure(2, weight=1)     
                
        self._create_widgets()
        self.centrar_ventana()

        
        
    def abrir_ventana02(self):
    # 1. Ocultamos la ventana principal
        self.master.withdraw()

        # 2. Creación de la ventana secundaria Toplevel
        top = Toplevel(self.master)
        top.title("Segunda Ventana")
        top.geometry("1000x400")

        # 3. Vinculamos el evento de cerrar (la 'X' de la ventana) para no dejar el proceso colgado
        v2 = Ventana02(master=top, ventana_anterior=self.master, app_principal=self)
        top.protocol("WM_DELETE_WINDOW", v2.back_ventana)    

        
    def fuction_limpiar(self):
        self.txt_des.delete(0, "end")
        self.txt_fecha.delete(0, "end")
        self.txt_monto.delete(0, "end")
        if self.cbo_cat['values']:
            self.cbo_cat.current(0)
        self.id_gasto = None
        self.txt_des.focus()
    
    def getdatos(self):
        descripcion = self.txt_des.get().strip()
        fecha_str = self.txt_fecha.get().strip()
        monto_str = self.txt_monto.get().strip()
        categoria_nombre = self.cbo_cat.get()

        if not descripcion or not fecha_str or not monto_str or not categoria_nombre:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return None

        fecha_obj = None
        for fmt in ("%d/%m/%y", "%d/%m/%Y", "%Y-%m-%d"):
            try:
                fecha_obj = datetime.strptime(fecha_str, fmt)
                break
            except ValueError:
                continue
        if fecha_obj is None:
            messagebox.showerror(
                "Error de fecha", 
                "La fecha debe tener el formato DD/MM/AA o DD/MM/AAAA (Ejemplo: 09/08/26)."
            )
            return None
        fecha_formateada = fecha_obj.strftime("%Y-%m-%d")

        try:
            monto = float(monto_str)
            if monto <= 0:
                messagebox.showwarning("Advertencia", "El monto debe ser mayor a 0.")
                return None
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número válido.")
            return None


        cat_id = self.d.buscarNombre_cat(categoria_nombre)
        if cat_id is None:
            messagebox.showerror("Error", "No se encontró la categoría seleccionada.")
            return None

        return descripcion, fecha_formateada, monto, cat_id
    
    def setdatos(self, descripcion, monto, nommbreCAT, fecha):
        self.fuction_limpiar()
        self.txt_des.insert(0,descripcion)
        self.txt_monto.insert(0,monto)
        self.cbo_cat.set(nommbreCAT)
        try:
            fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
            fecha = fecha_obj.strftime("%d/%m/%y")
        except ValueError:
            pass
        self.txt_fecha.insert(0,fecha)
           
    def _create_widgets(self):
        self._create_menu()
        self._create_encabezado()
        self._create_gastos()
        self._create_filtro()
        self.create_tabla()
        self.mostarCBO()
        self.recorrer_tabla() 
        self.filtro_gasto("Todos")
    
    def _create_menu(self):
        self.barraMenu = BarraMenu(self.master, self.abrir_ventana02)
    
    def centrar_ventana(self):
        self.master.update_idletasks()

        ancho = self.master.winfo_width()
        alto = self.master.winfo_height()

        x = (self.master.winfo_screenwidth() - ancho) // 2
        y = (self.master.winfo_screenheight() - alto) // 2

        self.master.geometry(f"{ancho}x{alto}+{x}+{y}")
    
            
    def _create_encabezado(self):

        panel = Frame(self, bg=BACKENCABEZADO)
        panel.grid(row=0,column=0,ipady=10, sticky="nwe", columnspan=4)

        lbl01 = Label(panel, text="Control de gastos", font=(FUENTE, 18, "bold"), bg=BACKENCABEZADO, fg=FG)
        lbl01.pack(anchor="w", padx=10, pady=(10,0))

        lbl02 = Label(panel, text="Registra y clasifica tus gastos", font=(FUENTE, 12), bg=BACKENCABEZADO, fg=FG)
        lbl02.pack(anchor="w", padx=10)
    
    def _create_gastos(self):

        panel = Frame(self, bg=BACKGASTO)
        panel.grid(row=1,column=0, sticky="nswe")

        form = Frame(panel, bg=BACKGASTO, relief="solid", highlightbackground="#00bcd4",highlightthickness=2)
        form.pack(padx=10,pady=10, side="left")

        lbl0 = Label(form, text="Descripción: ", font=(FUENTE, 12), bg=BACKGASTO, fg=FG)
        lbl1 = Label(form, text="Monto: ", font=(FUENTE, 12), bg=BACKGASTO, fg=FG)
        lbl2 = Label(form, text="Categoría: ", font=(FUENTE, 12), bg=BACKGASTO, fg=FG)
        lbl3 = Label(form, text="Fecha: ", font=(FUENTE, 12), bg=BACKGASTO, fg=FG)

        self.txt_des = Entry(form, width=30, font=(FUENTE, 12), fg=FG_ENTRY)
        self.txt_monto = Entry(form, width=30, font=(FUENTE, 12), fg=FG_ENTRY)
        self.cbo_cat = ttk.Combobox(form, state="readonly", font=(FUENTE, 12))
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
        frame_botones.grid(row=4, column=0, columnspan=3,pady=10, sticky="nswe")

        self.buton = Botones(frame_botones, {
            "create" : self.insertar_gastos,
            "update" : self.actualizar_gasto,
            "delete" : self.eliminar_gastos,
            "clear"  : self.fuction_limpiar
        })
        self.buton.pack(fill="both", expand=True)

    def _create_filtro(self):
        meses = ["Todos", "Meses"]
        
        panel = Frame(self, bg=BACKGASTO)
        panel.grid(row=2,column=0, sticky="nswe")
        form = Frame(panel, bg=BACKGASTO)    
        form.pack(padx=10,pady=5, side="left")
        lbl00 = Label(form,text="Filtro", bg=BACKGASTO, fg=FG, font=(FUENTE,18, "bold"))
        
        lbl0=Label(form, text="Categoría: ", bg=BACKGASTO, fg=FG, font=(FUENTE,12))
        lbl1=Label(form, text="Mes: ", bg=BACKGASTO, fg=FG, font=(FUENTE,12))
        self.cboCAT_filtro = ttk.Combobox(form, state="readonly", font=(FUENTE, 12))
        self.cboMES_filtro = ttk.Combobox(form, values=meses, state="readonly", font=(FUENTE, 12))
        lbl00.grid(row=0, column=0, padx=10, pady=5, sticky="nsw")
        lbl0.grid(row=1, column=0, padx=10, pady=5, sticky="nsw")
        self.cboCAT_filtro.grid(row=1, column=1, padx=10, pady=(15, 10), sticky="w")

        lbl1.grid(row=2, column=0, padx=10, pady=5, sticky="nsw")
        self.cboMES_filtro.grid(row=2, column=1, padx=10, pady=(5, 10), sticky="w")
        self.cboMES_filtro.current(0)
        
        self.cboCAT_filtro.bind("<<ComboboxSelected>>", self.filtro_gasto)
        self.cboMES_filtro.bind("<<ComboboxSelected>>",self.filtrado_meses)
        
        
        lblMonto = Label(form, text="Monto Total: ", bg=BACKGASTO, fg=FG, font=(FUENTE,12))
        self.lblmonto = Label(form, text="", bg=BACKGASTO, fg=FG, font=(FUENTE,16, "bold"))
        lblMonto.grid(row=3, column=0, padx=10, pady=(5, 10), sticky="w")
        self.lblmonto.grid(row=3, column=1, padx=10, pady=(5, 10), sticky="w")
        
    def create_tabla(self):
        
        panel = Frame(self, bg="gray")
        panel.grid(row=1, column=1, sticky="nsew", rowspan=2)

        self.tabla = ttk.Treeview(panel, columns=("col1", "col2", "col3", "col4"))

        self.tabla.column("#0", width=50, anchor="center")
        self.tabla.column("col1", width=200, anchor="w")
        self.tabla.column("col2", width=90, anchor="e")
        self.tabla.column("col3", width=120, anchor="center")
        self.tabla.column("col4", width=100, anchor="center")

        self.tabla.heading("#0", text="Id", anchor="center")
        self.tabla.heading("col1", text="Descripción", anchor="center")
        self.tabla.heading("col2", text="Monto", anchor="center")
        self.tabla.heading("col3", text="Categoría", anchor="center")
        self.tabla.heading("col4", text="Fecha", anchor="center")

        scroll = ttk.Scrollbar(panel, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        scrollx = ttk.Scrollbar(panel, orient="horizontal", command=self.tabla.xview)
        self.tabla.configure(yscrollcommand=scrollx.set)


        scroll.pack(side="right", fill="y")
        scrollx.pack(side="bottom", fill="x")
        self.tabla.pack(side="left", fill="both", expand=True)
        
        self.recorrer_tabla()
        self.tabla.bind("<<TreeviewSelect>>", self.selecion)
        
    def mostarCBO(self):

        datos = self.d.getdatos()
        nombres = [dato[1] for dato in datos]
        
        opciones_filtro = ["Todos"] + nombres
        self.cbo_cat['values'] = nombres
        self.cboCAT_filtro['values'] = opciones_filtro

        if nombres:
            self.cboCAT_filtro.current(0)
            self.cbo_cat.current(0)
        
    def insertar_gastos(self):
        try:
            datos = self.getdatos()
            if datos is None:
                return
            else:
                descripcion,fecha,monto, cat_id = datos
                self.d.insertar_gasto(descripcion, monto, cat_id, fecha)
                messagebox.showinfo("Éxito", "Se ha guardado correctamente los datos")        
                self.fuction_limpiar()
                self.recorrer_tabla() 
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrio un error al insertar datos \n{e}")
            
    def recorrer_tabla(self):
        #INSERTAR DATOS EN TABLA
        datos = self.d.getdatosGASTO()
        #Limpiamos
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        #Agregamos
        for dato in datos:
            nombreCat = self.d.buscarID_cat(dato[3])
            self.tabla.insert("", "end", text=[dato[0]], values=(dato[1], dato[2], nombreCat, dato[4]))
    
    def actualizar_gasto(self):
        try:
            datos = self.getdatos()
            if datos is None:
                return
            else:
                descripcion,fecha,monto,cat_id =datos
                if self.d.actualizar_gasto(descripcion, monto, cat_id, fecha, self.id_gasto):
                    self.recorrer_tabla()
                    self.fuction_limpiar()
                    messagebox.showinfo("Éxito", "Se ha actualizado correctamente los datos")
                else:
                    messagebox.showinfo("Fallo","El campo No fue actualizado")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrio un error al actualizar datos \n{e}")
    
    def selecion(self, event=None):
        cod = self.tabla.selection()
        if not cod:
            return
        item = cod[0]
        descripcion = self.tabla.item(item, "values")[0]
        monto = self.tabla.item(item, "values")[1]
        nombre = self.tabla.item(item, "values")[2]
        fecha = self.tabla.item(item, "values")[3]
        if not nombre:
            messagebox.showinfo("Advertencia","No se pudo encontrar la Categoria selecionada")
            return
        self.setdatos(descripcion, monto, nombre, fecha)
        self.id_gasto = self.tabla.item(item,"text")
    
    def eliminar_gastos(self):
        try:
            if self.id_gasto is None:
                messagebox.showinfo("Advertencia","Selecione una fila a eliminar")
                return
            respuesta = messagebox.askyesno("Confirmar eliminación", 
                                        "¿Está seguro de que desea eliminar este gasto?\nEsta acción no se puede deshacer.")
            cod=self.id_gasto
            if respuesta:
                if self.d.eliminar_gasto(cod):
                    self.recorrer_tabla()
                    self.fuction_limpiar()
                    messagebox.showinfo("Éxito", "Se ha eliminado correctamente los datos") 
                else:
                    messagebox.showinfo("Fallo","El campo No fue eliminado")
            else:
                messagebox.showinfo("Advertencia ","Eliminación cancelada por el usuario.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrio un error al eliminar datos \n{e}")
            
    def filtro_gasto(self, event=None): 
        try:
            nombre = self.cboCAT_filtro.get()
            
            if nombre == "Todos" or not nombre:
                self.recorrer_tabla()
                resultado=self.d.filtroGastoMONTO_TODOS()
                monto = resultado[0] if resultado else None
                if monto is None:
                        monto = 0.0
                valor = f"S/ {monto:.2f}"
                self.lblmonto["text"] = valor
                return
            
            cod = self.d.buscarNombre_cat(nombre)
            if not cod:
                messagebox.showinfo("Advertencia", f"No se encontró la categoría: {nombre}")
                return

            gastos_filtrados = self.d.filtroGasto(cod)
            
            # Limpiar
            for fila in self.tabla.get_children():
                self.tabla.delete(fila)

            for dato in gastos_filtrados:

                self.tabla.insert("", "end", text=dato[0], values=(dato[1], dato[2], dato[3], dato[4]))
            self.monto_filtrado(nombre)

            
        except sqlite3.Error as e:
            messagebox.showerror("Error de Base de Datos", f"Ocurrió un error:\n{e}")
    
    def monto_filtrado(self, nombre):
            resultado = self.d.filtroGastoMONTO(nombre)
            monto = resultado[0] if resultado else None
            if monto is None:
                monto = 0.0
            valor = f"S/ {monto:.2f}"
            self.lblmonto["text"] = valor
            
    def filtrado_meses(self, event=None):
        try:
            mes = self.cboMES_filtro.get().strip()
            if mes=="Meses":
                datos=self.d.filtro_meses_gastos()
                
                for fila in self.tabla.get_children():
                   self.tabla.delete(fila)
                   
                for dato in datos:
                    nombreCat = self.d.buscarID_cat(dato[3])
                    self.tabla.insert("", "end", text=[dato[0]], values=(dato[1], dato[2], nombreCat, dato[4]))
    
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al filtrar los datos:\n{e}")

        
    
