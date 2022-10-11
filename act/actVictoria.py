#Billetes que necesito: 200, 100, 50, 20, 5, 1

from dis import disco


def total(productoUno, productoDos, productoTres, productoCuatro, productoCinco, descuento ):
    totalPrice = productoUno + productoDos + productoTres + productoCuatro + productoCinco
    print("Precio sin descuento: $",totalPrice)
    discount = totalPrice-((descuento/100) * totalPrice)
    #Hacer lo de los billetes AQUI
    billetesDoscien = discount%200
    billetesCien = discount%100
    billetesCincu = discount%50
    billetesVeinte = discount%20
    billetesCinco = discount%5
    billetesUno = discount%1

    print("Precio con descuento: $", discount)
    euro = discount*0.049
    print("Precio en Euros: €", euro)
    print("Billetes de $200 = ",billetesDoscien)
    print("Billetes de $100 = ", billetesCien)
    print("Billetes de $50 = ",billetesCincu)
    print("Billetes de $20 = ", billetesVeinte)
    print("Monedas de $5 = ", billetesCinco)
    print("Monedas de $1 = ", billetesUno)



#Main
productoUno = int(input("Precio del primer producto: "))
productoDos = int(input("Precio del segundo producto: "))
productoTres = int(input("Precio del tercer producto: "))
productoCuatro = int(input("Precio del cuarto producto: "))
productoCinco = int(input("Precio del quinto producto: "))
descuento = int(input("Cual fue tu descuento: "))

print(total(productoUno, productoDos, productoTres, productoCuatro, productoCinco, descuento ))
