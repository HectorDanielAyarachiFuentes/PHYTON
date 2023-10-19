enunciado = """
Realizá un programa que permita que el usuario ingrese su nombre. 
El programa debe emitir una salida con un mensaje de bienvenida que 
incluya el nombre ingresado.
"""

print(enunciado)

while True:
    nombre_usuario = input("Ingrese su nombre (o escriba 'salir' para finalizar): ")

    if nombre_usuario.lower() == "salir":
        break

    print("Hola", nombre_usuario)
    cartel = "Hola " + nombre_usuario + ", ¿cómo estás?"
    print(cartel)








