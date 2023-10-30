print("===============================")
print("¡¡Programa para determinar números pares o impares!!")
print("===============================")

#Un número par es aquel que dividio entre 2 el modulo es igual 0
#Un número impar es aquel que dividio entre 2 el modulo es igual 1

numero = int(input("Introduce un número entero para saber si par o impar "))

resultado = numero % 2
print("El resultado es: ", resultado)

if resultado == 0:
    print("El número ", numero, " es par.")

elif resultado == 1:
    print("El número ", numero, " es impar.")
