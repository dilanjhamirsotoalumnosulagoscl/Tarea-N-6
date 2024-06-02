palabras = []

print("Ingrese palabras (ingrese una palabra vacía para finalizar):")
while True:
    palabra = input()
    if palabra == "":
        break
    palabras.append(palabra)

for palabra in palabras:
    consonantes = 0
    vocales = 0
    for letra in palabra:
        if letra in "aeiouAEIOU":
            vocales += 1
        elif (letra >= "A" and letra <= "Z") or (letra >= "a" and letra <= "z"):
            consonantes += 1
    print("Palabra:", palabra)
    print("Cantidad de vocales:", vocales)
    print("Cantidad de consonantes:", consonantes)
    print()

