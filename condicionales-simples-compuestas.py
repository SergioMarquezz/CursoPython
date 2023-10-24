print("Sistema para calcular el promedio de un alumno")
nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")
matematicas = int(input((nombre+ " ¿Cuál es tu calificación en matemáticas?: ")))
quimica = int(input((nombre+ " ¿Cuál es tu calificación en química?: ")))
biologia = int(input((nombre+ " ¿Cuál es tu calificación en biología?: ")))

sumaCalificacion = matematicas + quimica + biologia

calificacion = sumaCalificacion / 3

if calificacion >= 8:
    print("Felicidades "+nombre + " APROBASTE con un promedio de: " + str(calificacion))

else:
    print(nombre + " no has aprobado, tu calificación es de: " + str(calificacion))

print("FIN")

