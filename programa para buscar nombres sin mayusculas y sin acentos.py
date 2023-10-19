from unidecode import unidecode
from colorama import init, Fore, Style

MASCULINOS = [
    "Carlos", "José", "Pedro", "Manuel", "Juan",
    "Miguel", "Alberto", "Francisco", "Diego", "Antonio",
    "Eduardo", "Sergio", "Fernando", "Javier", "Ricardo",
    "Andrés", "Oscar", "Daniel", "Alejandro", "Mario",
    "Gustavo", "Enrique", "Alfredo", "Mauricio", "Martín",
    "Luis", "Raúl", "Gabriel", "Felipe", "Samuel",
    "Vicente", "Cristian", "Hugo", "Adrián", "Ignacio",
    "Arturo", "Pablo", "Rafael", "Salvador", "Julio",
    "Isaac", "Leonardo", "Ángel", "Santiago", "Víctor",
    "Elías", "Gonzalo", "Erik", "Ramón", "Alex"
]
FEMENINOS = [
    "María", "Ana", "Sofía", "Laura", "Carmen",
    "Isabel", "Marta", "Elena", "Patricia", "Sara",
    "Rosa", "Cristina", "Susana", "Lucía", "Paula",
    "Natalia", "Clara", "Beatriz", "Andrea", "Esther",
    "Verónica", "Julieta", "Vanesa", "Marina", "Lorena",
    "Silvia", "Julia", "Cecilia", "Teresa", "Luisa",
    "Rocío", "Yolanda", "Victoria", "Mercedes", "Irene",
    "Leticia", "Raquel", "Adriana", "Mónica", "Sonia",
    "Inés", "Daniela", "Miriam", "Virginia", "Pilar",
    "Gabriela", "Alejandra", "Violeta", "Olga", "Mar"
]

# Inicializa colorama
init(autoreset=True)

def quitar_acentos(nombre):
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
    }
    
    nombre_sin_acentos = ''.join(reemplazos.get(c, c) for c in nombre)
    
    return nombre_sin_acentos

def buscar_nombre(nombre, lista_nombres):
    nombre_sin_acentos = quitar_acentos(nombre)
    nombre_minusculas = nombre_sin_acentos.lower()
    nombres_minusculas = [quitar_acentos(n).lower() for n in lista_nombres]

    if nombre_minusculas in nombres_minusculas:
        return f"{Fore.GREEN + Style.BRIGHT}El nombre '{nombre}' se encuentra en la lista de nombres.{Style.RESET_ALL}"
    else:
        return f"{Fore.RED + Style.BRIGHT}El nombre '{nombre}' no se encuentra en la lista de nombres.{Style.RESET_ALL}"

while True:
    print(f"{Fore.CYAN}¿Qué sexo de nombres deseas buscar?{Style.RESET_ALL}")
    print(f"1. {Fore.MAGENTA}Masculino{Style.RESET_ALL}")
    print(f"2. {Fore.MAGENTA}Femenino{Style.RESET_ALL}")
    print(f"3. {Fore.YELLOW}Salir{Style.RESET_ALL}")
    
    opcion = input(f"{Fore.CYAN}Selecciona una opción (1/2/3): {Style.RESET_ALL}")
    
    if opcion == "1":
        sexo = "masculinos"
        lista_nombres = MASCULINOS
    elif opcion == "2":
        sexo = "femeninos"
        lista_nombres = FEMENINOS
    elif opcion == "3":
        break
    else:
        print(f"{Fore.RED + Style.BRIGHT}Opción no válida. Por favor, elige 1, 2 o 3.{Style.RESET_ALL}")
        continue
    
    nombre_a_buscar = input(f"{Fore.CYAN}Ingresa un nombre {sexo} para buscar (o escribe 'salir' para volver al menú anterior): {Style.RESET_ALL}")
    
    if nombre_a_buscar.lower() == "salir":
        continue
    
    resultado = buscar_nombre(nombre_a_buscar, lista_nombres)
    print(resultado)
