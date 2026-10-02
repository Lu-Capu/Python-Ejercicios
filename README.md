# Python

Coleccion de ejercicios practicos en Python, uno por carpeta y en orden de dificultad.
Cada carpeta es independiente y se ejecuta por separado.

## Como ejecutar

```bash
python 01-Prueba/main.py
```

Las carpetas `20-Tkinter`, `21-Calculadora`, `22-To-Do_List` y `23-GestorBD`
abren una ventana grafica. Los archivos `*.pyw` estan ignorados en `.gitignore`
porque son copias de respaldo.

`23-GestorBD` crea la base de datos `Users_BD.db` en la carpeta `Downloads`
cuando pulsas **Archivo → Crear BD**; todavia hay que ejecutar ese paso antes de
usar los botones del CRUD.

### Ver o modificar la base de datos

El archivo `.db` se genera solo, asi que no hay nada que instalar para usar el
CRUD. Pero si quieres mirar las tablas o cambiar datos por tu cuenta, el
proyecto **no incluye ningun visor**: instala
[DB Browser for SQLite](https://sqlitebrowser.org/), que es el mas usado y es
gratuito. Abre **Open Database**, elige
`~/Downloads/MiApp_BD/Users_BD.db`, y en la pestana **Browse Data** veras la
tabla `USER`. Recuerda cerrar la app antes, porque el cierre de conexion y los
`commit` ocurren al terminar cada operacion.

## Ejercicios

| # | Carpeta | Ejercicio | Que hace | Concepts | Archivo |
|---|---------|-----------|----------|----------|---------|
| 01 | `01-Prueba` | Conversor de millas | Convierte millas a kilometros con validacion de entrada | `input`, `while`, `try/except`, `float`, f-strings | `main.py` |
| 02 | `02-Ecuacion1` | Ecuacion de primer grado | Evalua `y = 3x³ - 2x² + 3x - 1` para varios valores de x | listas, `append`, `.strip()`, control de flujo | `main.py` |
| 03 | `03-Ecuacion2` | Ecuacion anidada | Evalua una fraccion continua de fracciones | listas, operadores, formato `>6.2f` | `main.py` |
| 04 | `04-EvaluadorTiempo` | Evaluador de tiempo | Suma una duracion a una hora y normaliza a hh:mm | `int`, `float`, `//`, `%`, `:02d` | `main.py` |
| 05 | `05-Bisiesto` | Anio bisiesto | Determina si un anio es bisiesto (regla gregoriana) | condicionales, `and/or`, `%`, `exit()` | `main.py` |
| 06 | `06-BucleWhile` | Adivina el numero | Juego de adivinar un numero secreto con `while` | `while`, `break`, `exit()`, texto multilinea | `main.py` |
| 07 | `07-CuentaRegresiva` | Cuenta regresiva | Cuenta de 5 a 1 en la misma linea | `for`, `range()`, `time.sleep()`, `end=` | `main.py` |
| 08 | `08-DevoradorDeVocales` | Devorador de vocales + piramide | Elimina vocales de una palabra y calcula altura de piramide | `continue`, `for`, `in`, `while` acumulado | `main.py` |
| 09 | `09-HipotesisCollatz` | Conjetura de Collatz | Aplica la conjetura hasta llegar a 1 | `while`, `%`, `//`, `try/except` | `main.py` |
| 10 | `10-Lista` | Manipulacion de listas | Anade, elimina e inserta integrantes de una lista | `append`, `del`, `insert`, `len`, `range` | `main.py` |
| 20 | `20-Tkinter` | GUI Suma | Ventana con dos campos que suma dos valores | `tkinter`, `grid()`, `Entry`, `Button`, `messagebox` | `main.py` |
| 21 | `21-Calculadora` | Calculadora GUI | Calculadora completa con teclado numerico | `tkinter`, `lambda`, `eval`, `grid`, `messagebox` | `main.py` |
| 22 | `22-To-Do_List` | Lista de tareas GUI | Agrega, edita y elimina tareas en una ventana con tema oscuro | `tkinter`, `Listbox`, `ttk.Style`, `Frame`, `grid()`, eventos `<Enter>` / `<Leave>` | `main.py` |
| 23 | `23-GestorBD` | CRUD de usuarios con SQLite | Gestor de usuarios sobre una base de datos SQLite creada en tiempo de ejecucion | `sqlite3`, `tkinter`, `Menu`, `simpledialog`, consultas parametrizadas, `pathlib` | `main.py` |

## Estructura

```
Python/
|-- README.md
|-- .gitignore
|-- 01-Prueba/main.py
|-- 02-Ecuacion1/main.py
|-- 03-Ecuacion2/main.py
|-- 04-EvaluadorTiempo/main.py
|-- 05-Bisiesto/main.py
|-- 06-BucleWhile/main.py
|-- 07-CuentaRegresiva/main.py
|-- 08-DevoradorDeVocales/main.py
|-- 09-HipotesisCollatz/main.py
|-- 10-Lista/main.py
|-- 20-Tkinter/main.py
|-- 21-Calculadora/main.py
|-- 22-To-Do_List/main.py
`-- 23-GestorBD/main.py
```