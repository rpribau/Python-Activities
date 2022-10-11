
costoTotal = 0


def deauu(tipoEnfermedad, dias):
     
        if tipoEnfermedad == 1:
            costoTotal = 2500*dias
            porcentaje = costoTotal + (costoTotal * 0.10)
            print("La tarifa total es = $",porcentaje)
            print("=================================================================================")

        elif tipoEnfermedad == 2:
            costoTotal = 1600*dias
            porcentaje = costoTotal + (costoTotal * 0.10)
            print("La tarifa total es = $",porcentaje)
            print("=================================================================================")

        elif tipoEnfermedad == 3:
            costoTotal = 2000*dias
            porcentaje = costoTotal + (costoTotal * 0.10)
            print("La tarifa total es = $",porcentaje)
            print("=================================================================================")

        elif tipoEnfermedad == 4:
            costoTotal = 3200*dias
            porcentaje = costoTotal + (costoTotal * 0.10)
            print("La tarifa total es = $",porcentaje)
            print("=================================================================================")


def naaa(tipoEnfermedad,dias):
    
    if tipoEnfermedad == 1:
        costoTotal = 2500*dias
        print("La tarifa total es = $",costoTotal)
        print("=================================================================================")
            
    elif tipoEnfermedad == 2:
        costoTotal = 1600*dias
        print("La tarifa total es = $",costoTotal)
        print("=================================================================================")

    elif tipoEnfermedad == 3:
        costoTotal = 2000*dias
        print("La tarifa total es = $",costoTotal)
        print("=================================================================================")
            
    elif tipoEnfermedad == 4:
        costoTotal = 3200*dias
        print("La tarifa total es = $",costoTotal)
        print("=================================================================================")

            

def main():
    tipoEnfermedad = int(input("¿Que tipo de enfermedad es? (Tipo A = 1, Tipo B = 2, Tipo C = 3, Tipo D = 4) "))
    edad = int(input("Dime tu edad = "))
    dias = int(input("Cuantos dias se quedo? "))

    if (edad >=14 and edad<=22):
        print(deauu(tipoEnfermedad,dias))

    else:
        print(naaa(tipoEnfermedad,dias))

main()

repeat = int(input("Desea hacerlo otra vez? (No = 0, Si = 1) "))
print("=================================================================================")

if (repeat == 1):
    main()

else:
    print("Fin del programa.")
    

