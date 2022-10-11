lista = []
tam = int(input("Tamaño de la lista = "))

if tam == 0:
    print(lista)

else:

    for i in range (tam):
        n = int(input("Dame un numero = "))
        n = n*n
        lista.append(n)
        n = 0
    lista.sort()
    print(lista)

    
