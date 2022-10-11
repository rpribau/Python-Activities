import re
import pathlib as pat

palabra = input("Dame una palabra: ")

cadenaInvertida = palabra[::-1]
cadenaInvertida = cadenaInvertida.upper()
print(cadenaInvertida)