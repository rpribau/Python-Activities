a = 0
tam = 0
while tam == 0:
    lista = []
    tam = int(input("Tamaño de la lista = "))

for i in range(tam):
    n = int(input("Dame un numero = "))
    lista.append(n)
    

lista.sort()
lista.reverse()
for j in range(1,tam+1,1):
    print("Lista[-",j,"] = ",lista[a])
    a = a + 1
    
lista.sort()
print(lista[tam-1])
print(lista[0])
print(lista)
    


    


