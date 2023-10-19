# Solicitar al usuario que ingrese el período de tiempo en segundos
segundos_totales = int(input("Ingrese un período de tiempo en segundos: "))

# Realizar cálculos para convertir los segundos a días, horas, minutos y segundos
dias = segundos_totales // 86400
segundos_restantes = segundos_totales % 86400

horas = segundos_restantes // 3600
segundos_restantes %= 3600

minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

# Mostrar el resultado al usuario
print(f"{segundos_totales} segundos equivale a:")
print(f"{dias} días, {horas} horas, {minutos} minutos y {segundos} segundos.")
