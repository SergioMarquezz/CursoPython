print("===============================")
print("¡¡Vacaciones para los trabajadores de RAPPI!!")
print("===============================")

nombreEmpleado = input("Escribe tu nombre completo para recibir vacaciones: ")
claveEmpleado = int(input("Escribe tu clave para identificar tu departamento: "))
aniosEmpleado = int(input("Escribe los años que tienes laborando en la empresa: "))

if claveEmpleado == 1:
    print("Pertenece al departamento de Atención a clientes ")
    if aniosEmpleado == 1 and aniosEmpleado < 2:
        print("El empleado ", nombreEmpleado, " tiene derecho a 6 dias de vacaciones.")

    elif 2 <= aniosEmpleado <= 6:
        print("El empleado ", nombreEmpleado, " tiene derecho a 14 dias de vacaciones.")

    elif aniosEmpleado >= 7:
        print("El empleado ", nombreEmpleado, " tiene derecho a 20 dias de vacaciones.")

    else:
        print("El empleado ", nombreEmpleado, " aun no tiene derecho a vacaciones.")


elif claveEmpleado == 2:
    print("Pertenece al departamento de Logistica ")
    if aniosEmpleado == 1 and aniosEmpleado < 2:
        print("El empleado ", nombreEmpleado, " tiene derecho a 7 dias de vacaciones.")

    elif 2 <= aniosEmpleado <= 6:
        print("El empleado ", nombreEmpleado, " tiene derecho a 15 dias de vacaciones.")

    elif aniosEmpleado >= 7:
        print("El empleado ", nombreEmpleado, " tiene derecho a 22 dias de vacaciones.")

    else:
        print("El empleado ", nombreEmpleado, " aun no tiene derecho a vacaciones.")

elif claveEmpleado == 3:
    print("Pertenece al departamento de Gerencia ")
    if aniosEmpleado == 1 and aniosEmpleado < 2:
        print("El empleado ", nombreEmpleado, " tiene derecho a 10 dias de vacaciones.")

    elif 2 <= aniosEmpleado <= 6:
        print("El empleado ", nombreEmpleado, " tiene derecho a 20 dias de vacaciones.")

    elif aniosEmpleado >= 7:
        print("El empleado ", nombreEmpleado, " tiene derecho a 30 dias de vacaciones.")

    else:
        print("El empleado ", nombreEmpleado, " aun no tiene derecho a vacaciones.")

else:
    print("La clave ", claveEmpleado, "no existe")