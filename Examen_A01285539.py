matriz = []
h = 3
encontrados = 0

#Funcion para ingresar datos
def nuevosdatos():
    listaNueva = []
    print("Ingrese su nombre: ")
    nombre = input()
    listaNueva.append(nombre)
    
    print("Ingrese numero de seguro social: ")
    numsocial = int(input())
    listaNueva.append(numsocial)
    
    print("Ingrese su edad: ")
    edad = int(input())
    listaNueva.append(edad)
    tipoSangre = input("Ingrese su tipo de sangre: ")
    listaNueva.append(tipoSangre)
    matriz.append(listaNueva)

#Funcion para consultar por numero de seguro social
def consultadonante():
    print("Ingrese el nombre del donante: ")
    nombre = input()
    for i in range(len(matriz)):
        if nombre in matriz[i]:
            print("Datos del donante: ")
            print("=====================================")
            print("Nombre del donante:",matriz[i][0])
            print("Numero de seguro social:",matriz[i][1])
            print("Edad:",matriz[i][2], "años")
            print("=====================================")

#Funcion para consultar por tipo de sangre
def consultatiposangre():
    global encontrados
    print("Ingrese el tipo de sangre: ")
    tiposangre = input()
    for i in range(len(matriz)):
        if tiposangre in matriz[i]:
            encontrados = encontrados + 1
    print("=====================================")
    print("Hay", encontrados, "donantes con ese tipo de sangre")
    encontrados = 0

#Menu
def menu(nuevosdatos,consultadonante,consultatiposangre):
        print("Bienvenido al sistema de donantes de sangre.")
        print("1. Ingresar datos")
        print("2. Mostrar datos de un donante")
        print("3. Consulta por tipo de sangre")
        print("4. Salir")
        print("Seleccione una opción: ")
        opcion = int(input())
        if opcion == 1:
            nuevosdatos()
            # print(matriz)
            menu(nuevosdatos,consultadonante,consultatiposangre)
        
        elif opcion == 2:
            consultadonante()
            menu(nuevosdatos,consultadonante,consultatiposangre)
        
        elif opcion == 3:
            consultatiposangre()
            menu(nuevosdatos,consultadonante,consultatiposangre)
        
        elif opcion == 4:
            h = 4
            print("Gracias por usar el programa")\
        
        else:
            print("Opción no valida")
            menu(nuevosdatos,consultadonante,consultatiposangre)
            
#Salidas
print(menu(nuevosdatos,consultadonante,consultatiposangre))
