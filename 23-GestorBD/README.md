# 23 - Gestor de usuarios

CRUD de usuarios sobre SQLite, desde una ventana.

```bash
python 23-GestorBD/main.py
```

La base de datos no viene en el repositorio. Ve a **Archivo → Crear BD** y se
genera `Users_BD.db` en `~/Downloads/MiApp_BD/`.

Para verla por fuera necesitas un visor aparte, por ejemplo
[DB Browser for SQLite](https://sqlitebrowser.org/). Abres ese archivo en
**Open Database** y la ves en la pestana **Browse Data**.

## Como esta repartido

```
23-GestorBD/
|-- main.py        punto de entrada
|-- config.py      fuentes, colores y ruta de la base de datos
|-- database.py    UserRepository: todo lo que habla con SQLite
|-- textos.py      About me y License
`-- ui/
    |-- encabezado.py
    |-- formulario.py
    |-- botones.py
    `-- menu.py
```

`database.py` no importa nada de Tkinter, asi que se puede probar sin abrir la
ventana:

```python
from database import UserRepository

repo = UserRepository("Users_BD.db")
repo.crear_bd()
repo.insertar("Ana", "Lopez", "1234", "Calle 1")
repo.buscar_por_id(1)
```