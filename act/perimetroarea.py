def areaRect(ancho,longitud):
    totalArea = ancho*longitud
    print("El area es: ", totalArea)

def perimetroRect(ancho,longitud):
    totalPerimetro = (ancho*2) + (longitud*2)
    print("El perimetro es: ", totalPerimetro)



ancho = int(input("Cual es el ancho? "))
longitud = int(input("Cual es la longitud? "))
print(perimetroRect(ancho,longitud))
print(areaRect(ancho, longitud))
