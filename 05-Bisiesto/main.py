while True:
    try:
        anio = int(input("Introduce el año: "))
        break
    except ValueError:
        print("Escribir un año válido en números")

if anio <= 1582:
    print("No se permite este formato (el calendario gregoriano inició en 1582)")
    exit()

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Año bisiesto")
else:
    print("Año común")