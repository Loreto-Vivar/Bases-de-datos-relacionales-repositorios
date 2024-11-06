#Define la cantidad de puntos de tu línea
length = int(input("Ingrese la longitud de la línea de puntos:"))
direction = input("horizontal(h) o vertical(v):").lower()
if direction =="h":
    print("*" * length)
elif direction=="v" :
    for _ in range(length):
        print("*")
else:
    print("direccion no valida")
