import time

for i in range(5, 0, -1):
    print(f"\rTiempo restante: {i} Mississippi...  ", end="", flush=True)
    time.sleep(1)

print("\r¡Se acabó el tiempo!             ")
