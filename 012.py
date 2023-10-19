# Pedir al usuario que ingrese los valores de los dos ángulos
angulo1 = float(input("Ingrese el valor del primer ángulo en grados: "))
angulo2 = float(input("Ingrese el valor del segundo ángulo en grados: "))

# Calcular la suma de los dos ángulos
suma_angulos = angulo1 + angulo2

# Verificar si la suma de los ángulos es mayor o igual a 180
if suma_angulos >= 180:
    print("La suma de los ángulos ingresados es mayor o igual a 180 grados. Ingrese valores válidos.")
else:
    # Calcular el ángulo restante
    angulo_restante = 180 - suma_angulos
    print("El ángulo restante es:", angulo_restante, "grados")
40