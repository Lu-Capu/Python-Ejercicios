from tkinter import Tk
from ventana import ventanaPrincipal

def main():
    root = Tk()
    root.title("Gestor de gastos")
    root.geometry("500x650")
    root.resizable(False, False)
    
    app = ventanaPrincipal(root)
    app.mainloop()

if __name__ == "__main__":
    main()
