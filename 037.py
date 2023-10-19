def calcular_sueldo_neto(sueldo_basico, antiguedad, estado_civil):
    if estado_civil == "S":
        incremento_por_antiguedad = 0.05
    elif estado_civil == "C":
        incremento_por_antiguedad = 0.07
    else:
        print("Estado civil no válido.")
        return
    
    incremento = sueldo_basico * incremento_por_antiguedad * antiguedad
    sueldo_bruto = sueldo_basico + incremento
    
    jubilacion = sueldo_bruto * 0.11
    obra_social = sueldo_bruto * 0.03
    sindicato = sueldo_bruto * 0.03
    
    sueldo_neto = sueldo_bruto - jubilacion - obra_social - sindicato
    
    print("Estado Civil:", "Soltero" if estado_civil == "S" else "Casado")
    print("Sueldo básico: $", sueldo_basico)
    print("Antigüedad:", antiguedad, "años\n")
    print("Descuentos:")
    print("Jubilación - {:.2f}".format(jubilacion))
    print("Obra Social - {:.2f}".format(obra_social))
    print("Sindicato - {:.2f}".format(sindicato))
    print("\nSueldo Neto {:.2f}".format(sueldo_neto))

def main():
    sueldo_basico = float(input("Ingrese el sueldo básico: "))
    antiguedad = int(input("Ingrese la antigüedad en años: "))
    estado_civil = input("Ingrese el estado civil (S para Soltero / C para Casado): ").upper()
    
    calcular_sueldo_neto(sueldo_basico, antiguedad, estado_civil)

if __name__ == "__main__":
    main()
