import math

radio = int(input("¿Cual es el radio de la esfera?"));

area = (4*math.pi)*radio**2;
volumen = (4*math.pi*radio**3)/3;

print("El area de la esferea es = ",area);
print("El volumen de la esferea es = ",volumen);