from unidecode import unidecode

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

def buscar_nombre(nombre):
    nombre_sin_acentos = unidecode(nombre)  # Quitamos los acentos del nombre ingresado
    nombre_minusculas = nombre_sin_acentos.lower()  # Convertimos a minúsculas
    nombres_minusculas = [unidecode(n).lower() for n in MASCULINOS]  # Quitamos acentos y convertimos a minúsculas

    if nombre_minusculas in nombres_minusculas:
        return f"El nombre '{nombre}' se encuentra en la lista de nombres masculinos."
    else:
        return f"El nombre '{nombre}' no se encuentra en la lista de nombres masculinos."

while True:
    nombre_a_buscar = input("Ingresa un nombre para buscar (o escribe 'salir' para salir): ")
    
    if nombre_a_buscar.lower() == "salir":
        break
    
    resultado = buscar_nombre(nombre_a_buscar)
    print(resultado)
