def main():
    numero = int(input("Ingrese un número entero: "))
    
    esDeUnSoloDigito = numero >= 0 and numero <= 9
    esImpar = numero % 2 != 0
    
    estaEnAmbos = esDeUnSoloDigito and esImpar
    noEstaEnNinguno = not esDeUnSoloDigito and not esImpar
    
    print("Es de un solo dígito:", esDeUnSoloDigito)
    print("Es impar:", esImpar)
    print("Está en ambos conjuntos:", estaEnAmbos)
    print("No está en ninguno de los conjuntos:", noEstaEnNinguno)

if __name__ == "__main__":
    main()
5
