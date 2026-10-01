x_valores=[]
print("Ingresa los valores de x uno a uno (escribe 'fin' para finalizar): ")
while True:
    entrada=input("Ingrese los valores de x: ").strip()
    if entrada.lower() == "fin":
            if not x_valores:
                print("Debe de haber 1 dato por lo menos")
                continue
            break
    try:
        x = float(entrada)
        x_valores.append(x)
    except ValueError:
        print("Dar un formato adecuado");
print("---------Resultado---------")
for x in x_valores:
    y=  1/(x+1/(x+1/(x+ 1/x)))
    print(f"Para x {x:>6.2f} ---> El valor de y {y:>8.6f}")