from tokenize import Double


lista = []
suma = 0
cantidad = int(input("Cuantos numeros son? = "))

for i in range(cantidad):
    n = int(input("Dame el numero = "))
    suma = suma + n
    lista.append(n)

promedio = suma/float(cantidad)
print(lista)
print(promedio)