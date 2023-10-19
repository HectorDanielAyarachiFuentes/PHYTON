# Solicitar al usuario que ingrese los números y la operación
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

# Realizar la operación y mostrar el resultado
if operacion == '+':
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operacion == '-':
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operacion == '*':
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("ERROR: No se puede dividir por cero.")
else:
    print("Operación no válida.")
