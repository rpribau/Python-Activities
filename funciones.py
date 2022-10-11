def saludar (nombre, edad):
    mensaje = ("Bienvenido "+ nombre + " tienes "+ edad + " años")
    return mensaje

#main

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
print(saludar(nombre,edad))