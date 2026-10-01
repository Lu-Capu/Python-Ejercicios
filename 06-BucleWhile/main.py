secret_number=777;
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
while True:
    try:
        number = int(input("Ingresa el numero o 0 para finalizar el programa: "))
        if number == 0:
            print("Programa finalizado")
            exit()
    except ValueError:
        print("Se debe de ingresar un numero")
    if number != secret_number:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    else:
        print("¡Bien hecho, muggle! Eres libre ahora.")
        break
    