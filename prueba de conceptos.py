# Inicializar variables
inicio = 42
fin = 176
suma = 0

# Calcular la suma de los números comprendidos entre inicio y fin
for numero in range(inicio, fin + 1):
    suma += numero

# Imprimir el resultado
print("La suma de los números entre", inicio, "y", fin, "es:", suma)
