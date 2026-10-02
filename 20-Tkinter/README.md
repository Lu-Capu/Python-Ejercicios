# 20 - Tkinter

Mi primera ventana: pide dos numeros y los suma.

```bash
python 20-Tkinter/main.py
```

Fondo negro, dos `Entry` y un boton que llama a `suma()`. Si el valor no es
numerico sale un `messagebox` en vez de un error en la consola.

Todo se coloca con `grid()`, y el boton de salir llama a `ventana.destroy()`.