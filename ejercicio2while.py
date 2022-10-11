num = int(input("Teclea un numero: "))

i = 0
suma = num

while(num != 0):
    num = int(input("Teclea un numero: "))
    suma = suma + num
    i = i+1

print("La sumatoria de los numero es = ", suma)
print("Y tecleaste: ", i)
