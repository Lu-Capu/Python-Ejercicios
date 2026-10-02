# 08 - Devorador de vocales

Quita las vocales de una palabra y despues calcula una piramide de bloques.

```bash
python 08-DevoradorDeVocales/main.py
```

La primera parte pasa la palabra a mayusculas y salta las vocales con
`continue`. La segunda va gastando bloques de 1, 2, 3, 4... y cuenta cuantas
filas completas se pueden armar.

Con 10 bloques salen 4 filas, porque 1 + 2 + 3 + 4 = 10 y para la quinta haria
falta uno mas.