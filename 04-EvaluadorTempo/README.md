# 04 - Evaluador de tiempo

Dice a que hora termina un evento, sumando su duracion a la hora que le indiques.

```bash
python 04-EvaluadorTempo/main.py
```

Ejemplo: si el evento es a las `09:30` y dura `45` minutos, el resultado es
`10:15`.

Los minutos se leen como `float` porque el enunciado los daba en ese formato. Si
te pasas de 60, el `//` y el `%` reparten la hora antes de calcular. Ojo con que
el formato de salida es `HH:MM.SS`, no `HH:MM`.