# 23 - Gestor de usuarios con SQLite

CRUD de usuarios sobre una base de datos SQLite, desde una ventana.

```bash
python 23-GestorBD/main.py
```

## Como funciona

El archivo `.db` **no viene en el repositorio**, se crea la primera vez. Ve a
**Archivo → Crear BD** y el programa genera `Users_BD.db` en
`~/Downloads/MiApp_BD/`.

Ese paso va primero porque la conexion se abre ahi. Si pulsas Create, Read,
Update o Delete sin haberla creado, sale un error de atributo en vez de un aviso
claro, ya que `self.myconexion` todavia no existe.

Despues ya puedes usar las cuatro opciones del menu, cada una en su dialogo.
Cerrar y volver a abrir la app no pierde nada: los datos estan en el archivo.

## Ver la base de datos por fuera

Esto no trae ningun visor, asi que si quieres mirar las tablas o tocar datos por
tu cuenta necesitas instalar uno aparte. El mas usado es
[DB Browser for SQLite](https://sqlitebrowser.org/) y es gratuito.

Abre **Open Database**, elige `~/Downloads/MiApp_BD/Users_BD.db` y ve a la
pestana **Browse Data** para ver la tabla `USER`. Cierra la app antes, porque
mientras este abierta la conexion puede tener cambios sin guardar.

## Un par de detalles

Las consultas van con `?` en vez de pegar el valor dentro del texto de la
consulta. Esa es la parte importante de usar `sqlite3` y no conviene dejarla de
lado.

El menu de la aplicacion es un `Menu` de verdad y no botones sueltos, asi que las
opciones quedan separadas en Crear BD, el CRUD, y License / About me. La tabla se
llama `USER` y guarda `id`, `nombre`, `apellido`, `password` y `addres`.