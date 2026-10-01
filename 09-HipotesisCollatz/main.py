print(
"""
+======================================+
|  ¡Bienvenido!! Hipotesis de Collazt  |
+======================================+
""")
valor= input("Ingresa un numero positivo o escribe 'Fin' para finalizar el programa: ")
if valor.lower() == "fin":
        print("Programa cancelado")
        exit()
try:
        num = int(valor)
except ValueError:
        print("Escribir un numero positivo")
        exit()
if num < 0: 
        print("Escribe un numero mayor a 0") 
        exit()
while num !=1:    
    if num % 2 ==0:
        num = num // 2
    else:
        num = 3 *num + 1
    print(num)


    