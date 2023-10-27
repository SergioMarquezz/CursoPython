print("Introduce dos numeros para comparar:\n")
numeroUno = int(input("Introduce el número uno a comparar: "))
numeroDos = int(input("Introduce el número dos a comparar: "))

print("\n Los números para comparar son: ", numeroUno, " y ", numeroDos, "\n")

if numeroUno != numeroDos:
    print("Es diferente....")

if numeroUno > numeroDos:
    print("Es mayor....")

if numeroUno >= numeroDos:
    print("Es mayor o igual....")
