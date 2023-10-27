print("================")
print("Conversor")
print("================ \n")

print("Menu de Opciones: \n")
print("Presiona 1 para covertir de número a palabra.")
print("Presiona 2 para covertir de palabra a número.  \n")

opcion = int(input("¿Cúal es tu opción deseada?:"))

if opcion == 1:
    print("\n Coversor de número a palabra. \n")

    opcionUno = int(input("¿Cúal es el número que deseas convertir a palabra?:"))

    if opcionUno == 1:
        print("El número es 'UNO'")

    elif opcionUno == 2:
        print("El número es 'DOS'")

    elif opcionUno == 3:
        print("El número es 'TRES'")

    elif opcionUno == 4:
        print("El número es 'CUATRO'")

    elif opcionUno == 5:
        print("El número es 'CINCO'")

    else:
        print("El numero "+str(opcionUno)+" no esta registrado")

elif opcion == 2:
    print("\n Coversor de palabra número. \n")

    opcionDos = input("¿Cúal es la palabra que deseas convertir a número?:")
    opcionDos = opcionDos.lower() #Convierte a minusculas

    if opcionDos == "uno":
        print("El numero es '1'")

    elif opcionDos == "dos":
        print("El numero es '2'")

    elif opcionDos == "tres":
        print("El numero es '3'")

    elif opcionDos == "cuatro":
        print("El numero es '4'")

    elif opcionDos == "cinco":
        print("El numero es '5'")

    else:
        print("El numero " +opcionDos+ " no esta registrado")

else:
    print("La opción no esta disponible.")

print("Fin del programa.")
