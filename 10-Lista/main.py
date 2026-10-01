beatles = []
cont=0
while cont<3:
    nombre = input("Ingrese un integrante: ")
    beatles.append(nombre)
    cont += 1

print("Paso 1:", beatles)
for i in range(len(beatles) -1):
    nombre = input("Ingrese un integrante: ")
    beatles.append(nombre)
    
print("Paso 2:", beatles)
del beatles[-1]
del beatles[-1]

print("Paso 3:", beatles)
nombre = input("Ingrese a otro integrante: ")
beatles.insert(0,nombre)

print("Paso 4: FIN DEL PROGRAMA", beatles)