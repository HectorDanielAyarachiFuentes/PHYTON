# Solicitar los datos al usuario
nombre_vendedor = input("Ingrese el nombre del vendedor: ")
cantidad_ventas = int(input("Ingrese la cantidad de ventas realizadas: "))
valor_total_ventas = float(input("Ingrese el valor total de las ventas: "))

# Definir los valores constantes
salario_base = 200000  # Salario base del vendedor
comision_por_venta = 5000  # Comisión fija por cada venta realizada
porcentaje_comision = 0.05  # Porcentaje del valor de las ventas

# Calcular la comisión total
comision_total = comision_por_venta * cantidad_ventas

# Calcular la comisión por el 5% del valor de las ventas
comision_5_porcentaje = valor_total_ventas * porcentaje_comision

# Calcular el salario total
salario_total = salario_base + comision_total + comision_5_porcentaje

# Mostrar los resultados
print("Nombre del vendedor:", nombre_vendedor)
print("Salario correspondiente:", salario_total)
