import tkinter 
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.geometry("500x300") 
ventana.title("TKINTER")
ventana.config(bg="black")


def suma():
    x = entrada.get()
    y = entrada1.get()
    try:
        valor = float(x)+float(y)
        lbl4["text"] = valor
    except ValueError:
        messagebox.showerror("Error", "Escribir un formato adecuado")

fuente_titulo = ("Arial", 14, "bold")
fuente_texto = ("Arial", 11)
fuente_boton = ("Arial", 11, "bold")

lbl = tkinter.Label(ventana, text="Bienvenido!! Aqui puedes sumar", fg="white", bg="black", font=fuente_titulo)
lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")

lbl1 = tkinter.Label(ventana, text="Ingrese el primer valor", fg="white", bg="black", font=fuente_texto)
lbl1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entrada = tkinter.Entry(ventana, font=fuente_texto)
entrada.grid(row=1, column=1, padx=10, pady=10)

lbl2 = tkinter.Label(ventana, text="Ingresa el segundo valor", fg="white", bg="black", font=fuente_texto)
lbl2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entrada1 = tkinter.Entry(ventana, font=fuente_texto)
entrada1.grid(row=2, column=1, padx=10, pady=10)

lbl3 = tkinter.Label(ventana, text="Resultado", fg="white", bg="black", font=fuente_texto)
lbl3.grid(row=3, column=0, padx=10, pady=20, sticky="w")

lbl4 = tkinter.Label(ventana, text="", fg="white", bg="gray", width="20", height="2", font=("Arial", 12, "bold"))
lbl4.grid(row=4, column=0, padx=10, pady=10, sticky="w")

btn = tkinter.Button(ventana, text="Sumar", command=suma, bg="cyan", fg="black", font=fuente_boton)
btn.grid(row=3, column=1, ipadx=15, ipady=10)

btnsalir = tkinter.Button(ventana, text="Salir", command=ventana.destroy, bg="red", fg="white", font=fuente_boton)
btnsalir.grid(row=4,column=1, sticky="e")

ventana.mainloop()