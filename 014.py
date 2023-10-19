# Paso 1: Solicitar al usuario que ingrese el ancho y largo del terreno
ancho = float(input("Ingrese el ancho del terreno en metros: "))
largo = float(input("Ingrese el largo del terreno en metros: "))

# Paso 2: Solicitar al usuario que ingrese el valor del metro cuadrado de tierra
valor_metro_cuadrado = float(input("Ingrese el valor del metro cuadrado de tierra en pesos: "))

# Paso 3: Calcular el valor total del terreno
valor_total_terreno = ancho * largo * valor_metro_cuadrado

# Mostrar el valor total del terreno
print("El valor total del terreno es:", valor_total_terreno, "pesos")

# Paso 4: Calcular la cantidad de metros de alambre necesarios para cercar a tres alturas distintas
altura_1 = 1  # metros
altura_2 = 2  # metros
altura_3 = 3  # metros

perimetro = 2 * (ancho + largo)
metros_alambre_altura_1 = perimetro * altura_1
metros_alambre_altura_2 = perimetro * altura_2
metros_alambre_altura_3 = perimetro * altura_3

# Mostrar la cantidad de metros de alambre necesarios para cercar a las tres alturas distintas
print("Metros de alambre necesarios a", altura_1, "metro de altura:", metros_alambre_altura_1, "metros")
print("Metros de alambre necesarios a", altura_2, "metros de altura:", metros_alambre_altura_2, "metros")
print("Metros de alambre necesarios a", altura_3, "metros de altura:", metros_alambre_altura_3, "metros")
