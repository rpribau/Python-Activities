palabraUno = input("Dame una palabra: ")
palabraDos = input("Dame otra palabra: ")

if len(palabraUno) > len(palabraDos):
    print(palabraUno)

elif len(palabraUno) < len(palabraDos):
    print(palabraDos)
else:
    print(palabraUno)
    print(palabraDos)