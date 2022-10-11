import numpy as np
import random as rnd

""" 
Cosas que faltan:
- Falta integrar lo de dos jugadores
- Poder elegir el tablero (en caso de poner numero impar marcar ERROR)
- Dormir...

INSTRUCCIONES:

Este memorama es en base de matrices utilizando la libreria de numpy para crear matrices de manera mas sencilla y la libreria random para poder asignar
cada carta. 
    - Cada carta es representada por un numero.
    - Solo tienes 3 oportunidades de fallar (al menos en este programa. A futuro se va cambiar debido a la implementación de dos jugadores.)
    - Los ceros que se muestran al iniciar el programa representan las cartas volteadas.
    Ejem:

    [[0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0]]

    - Para poder elejir una carta usamos en base a la linea y columna en la que se encuentra. Es decir:

                    Columnas:
                    0 1 2 3 4 5 6 7 8 9

Fila 0            [[0 0 0 0 0 0 0 0 0 0]
Fila 1            [0 0 0 0 0 0 0 0 0 0]
Fila 2            [0 0 0 0 0 0 0 0 0 0]
Fila 3            [0 0 0 0 0 0 0 0 0 0]
Fila 4            [0 0 0 0 0 0 0 0 0 0]
Fila 5            [0 0 0 0 0 0 0 0 0 0]
Fila 6            [0 0 0 0 0 0 0 0 0 0]
Fila 7            [0 0 0 0 0 0 0 0 0 0]
Fila 8            [0 0 0 0 0 0 0 0 0 0]
Fila 9            [0 0 0 0 0 0 0 0 0 0]]


    - Cuando una carta sea distinta esto mostrara:

>   Fila de la ficha 1:0
>   Columna de la ficha 1:4
>   Fila de la ficha 2: 0
>   Columna de la ficha 2: 6

Las fichas son diferentes =  31 7
Estado del juego:
[[0 0 0 0 0 0 0 0 0 0]
Las fichas son diferentes =  30 46
Estado del juego:
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]

 """



def tableroparejas(n):
    
    fichasUnicas = (n*n)//2
    tablero = np.zeros(shape=(n,n),dtype =int)

    i = 1
    while (i <= fichasUnicas):
        filaUno = int(rnd.random()*n)+0
        columnaUno = int(rnd.random()*n)+0
        
        while (tablero[filaUno,columnaUno]!=0):
            filaUno = int(rnd.random()*n)+0
            columnaUno = int(rnd.random()*n)+0
        tablero[filaUno,columnaUno] = i
        filaDos = int(rnd.random()*n)+0
        columnaDos = int(rnd.random()*n)+0
        
        while (tablero[filaDos,columnaDos]!=0):
            filaDos = int(rnd.random()*n)+0
            columnaDos = int(rnd.random()*n)+0
        tablero[filaDos,columnaDos] = i
        i = i + 1
    return(tablero)



#Modificar el tamaño del memorama (SOLO NUMEROS PARES)
n = 1
while n == 1:
    n = int(input("Dame un numero solo (Solo pares) = "))
    nuevaN = n%2
    if nuevaN == 1:
        print("Error, ingresa un numero PAR.")


#Tablero
tablero = tableroparejas(n)
descubiertas = np.zeros(shape=(n,n),dtype=int)
equivocado = 0
encontrado = 0
while (equivocado<3 and encontrado<(n*n)):
    
    print("Estado del juego:")
    print(descubiertas)

    filaUno = int(input("Fila de la ficha 1:"))
    columnaUno = int(input("Columna de la ficha 1:"))

    while (descubiertas[filaUno,columnaUno]!=0):
        filaUno = int(input('Fila de la ficha 1:'))
        columnaUno = int(input('Columna de la ficha 1:'))

    filaDos = int(input("Fila de la ficha 2: "))
    columnaDos = int(input("Columna de la ficha 2: "))
    while (descubiertas[filaDos,columnaDos]!=0):
        filaDos = int(input("Fila de la ficha 2: "))
        columnaDos = int(input("Columna de la ficha 2: "))

    ficha1 = tablero[filaUno,columnaUno]
    ficha2 = tablero[filaDos,columnaDos]

    if ficha1==ficha2:
        descubiertas[filaUno,columnaUno] = ficha1
        descubiertas[filaDos,columnaDos] = ficha2
        encontrado = encontrado + 2
        print('Haz encontrado una pareja! = ',ficha1,ficha2)
    else:
        equivocado = equivocado + 1
        print('Las fichas son diferentes = ',ficha1,ficha2)

#Main
print("Solucion del tablero:")
print(tablero)
print("Estado del juego:")
print(descubiertas)
if encontrado==(n*n):
    print("Muy bien..!! Encontraste todas las fichas. ")
else:
    print("Te haz equivocado tres veces... Fin del juego. ")
    print("Fichas descubiertas:", encontrado)