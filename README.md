# Python

Coleccion de ejercicios practicos en Python, uno por carpeta y en orden de dificultad.
Cada carpeta es independiente y se ejecuta por separado.

## Como ejecutar

```bash
python 01-Prueba/main.py
```

Las carpetas `20-Tkinter` y `21-Calculadora` abren una ventana grafica.
Los archivos `*.pyw` estan ignorados en `.gitignore` porque son copias de respaldo.

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
`-- 21-Calculadora/main.py
```