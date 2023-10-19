# Solicitar al usuario que ingrese la cantidad de dinero a convertir
cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))

# Inicializar el valor del resto como la cantidad total
resto = cantidad_total

# Calcular la cantidad de cada tipo de billete y moneda
billetes_mil = resto // 1000
resto %= 1000

billetes_doscientos = resto // 200
resto %= 200

billetes_cien = resto // 100
resto %= 100

billetes_cincuenta = resto // 50
resto %= 50

billetes_diez = resto // 10
resto %= 10

billetes_cinco = resto // 5
resto %= 5

billetes_uno = resto // 1

# Mostrar los resultados
print("Para la cantidad de", cantidad_total, "soles:")
print(billetes_mil, "billetes de 1000 soles")
print(billetes_doscientos, "billetes de 200 soles")
print(billetes_cien, "billetes de 100 soles")
print(billetes_cincuenta, "billetes de 50 soles")
print(billetes_diez, "billetes de 10 soles")
print(billetes_cinco, "billetes de 5 soles")
print(billetes_uno, "billetes de 1 sol")
