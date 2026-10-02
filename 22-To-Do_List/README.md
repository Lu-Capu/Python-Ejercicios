# 22 - Lista de tareas

Lista de tareas en una ventana, con tema oscuro.

```bash
python 22-To-Do_List/main.py
```

Escribes la tarea en el campo de arriba y le das a Agregar. Para editar,
seleccionas una de la lista, esta se copia al campo, cambias el texto y pulsas
Editar. El boton de la papelera borra la que tenga seleccionada.

Los botones cambian de color al pasar el raton por encima, con `bind` a
`<Enter>` y `<Leave>`. Eso se hizo aparte, en `_hover()`, porque si se repitiera
el `config` en cada boton quedaria el mismo bloque tres veces seguidas.

Los avisos de "campo vacio" o "no hay nada seleccionado" salen por `messagebox`,
para no tener que escribir el texto en un `Label` que se solaparia con la lista.