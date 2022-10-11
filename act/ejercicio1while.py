def deauu(valorA,valorB):
    
    while(valorA<=valorB):
        
        if valorA%2 == 0:
            print(valorA)
        
        valorA = valorA + 1
    


valorA = int(input("Dame el valor de a = "))
valorB = int(input("Dame el valor de b = "))

print(deauu(valorA,valorB))