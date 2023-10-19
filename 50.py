def validar_nota(nota):
    if nota == 0:
        return "Ausente"
    elif nota == 1 or nota == 3:
        return "Nota inválida"
    elif nota >= 2 and nota <= 10:
        return "Nota válida"
    else:
        return "Nota fuera de rango"

while True:
    try:
        nota = float(input("Ingrese la nota del examen (0-10): "))
        if nota.is_integer() and nota >= 0:
            resultado = validar_nota(int(nota))
            print(resultado)
            if resultado == "Nota válida":
                break
        else:
            print("Ingrese un número entero entre 0 y 10.")
    except ValueError:
        print("Ingrese un valor numérico válido.")
