"""print("Ejercicio 1: Operaciones aritmeticas")
x = input("Ingrese primer numero ")
y = input("Ingrese segundo numero ")
xnumero =int(x)
ynumero = int(y)

suma = xnumero+ynumero
resta = xnumero-ynumero
multi = xnumero*ynumero
divi = xnumero/ynumero
modu = xnumero%ynumero
expo = xnumero**ynumero
coci = xnumero//ynumero


print(xnumero, "+", ynumero, "=", suma)
print(xnumero, "-", ynumero, "=", resta)
print(xnumero, "*", ynumero, "=", multi)
print(xnumero, "/", ynumero, "=", divi)
print(xnumero, "%", ynumero, "=", modu)
print(xnumero, "**", ynumero, "=", expo)
print(xnumero, "//", ynumero, "=", coci)"""

print("Ejercicio 2")

x = input("Ingrese primer numero ")
y = input("Ingrese segundo numero ")
xnumero =int(x)
ynumero = int(y)

suma = xnumero+ynumero
resta = xnumero-ynumero
multi = xnumero*ynumero
divi = xnumero/ynumero
modu = xnumero%ynumero
expo = xnumero**ynumero
coci = xnumero//ynumero

print("A continuacion se muestra un menu de operaciones que puede realizar")
print(" + = suma")
print(" - = resta")
print(" * = multiplicacion")
print(" / = division")
print(" % = modulo")
print(" ** = exponenciacion")
print(" // = cociente")

z = input("Seleccione el signo de la operacion que desea realizar ")

if z == "+":
    print(xnumero, "+", ynumero, "=", suma)
elif z == "-":
    print(xnumero, "-", ynumero, "=", resta)
elif z == "*":
    (xnumero, "*", ynumero, "=", multi)
elif z == "/":
    print(xnumero, "/", ynumero, "=", divi)
elif z == "%":
    print(xnumero, "%", ynumero, "=", modu)
elif z == "**":
    print(xnumero, "**", ynumero, "=", expo)
elif z == "//":
    print(xnumero, "//", ynumero, "=", coci)

a = input("Escriba continuar para realizar otra operacion o cancelar para cerrar el programa ")

while a == "continuar":
    print("A continuacion se muestra un menu de operaciones que puede realizar")
    print(" + = suma")
    print(" - = resta")
    print(" * = multiplicacion")
    print(" / = division")
    print(" % = modulo")
    print(" ** = exponenciacion")
    print(" // = cociente")

    z = input("Seleccione el signo de la operacion que desea realizar ")

    if z == "+":
        print(xnumero, "+", ynumero, "=", suma)
    elif z == "-":
        print(xnumero, "-", ynumero, "=", resta)
    elif z == "*":
        (xnumero, "*", ynumero, "=", multi)
    elif z == "/":
        print(xnumero, "/", ynumero, "=", divi)
    elif z == "%":
        print(xnumero, "%", ynumero, "=", modu)
    elif z == "**":
        print(xnumero, "**", ynumero, "=", expo)
    elif z == "//":
        print(xnumero, "//", ynumero, "=", coci)

    a = input("Escriba 'continuar' para realizar otra operacion o 'cancelar' para cerrar el programa ")
if a == "cancelar":
    print("de nada, vuelva pronto")


 




