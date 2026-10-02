# 21 - Calculadora

Calculadora completa en una ventana, con tema oscuro.

```bash
python 21-Calculadora/main.py
```

Los botones no hacen su operacion por separado: todos pasan por `resultado()` y lo
que hay que calcular sale del texto acumulado en la etiqueta. Como el boton de
multiplicar escribe `x` y Python no entiende eso, antes del `eval` se cambia por
`*`.

Va con `AC`, borrar el ultimo caracter, parentesis y porcentaje. Ojo con el
porcentaje: el boton existe pero `eval` no lo entiende, asi que da "Expresion
invalida". Es el único boton sin terminar.

Los errores se controlan por separado: dividir entre cero tiene su propio aviso
para que se entienda que paso.