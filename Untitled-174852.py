def calcular_importe_a_cobrar(ventas):
    sueldo_fijo = 44000
    porcentaje_comision = 0.16

    monto_total_vendido = float(ventas)
    comision = monto_total_vendido * porcentaje_comision
    importe_a_cobrar = sueldo_fijo + comision

    return importe_a_cobrar

def main():
    monto_ventas = input("Ingrese el monto total de ventas realizadas por el vendedor en el mes: ")

    try:
        importe_a_cobrar = calcular_importe_a_cobrar(monto_ventas)
        print("El importe a cobrar por el vendedor es: {:.2f} pesos".format(importe_a_cobrar))
    except ValueError:
        print("Error: Ingrese un monto válido de ventas (número decimal).")

if __name__ == "__main__":
    main()
