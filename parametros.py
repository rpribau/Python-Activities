#Funcion suma

def sum(numUno, numDos):
    suma = numUno + numDos;
    print("Tu suma es = ",suma);
    print("====================================")

def sub(numUno, numDos):
    resta = numUno - numDos;
    print("Tu resta es = ",resta);
    print("====================================")

def mul(numUno, numDos):
    multi = numUno * numDos;
    print("Tu multiplicacion es = ",multi);
    print("====================================")

def divicion(numUno, numDos):
    div = numUno / numDos;
    print("Tu division es = ",div);
    print("====================================")


#main

numUno = int(input("¿Cual es el primer numero? "));
numDos = int(input("¿Cual es el segundo numero? "));
sum(numUno, numDos);
sub(numUno, numDos);
mul(numUno, numDos);
divicion(numUno, numDos);
