# Definición de funciones matemáticas
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Definición de funciones de manipulación de cadenas
def capitalize(text):
    return text.capitalize()

def reverse(text):
    return text[::-1]

# Función principal
def main():
    num1 = 10
    num2 = 5
    result_add = add(num1, num2)
    result_subtract = subtract(num1, num2)

    print(f"Addition: {num1} + {num2} = {result_add}")
    print(f"Subtraction: {num1} - {num2} = {result_subtract}")

    text = "hello, world!"
    capitalized_text = capitalize(text)
    reversed_text = reverse(text)

    print(f"Original Text: {text}")
    print(f"Capitalized Text: {capitalized_text}")
    print(f"Reversed Text: {reversed_text}")

if __name__ == "__main__":
    main()
