# Pedir al usuario que ingrese un valor para num1
num1 = float(input("Ingrese un valor para num1: "))

# Pedir al usuario que ingrese un valor para num2
num2 = float(input("Ingrese un valor para num2: "))

# Mostrar por pantalla el valor de num1 y num2
print("Valores originales:")
print("num1 =", num1)
print("num2 =", num2)

# Intercambiar los valores de num1 y num2
temp = num1
num1 = num2
num2 = temp

# Mostrar por pantalla el valor actualizado de num1 y num2
print("Valores intercambiados:")
print("num1 =", num1)
print("num2 =", num2)


# Pedir al usuario que ingrese los datos de los socios y sus capitales aportados
socio1_nombre = input("Ingrese el nombre del primer socio: ")
socio1_capital = float(input("Ingrese el capital aportado por el primer socio: "))

socio2_nombre = input("Ingrese el nombre del segundo socio: ")
socio2_capital = float(input("Ingrese el capital aportado por el segundo socio: "))

socio3_nombre = input("Ingrese el nombre del tercer socio: ")
socio3_capital = float(input("Ingrese el capital aportado por el tercer socio: "))

# Calcular el valor total aportado
total_aportado = socio1_capital + socio2_capital + socio3_capital

# Calcular el porcentaje aportado por cada socio
socio1_porcentaje = (socio1_capital / total_aportado) * 100
socio2_porcentaje = (socio2_capital / total_aportado) * 100
socio3_porcentaje = (socio3_capital / total_aportado) * 100

# Mostrar los resultados
print("\nValor total aportado:", total_aportado)
print("\nPorcentaje aportado por cada socio:")
print(f"{socio1_nombre}: {socio1_porcentaje:.2f}%")
print(f"{socio2_nombre}: {socio2_porcentaje:.2f}%")
print(f"{socio3_nombre}: {socio3_porcentaje:.2f}%")

