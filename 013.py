# Paso 1: Solicitar al usuario que ingrese el monto total de ventas
monto_ventas = float(input("Ingrese el monto total de ventas realizadas por el vendedor: "))

# Paso 2: Calcular el 16% del monto total de ventas
comision = 0.16 * monto_ventas

# Paso 3: Sumar la comisión al sueldo fijo
sueldo_fijo = 200000  # Sueldo fijo del vendedor
importe_a_cobrar = sueldo_fijo + comision

# Paso 4: Mostrar el importe a cobrar
print("El importe a cobrar por el vendedor es:", importe_a_cobrar)
