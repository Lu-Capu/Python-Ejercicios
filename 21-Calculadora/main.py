import tkinter
from tkinter import messagebox

class Aplication(tkinter.Frame):
    
    
    def __init__(self, master=None ):
        super().__init__(master, width="400", height="300", bg="#222")
        self.master=master
        self.pack()
        self.create_widgets()
    
    def resultado(self):
        expresion = str(self.lbl_resultado["text"]).replace("X", "*")
        try:
            if expresion:
                res = eval(expresion)
                self.lbl_resultado["text"] = res
            else:
                messagebox.showinfo("Dato Curioso", "Debes ingresar números")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero")
        except Exception:
            messagebox.showerror("Error", "Expresión inválida")

    def mostrar(self,num):
        self.lbl_resultado["text"] = str(self.lbl_resultado["text"]) + str(num)

    def clear(self):
        self.lbl_resultado["text"] = ""

    def borrar_uno(self):
        self.lbl_resultado["text"] = str(self.lbl_resultado["text"])[:-1]
    
    def create_widgets(self):
        
        #Elementos reutilizables
        fgB = ("#fff")
        fontC = ("Arial", 12)
        
        self.lblTitulo = tkinter.Label(self, text="Calculadora", fg="black", bg="gray", font=fontC)
        self.lblTitulo.grid(row=0, column=0, ipady=5, sticky="ew", columnspan=4)

        self.lbl_resultado = tkinter.Label(self, fg="black", font=fontC)
        self.lbl_resultado.grid(row=1, column=0, sticky="ew", columnspan=4)

        # Columna 0
        self.btnAC = tkinter.Button(self, text="AC", bg="green", fg=fgB, command=self.clear)
        self.btnAC.grid(row=2, column=0, ipadx=35, ipady=5)
        self.btn7 = tkinter.Button(self, text="7", command=lambda: self.mostrar(7))
        self.btn7.grid(row=3, column=0, ipadx=35, ipady=5)
        self.btn4 = tkinter.Button(self, text="4", command=lambda: self.mostrar(4))
        self.btn4.grid(row=4, column=0, ipadx=35, ipady=5)
        self.btn1 = tkinter.Button(self, text="1", command=lambda: self.mostrar(1))
        self.btn1.grid(row=5, column=0, ipadx=35, ipady=5)
        self.btn0 = tkinter.Button(self, text="0", command=lambda: self.mostrar(0))
        self.btn0.grid(row=6, column=0, ipadx=35, ipady=5)

        # Columna 1
        self.btnP = tkinter.Button(self, text="()", command=lambda: self.mostrar("("))
        self.btnP.grid(row=2, column=1, ipadx=35, ipady=5)
        self.btn8 = tkinter.Button(self, text="8", command=lambda: self.mostrar(8))
        self.btn8.grid(row=3, column=1, ipadx=35, ipady=5)
        self.btn5 = tkinter.Button(self, text="5", command=lambda: self.mostrar(5))
        self.btn5.grid(row=4, column=1, ipadx=35, ipady=5)
        self.btn2 = tkinter.Button(self, text="2", command=lambda: self.mostrar(2))
        self.btn2.grid(row=5, column=1, ipadx=35, ipady=5)
        self.btnPT = tkinter.Button(self, text=".", command=lambda: self.mostrar("."))
        self.btnPT.grid(row=6, column=1, ipadx=35, ipady=5)

        # Columna 2
        self.btnPO = tkinter.Button(self, text="%", command=lambda: self.mostrar("%"))
        self.btnPO.grid(row=2, column=2, ipadx=35, ipady=5)
        self.btn9 = tkinter.Button(self, text="9", command=lambda: self.mostrar(9))
        self.btn9.grid(row=3, column=2, ipadx=35, ipady=5)
        self.btn6 = tkinter.Button(self, text="6", command=lambda: self.mostrar(6))
        self.btn6.grid(row=4, column=2, ipadx=35, ipady=5)
        self.btn3 = tkinter.Button(self, text="3", command=lambda: self.mostrar(3))
        self.btn3.grid(row=5, column=2, ipadx=35, ipady=5)
        self.btn_atras = tkinter.Button(self, text="<-", command=self.borrar_uno)
        self.btn_atras.grid(row=6, column=2, ipadx=35, ipady=5)

        # Columna 3
        self.btn_dividir = tkinter.Button(self, text="/", command=lambda: self.mostrar("/"))
        self.btn_dividir.grid(row=2, column=3, ipadx=35, ipady=5)
        self.btn_multi = tkinter.Button(self, text="X", command=lambda: self.mostrar("X"))
        self.btn_multi.grid(row=3, column=3, ipadx=35, ipady=5)
        self.btn_rest = tkinter.Button(self, text="-", command=lambda: self.mostrar("-"))
        self.btn_rest.grid(row=4, column=3, ipadx=35, ipady=5)
        self.btn_sum = tkinter.Button(self, text="+", command=lambda: self.mostrar("+"))
        self.btn_sum.grid(row=5, column=3, ipadx=35, ipady=5)
        self.btn_igual = tkinter.Button(self, text="=", bg="cyan", fg="black", command=self.resultado)
        self.btn_igual.grid(row=6, column=3, ipadx=35, ipady=5)


root = tkinter.Tk()
app = Aplication(root)

root.title("Titulo")
app.mainloop()