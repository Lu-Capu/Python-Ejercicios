import tkinter
from tkinter import messagebox

class Aplication(tkinter.Frame):
    
    def __init__(self, master=None):
        super().__init__(master, bg="#1e1e1e")
        self.master = master
        self.pack(fill="both", expand=True)
        
        #Reseteo de las columnas y row
        for col in range(4):
            self.columnconfigure(col, weight=1)
            

        for row in range(2, 7):
            self.rowconfigure(row, weight=1)

        self.create_widgets()
    
    def resultado(self):
        expresion = str(self.lbl_resultado["text"]).replace("x", "*")
        try:
            if expresion:
                res = eval(expresion)
                self.lbl_resultado["text"] = res
            else:
                messagebox.showinfo("Información", "Debes ingresar números")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero")
        except Exception:
            messagebox.showerror("Error", "Expresión inválida")

    def mostrar(self, num):
        self.lbl_resultado["text"] = str(self.lbl_resultado["text"]) + str(num)

    def clear(self):
        self.lbl_resultado["text"] = ""

    def borrar_uno(self):
        self.lbl_resultado["text"] = str(self.lbl_resultado["text"])[:-1]
    
    def create_widgets(self):
        
        font_num = ("Segoe UI", 12, "bold")
        font_pantalla = ("Segoe UI", 20, "bold")
        
        bg_num = "#333333"      
        bg_op = "#3e3e42"        
        bg_clear = "#e53935"     
        bg_igual = "#00acc1"     
        fg_texto = "#ffffff"     
        
        # 1. Título
        self.lblTitulo = tkinter.Label(
            self, text="Calculadora", fg="#888888", bg="#1e1e1e", font=("Segoe UI", 10)
        )
        self.lblTitulo.grid(row=0, column=0, columnspan=4, pady=(10, 5))
        
        self.lbl_resultado = tkinter.Label(
            self, text="", fg=fg_texto, bg="#2d2d30", font=font_pantalla, anchor="e", padx=15
        )
        self.lbl_resultado.grid(row=1, column=0, columnspan=4, sticky="ew", padx=12, pady=(0, 15), ipady=10)

        botones = [
            # Texto, fila, columna, color_fondo, comando
            ("AC", 2, 0, bg_clear, self.clear),
            ("()", 2, 1, bg_op, lambda: self.mostrar("(")),
            ("%",  2, 2, bg_op, lambda: self.mostrar("%")),
            ("/",  2, 3, bg_op, lambda: self.mostrar("/")),
            
            ("7",  3, 0, bg_num, lambda: self.mostrar(7)),
            ("8",  3, 1, bg_num, lambda: self.mostrar(8)),
            ("9",  3, 2, bg_num, lambda: self.mostrar(9)),
            ("x",  3, 3, bg_op, lambda: self.mostrar("x")),
            
            ("4",  4, 0, bg_num, lambda: self.mostrar(4)),
            ("5",  4, 1, bg_num, lambda: self.mostrar(5)),
            ("6",  4, 2, bg_num, lambda: self.mostrar(6)),
            ("-",  4, 3, bg_op, lambda: self.mostrar("-")),
            
            ("1",  5, 0, bg_num, lambda: self.mostrar(1)),
            ("2",  5, 1, bg_num, lambda: self.mostrar(2)),
            ("3",  5, 2, bg_num, lambda: self.mostrar(3)),
            ("+",  5, 3, bg_op, lambda: self.mostrar("+")),
            
            ("0",  6, 0, bg_num, lambda: self.mostrar(0)),
            (".",  6, 1, bg_num, lambda: self.mostrar(".")),
            ("<-", 6, 2, bg_op, self.borrar_uno),
            ("=",  6, 3, bg_igual, self.resultado),
        ]


        for texto, fila, col, color, cmd in botones:
            btn = tkinter.Button(
                self, 
                text=texto, 
                bg=color, 
                fg=fg_texto, 
                font=font_num, 
                bd=0,                 
                relief="flat",        
                activebackground="#505050", 
                activeforeground=fg_texto,
                command=cmd
            )
            btn.grid(row=fila, column=col, sticky="nsew", padx=3, pady=3)


root = tkinter.Tk()
root.title("Calculadora")
root.geometry("350x450")
root.config(bg="#1e1e1e")

# Ya no estira
root.resizable(False, False)

app = Aplication(root)

root.mainloop()