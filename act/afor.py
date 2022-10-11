global newCantidad,newTotal

newCantidad = 0
newTotal = 0

def deau(cantidad, total):
    print("=======================================================")
    
    nuevoArticulo = input("Desea agregar otro articulo? (Y/N): ")
    
    while nuevoArticulo == "Y":
        main()
    

def main():
    global newCantidad,newTotal

    articulo = int(input("Dame el precio del articulo = "))
    cantidad = int(input("Numero de articulos = "))
    total = articulo * cantidad
    newCantidad = cantidad + newCantidad
    newTotal = total + newTotal
    deau(cantidad, total)
    print("=======================================================")
    print("Numero de articulos comprados = ",newCantidad)
    print("=======================================================")
    print("Total = $",newTotal)

main()



