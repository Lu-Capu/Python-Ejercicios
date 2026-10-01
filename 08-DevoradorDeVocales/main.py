print(
"""
+================================+
| ¡Bienvenido a un Devorador de !|
|  Palabras(Vocales)!!!          |
+================================+
""")

user_word = input("Ingresa una palabra: ").upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter, end="")
    
### MEDIDOR DE ALTURA DE UNA PIRAME A BASE DE BLOQUES 
print("")
bloques = int(input("Ingresa el número de bloques: "))

altura = 0
necesarios = 1

while bloques >= necesarios:
    bloques -= necesarios
    altura += 1
    necesarios += 1

print("La altura de la pirámide:", altura)