#Asiganación de String
print("ASIGNACIÓN")
mensajeAsignacion = "Hola"
mensajeAsignacion += " "
mensajeAsignacion += "Sergio Alberto"
print(mensajeAsignacion)

#Concatenación de String
print("CONCATENACIÓN")
mensajeConcatenacion = "Hola"
mensajeEspacio = " "
mensajeNombre = "Alberto Marquez"
print(mensajeConcatenacion + mensajeEspacio + mensajeNombre)

numeroUno = 4
numeroDos = 6
resultado = numeroUno + numeroDos
resultado = str(resultado) #Se convierte de entero a string
print("El resultado de la suma es: " + resultado)

#Busqueda de String
print("BUSCAR STRING")
mensajeBuscar = "Hola Sergio Alberto"
mensajeSubcadena = mensajeBuscar.find("Alberto")
print(mensajeSubcadena) #Imprime 12

#Extracción de String
print("EXTRAER STRING")
mensajeExtraer = "Hola Sergio Alberto"
mensajeSubExtraer = mensajeExtraer[12:19]
print(mensajeSubExtraer)

#Comparación de String
print("COMPARAR STRING")
mensajeUno = "Hola"
mensajeDos = "Hola"
mensajeResultado = mensajeUno == mensajeDos 
print(mensajeResultado)
