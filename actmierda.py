import numpy as np

sumaUno = 0
a = []
b = []
c = []
xd= 0
filas = int(input("Cuantas filas: "))
columnas = int(input("Cuantas columnas: "))
suma = 0
numero = 0
for i in range (filas):
    a = a+[[]]
    for j in range(columnas):
        x=int(input("Dato para la fila "+str(i)+", columna "+ str(j)+":"))
        sumaUno = sumaUno + x
        suma = sum([x]) + suma
        b.append(suma)
        sum([x]) == 0
        a[i]=a[i]+[x]
print(a)    

for g in range(0):
    for r in range(filas):
        for h in range(columnas):
            xd = a[g][r][h] + a[g][r][h]
            c.append(xd)
print(c)






