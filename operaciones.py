#Funcion suma

def sum():
    numUno = int(input("¿Cual es el primer numero? "));
    numDos = int(input("¿Cual es el segundo numero? "));
    suma = numUno + numDos;
    print("Tu suma es = ",suma);
    print("====================================")

def sub():
    numUno = int(input("¿Cual es el primer numero? "));
    numDos = int(input("¿Cual es el segundo numero? "));
    resta = numUno - numDos;
    print("Tu resta es = ",resta);
    print("====================================")

def mul():
    numUno = int(input("¿Cual es el primer numero? "));
    numDos = int(input("¿Cual es el segundo numero? "));
    multi = numUno * numDos;
    print("Tu multiplicacion es = ",multi);
    print("====================================")

def divicion():
    numUno = int(input("¿Cual es el primer numero? "));
    numDos = int(input("¿Cual es el segundo numero? "));
    div = numUno / numDos;
    print("Tu division es = ",div);
    print("====================================")


#main

sum();
sub();
mul();
divicion();
