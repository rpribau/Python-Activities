def total(horas, min,segundos):

    totalHoras = horas * 3600
    totalMin = min * 60
    totalSeg = segundos
    
    resultado = totalHoras+totalMin+totalSeg

    print(horas," horas ", min, " minutos ", segundos, " segundos son: ", resultado, " segundos")


horas = int(input("Cuantas horas son? "))
min = int(input("Cuantos minutos son? "))
segundos = int(input("Cuantos segundos son? "))

print(total(horas,min,segundos))