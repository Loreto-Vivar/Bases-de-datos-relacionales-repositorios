# Solicita al usuario el número de ondas.
waves = int(input("Ingrese el número de ondas: "))

# Genera el patrón de ondas.
for _ in range(3):  # Número de líneas de ondas.
    for _ in range(waves):
        print("~ ", end="")  # Imprime la primera fila de ondas.
    print()  # Salto de línea.
    for _ in range(waves):
        print(" ~", end="")  # Imprime la segunda fila de ondas desplazada.
    print()  # Salto de línea.