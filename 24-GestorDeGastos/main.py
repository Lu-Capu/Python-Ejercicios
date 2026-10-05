from tkinter import Tk, messagebox
import sqlite3
from ventana import ventanaPrincipal
from database import GastosRepository
from config import RUTA_BD

def main():
    root = Tk()
    root.title("Gestor de gastos")
    root.geometry("1000x600")
    root.resizable(False, False)

    try:
        data = GastosRepository(RUTA_BD)
        data.createBD()
    except sqlite3.Error as e: 
        
        messagebox.showerror("Error de Base de Datos", f"Ha ocurrido un error inesperado:\n{e}")
        root.destroy()
        return
    
    app = ventanaPrincipal(root)
    app.mainloop()

if __name__ == "__main__":
    main()