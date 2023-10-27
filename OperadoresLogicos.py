#Conjución
print("Conjunción (AND)")

numeroUno = int(input("Escribre un número mayor a 2 y menor a 5: "))

if numeroUno > 2 and numeroUno < 5:
    print("El número ", numeroUno, " cumple con la condición.\n")
else:
    print("El número ", numeroUno, " NO cumple con la condición.\n")

#Disyunción
print("Disyunción (OR)")

palabra = input("Para cumplir la condición escribe 'si' o 'yes':")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido.\n")
else:
    print("La condición NO se ha cumplido.\n")

#Negación
print("Negación (NOT)")

numeroOne = int(input("Introduce un número igual a 5: "))

if not numeroOne == 5:
    print("\n El número es diferente de cinco y SI cumple la condición.\n")
else:
    print("\n El número es igual a cinco y NO cumple la condición.\n")