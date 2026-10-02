# 09 - Hipotesis de Collatz

Aplica la conjetura de Collatz hasta llegar al 1.

```bash
python 09-HipotesisCollatz/main.py
```

La regla es simple: si el numero es par se divide entre 2, y si es impar se le
multiplica por 3 y se le suma 1. Se repite hasta llegar a 1.

Escribe `fin` para cancelar. Casi todo el codigo es validar la entrada antes de
meterse al bucle, que si no el `while` se queda trabajando con algo que no es un
numero.