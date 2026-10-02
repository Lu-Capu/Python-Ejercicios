from tkinter import Tk

from app import Application
from config import RUTA_BD
from database import UserRepository


def main():
    root = Tk()
    root.title("CRUD")
    root.geometry("500x400")
    root.resizable(False, False)

    repositorio = UserRepository(RUTA_BD)
    app = Application(root, repositorio)
    app.mainloop()


if __name__ == "__main__":
    main()
