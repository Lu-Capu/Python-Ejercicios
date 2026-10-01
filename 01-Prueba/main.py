while True:
   try:
    valor = float(input("Ingresa la milla: "))
    break;
   except ValueError:
	    print("Error: Por favor, ingresa un número válido (ejemplo: 5 o 10.5).\n")
kilometros = valor * 1.61
print(f"{valor} Millas en Kilometros es {kilometros:.2f} Km")