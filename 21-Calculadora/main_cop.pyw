import tkinter
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.geometry("400x300")
ventana.title("Titulo")

ventana.config(bg="#222")

back = ("#222")
fgB = ("#fff")

fontC = ("Arial", 12)

def resultado():
    expresion = str(lbl_resultado["text"]).replace("X", "*")
    try:
        if expresion:
            res = eval(expresion)
            lbl_resultado["text"] = res
        else:
            messagebox.showinfo("Dato Curioso", "Debes ingresar números")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero")
    except Exception:
        messagebox.showerror("Error", "Expresión inválida")

def mostrar(num):
    lbl_resultado["text"] = str(lbl_resultado["text"]) + str(num)

def clear():
    lbl_resultado["text"] = ""

def borrar_uno():
    lbl_resultado["text"] = str(lbl_resultado["text"])[:-1]


lblTitulo = tkinter.Label(ventana, text="Calculadora", fg="black", bg="gray", font=fontC)
lblTitulo.grid(row=0, column=0, ipady=5, sticky="ew", columnspan=4)

lbl_resultado = tkinter.Label(ventana, fg="black", font=fontC)
lbl_resultado.grid(row=1, column=0, sticky="ew", columnspan=4)

# Columna 0
btnAC = tkinter.Button(ventana, text="AC", bg="green", fg=fgB, command=clear)
btnAC.grid(row=2, column=0, ipadx=35, ipady=5)
btn7 = tkinter.Button(ventana, text="7", command=lambda: mostrar(7))
btn7.grid(row=3, column=0, ipadx=35, ipady=5)
btn4 = tkinter.Button(ventana, text="4", command=lambda: mostrar(4))
btn4.grid(row=4, column=0, ipadx=35, ipady=5)
btn1 = tkinter.Button(ventana, text="1", command=lambda: mostrar(1))
btn1.grid(row=5, column=0, ipadx=35, ipady=5)
btn0 = tkinter.Button(ventana, text="0", command=lambda: mostrar(0))
btn0.grid(row=6, column=0, ipadx=35, ipady=5)

# Columna 1
btnP = tkinter.Button(ventana, text="()", command=lambda: mostrar("("))
btnP.grid(row=2, column=1, ipadx=35, ipady=5)
btn8 = tkinter.Button(ventana, text="8", command=lambda: mostrar(8))
btn8.grid(row=3, column=1, ipadx=35, ipady=5)
btn5 = tkinter.Button(ventana, text="5", command=lambda: mostrar(5))
btn5.grid(row=4, column=1, ipadx=35, ipady=5)
btn2 = tkinter.Button(ventana, text="2", command=lambda: mostrar(2))
btn2.grid(row=5, column=1, ipadx=35, ipady=5)
btnPT = tkinter.Button(ventana, text=".", command=lambda: mostrar("."))
btnPT.grid(row=6, column=1, ipadx=35, ipady=5)

# Columna 2
btnPO = tkinter.Button(ventana, text="%", command=lambda: mostrar("%"))
btnPO.grid(row=2, column=2, ipadx=35, ipady=5)
btn9 = tkinter.Button(ventana, text="9", command=lambda: mostrar(9))
btn9.grid(row=3, column=2, ipadx=35, ipady=5)
btn6 = tkinter.Button(ventana, text="6", command=lambda: mostrar(6))
btn6.grid(row=4, column=2, ipadx=35, ipady=5)
btn3 = tkinter.Button(ventana, text="3", command=lambda: mostrar(3))
btn3.grid(row=5, column=2, ipadx=35, ipady=5)
btn_atras = tkinter.Button(ventana, text="<-", command=borrar_uno)
btn_atras.grid(row=6, column=2, ipadx=35, ipady=5)

# Columna 3
btn_dividir = tkinter.Button(ventana, text="/", command=lambda: mostrar("/"))
btn_dividir.grid(row=2, column=3, ipadx=35, ipady=5)
btn_multi = tkinter.Button(ventana, text="X", command=lambda: mostrar("X"))
btn_multi.grid(row=3, column=3, ipadx=35, ipady=5)
btn_rest = tkinter.Button(ventana, text="-", command=lambda: mostrar("-"))
btn_rest.grid(row=4, column=3, ipadx=35, ipady=5)
btn_sum = tkinter.Button(ventana, text="+", command=lambda: mostrar("+"))
btn_sum.grid(row=5, column=3, ipadx=35, ipady=5)
btn_igual = tkinter.Button(ventana, text="=", bg="cyan", fg="black", command=resultado)
btn_igual.grid(row=6, column=3, ipadx=35, ipady=5)

ventana.mainloop()