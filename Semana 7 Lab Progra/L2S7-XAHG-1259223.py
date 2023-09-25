"""print("Ejercicio 3: Jerarquía de operaciones")
a = input("Ingrese primer número ")
b = input("Ingrese segundo número ")
c = input("Ingrese tercer número ")

an = int(a)
bn = int(b)
cn = int(c)

print(an*bn+cn)
print(an*(bn+cn))
print(an/bn*cn)
print(((3*an)+(2*bn))/cn**2)

if an != 0:
    raizp = (-bn + (bn**2 - 4*an*cn)**0.5) / (2*an)
    raizn = (-bn - (bn**2 - 4*an*cn)**0.5) / (2*an)
    fcp = raizp
    fcn = raizn
    print(fcp)
    print(fcn)
else:
    print("La operación no puede ser realizada debido a que la división por cero resulta en una indefinición matemática. " )"""


print("Ejercicio 3: Jerarquía de operaciones")
a = input("Ingrese primer número ")
b = input("Ingrese segundo número ")
c = input("Ingrese tercer número ")

an = int(a)
bn = int(b)
cn = int(c)

print("A continuacion se muestra un menu de operaciones que puede realizar")
print("a * b + c = 1")
print("a * (b + c) = 2")
print("a / b * c = 3")
print("3a + 2b / c^2 = 4")
print("Fórmula cuadrática positiva = 5")
print("Fórmula cuadrática negativa = 6")

z = input("Seleccione el número de la operacion que desea realizar ")

if z == "1":
    print(an*bn+cn)
elif z == "2":
    print(an*(bn+cn))
elif z == "3":
    print(an/bn*cn)
elif z == "4":
    print(((3*an)+(2*bn))/cn**2)
elif z == "5":
    if an != 0:
        raizp = (-bn + (bn**2 - 4*an*cn)**0.5) / (2*an)
        fcp = raizp
        print(fcp)
    else:
        print("La operación no puede ser realizada debido a que la división por cero resulta en una indefinición matemática. " )
elif z == "6":
    if an != 0:
        raizn = (-bn - (bn**2 - 4*an*cn)**0.5) / (2*an)
        fcn = raizn
        print(fcn)
    else:
        print("La operación no puede ser realizada debido a que la división por cero resulta en una indefinición matemática. " )

x = input("Escriba 'continuar' para realizar otra operacion o 'cancelar' para cerrar el programa ")

while x == "continuar":
    print("A continuacion se muestra un menu de operaciones que puede realizar")
    print("a * b + c = 1")
    print("a * (b + c) = 2")
    print("a / b * c = 3")
    print("3a + 2b / c^2 = 4")
    print("Fórmula cuadrática positiva = 5")
    print("Fórmula cuadrática negativa = 6")

    z = input("Seleccione el número de la operacion que desea realizar ")

    if z == "1":
        print(an*bn+cn)
    elif z == "2":
        print(an*(bn+cn))
    elif z == "3":
        print(an/bn*cn)
    elif z == "4":
        print(((3*an)+(2*bn))/cn**2)
    elif z == "5":
        if an != 0:
            raizp = (-bn + (bn**2 - 4*an*cn)**0.5) / (2*an)
            fcp = raizp
            print(fcp)
        else:
            print("La operación no puede ser realizada debido a que la división por cero resulta en una indefinición matemática. " )
    elif z == "6":
        if an != 0:
            raizn = (-bn - (bn**2 - 4*an*cn)**0.5) / (2*an)
            fcn = raizn
            print(fcn)
        else:
            print("La operación no puede ser realizada debido a que la división por cero resulta en una indefinición matemática. " )

    x = input("Escriba 'continuar' para realizar otra operacion o 'cancelar' para cerrar el programa ")
else:
    print("de nada, vuelva pronto")


