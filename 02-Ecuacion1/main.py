valores_x = []
#Si esta vacio devuelve False
print("Ingresa los valores de x uno a uno (escribe 'fin' para evaluar):")
while True:
    entrada = input("Ingresa un valor: ").strip()
    #El strip elimina espacios en blacno al inico y al final 
    
    if entrada.lower() == "fin":
        if not valores_x:
            print("Debes ingresar al menos un número antes de finalizar.")
            continue
        break
        
    try:
        x = float(entrada)
        valores_x.append(x)
    except ValueError:
        print("Entrada inválida. Ingresa un número o la palabra 'fin'.")

print("\n--- Resultados de la evaluación ---")
for x in valores_x:
    y = 3 * x**3 - 2 * x**2 + 3 * x - 1
    print(f"Para x = {x:>6.2f}  -- ->  y ={y:>8.2f}")
    
