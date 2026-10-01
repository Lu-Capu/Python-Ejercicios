while True:
    try:
        hora = int(input("Ingrese la hora: "))
        minuto = float(input("Ingrese los minutos: "))
        duracion = float(input("Ingrese el tiempo de duracion en minutos: "))
        break
    except ValueError:
        print("Ingrese un formato adecuado")

if minuto >= 60:
    hora += int(minuto // 60)
    minuto = minuto % 60

print(f"La hora dada es {hora:02d}:{minuto:05.2f}")

minutos_totales = minuto + duracion
horas_extra = int(minutos_totales // 60)
minutos_finales = minutos_totales % 60

hora_final = hora + horas_extra

print(f"El evento finalizará a las {hora_final:02d}:{minutos_finales:05.2f}")

