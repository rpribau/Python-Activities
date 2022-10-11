cadena = input("Escribe un texto: ")
letra = input("Escribe la letra que deseas conservar: ")
def reemplazar(texto, letra):
    for i in texto:
        if i != letra:
            texto = texto.replace(i,'*')
    return texto
print(reemplazar(cadena,letra))