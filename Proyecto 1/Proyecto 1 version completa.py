"""José Andrés Puaque Guerra #1189523, Ximena Alejandra Hernández Gómez #1259233"""
print("Proyecto número 1")
print("Por favor llenar los datos necesarios para calcular el rendimiento de las líneas de producción")

print("Ingrese los datos de la línea 1")
PM2=float(input("Ingrese el precio de venta por metro cuadrado de la línea 1: "))
M2PM=float(input("Ingrese la cantidad de metros cuadrados vendidos al mes de la línea 1: "))
CT1 = float(0)
CT2 = float(0)
ciclo = True
while ciclo:
    Nempleados=int(input("Ingrese la cantidad de empleados de la línea 1: "))
    CHPE1 = []
    HTPE1 = []
    if Nempleados >= 1 and Nempleados <= 20:
        for i in range (Nempleados):
            CHPE11 = float(input("\n Ingrese el pago por hora del empleado " + str(i+1) + ": "))
            HTPE11 = float(input("Ingrese las horas trabajadas del empleado " + str(i+1) + ": "))
            CHPE1.append(CHPE11)
            HTPE1.append(HTPE11)
            i = i + 1
        ciclo = False
    else:
        print("La cantidad de empleados no está dentro del rango admitido.")

print("\nIngrese los datos de la línea 2")
PM22=float(input("Ingrese el precio de venta por metro cuadrado de la línea 2: "))
M2PM2=float(input("Ingese la cantidad de metros cuadrados vendidos al mes de la línea 2: "))
CT2 = float(0)
ciclo2 = True
while ciclo2: 
    Nempleados2=int(input("Ingrese la cantidad de empleados de la línea 2: "))
    CHPE2 = []
    HTPE2 = []
    if Nempleados2 >= 1 and Nempleados2 <=20:
        for i in range (Nempleados2):
            CHPE22 = float(input("\n Ingrese el pago por hora del empleado " + str(i+1) + ": "))
            HTPE22 = float(input("Ingrese las horas trabajadas del empleado " + str(i+1) + ": "))
            CHPE2.append(CHPE22)
            HTPE2.append(HTPE22)
            i = i + 1
            ciclo2 = False
    else:
            print("La cantidad de empleados no está dentro del rango admitido.")


print("\nMetros vendidos en la línea 1:", M2PM, "mt2")
print("Precio por metro cuadrado línea 1:", PM2)
print("Costo por metro cuadrado: ")
print("  Empleados en la línea 1:", Nempleados)

for i in range(Nempleados):
    print(f"    Empleado {i + 1}:")
    print(f"    Horas trabajadas: {HTPE1[i]} horas")
    print(f"    Precio por hora: {CHPE1[i]}")
    print()

GT = M2PM * PM2
print("\nGanancia total =", M2PM, "*", PM2, "=", GT)

Cdesglosado = ""

for i in range(Nempleados):
    Cporempleado = CHPE1[i] * HTPE1[i]
    Cdesglosado = f"({CHPE1[i]} * {HTPE1[i]})" + Cdesglosado 

    if i < Nempleados - 1:
        Cdesglosado = " + " + Cdesglosado

    CT1 = Cporempleado + CT1

print("Costo total =", Cdesglosado, "=", CT1)

GN = GT - CT1
print("Ganancia total =", GT, "-", CT1, "=", GN)

mejorlinea = GN/len(CHPE1)
print("Índice de eficiencia = ", GN, "/", len(CHPE1), "=", mejorlinea)


print("\nMetros vendidos en la línea 2:", M2PM2, "mt2")
print("Precio por metro cuadrado línea 2:", PM22)
print("Costo por metro cuadrado: ")
print("  Empleados en la línea 2:", Nempleados2)

for i in range(Nempleados2):
    print(f"    Empleado {i + 1}:")
    print(f"    Horas trabajadas: {HTPE2[i]} horas")
    print(f"    Precio por hora: {CHPE2[i]}")
    print()

GT2 = M2PM2 * PM22
print("\nGanancia total =", M2PM2, "*", PM22, "=", GT2)

Cdesglosado2 = ""

for i in range(Nempleados2):
    Cporempleado2 = CHPE2[i] * HTPE2[i]
    Cdesglosado2 = f"({CHPE2[i]} * {HTPE2[i]})" + Cdesglosado2 

    if i < Nempleados2 - 1:
        Cdesglosado2 = " + " + Cdesglosado2

    CT2 = Cporempleado2 + CT2

print("Costo total =", Cdesglosado2, "=", CT2)

GN2 = GT2 - CT2
print("Ganancia total =", GT2, "-", CT2, "=", GN2)

mejorlinea2 = GN2/len(CHPE2)
print("Índice de eficiencia = ", GN2, "/", len(CHPE2), "=", mejorlinea2)
print()

if mejorlinea > mejorlinea2:
    print("La línea 1 tuvo mayor índice de eficiencia.")

if mejorlinea < mejorlinea2:
    print("La línea 2 tuvo mayor índice de eficiencia.")

else: 
    print("Las líneas tuvieron el mismo índice de eficiencia.")




