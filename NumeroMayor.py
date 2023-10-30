print("===============================")
print("¡¡Programa para saber cual es el número mas grande de los 3!!")
print("===============================")

numeroUno = int(input("Escribe el primer número: "))
numeroDos = int(input("Escribe el segundo número: "))
numeroTres = int(input("Escribe el tercer número: "))

if numeroUno > numeroDos and numeroUno > numeroTres:
    print("El número ", numeroUno, "es el mas grade de los tres.")
else:
    if numeroDos > numeroTres:
        print("El número ", numeroDos, "es el mas grade de los tres.")
    else:
        print("El número ", numeroTres, "es el mas grade de los tres.")