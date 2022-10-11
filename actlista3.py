lista = []
suma = 0
numpares = 0
numimpares = 0


cantidad = int(input("Cuantos numeros son? = "))

for i in range(cantidad):
    
    n = int(input("Dame un numero = "))
    
    lista.append(n)
    
    if n%2 == 0 and n/2 == -(n/2):
        numpares = numpares + 1
    elif n%2 == 1 and n/2 == -(n/2):
        numimpares = numimpares + 1

print("Numero de pares = ", numpares)
print("Numeros de impares = ", numimpares)