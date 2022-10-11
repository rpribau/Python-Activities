import string

sumaUno = 0
a = []
filas = int(input("Cuantas filas: "))
columnas = int(input("Cuantas columnas: "))

for i in range (filas):
    a = a+[[]]
    for j in range(columnas):
        x=int(input("Dato para la fila "+str(i)+", columna "+ str(j)+":"))
        sumaUno = sumaUno + x
        a[i]=a[i]+[x]
print(a)

b=[]
for i in range(filas):
    suma = 0
    for c in range(len(a[i])):
        suma+=a[i][c]
    b.append(suma)
print("Suma de filas: ", b)