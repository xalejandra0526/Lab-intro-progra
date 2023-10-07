print("A continuacion se muestra un menu de operaciones que puede realizar")
print(" 1 = Factorial")
print(" 2 = Secuencia de Fibonacci")
print(" 3 = Salir")

z = input("Seleccione el número de la operacion que desea realizar ")

if z == "1":
    x = input("Ingrese el número del cual quiere obtener el factorial: ")
    x = int(x)
    
    factorial = 1
    
    for i in range(1, x + 1):
        factorial *= i
    
    print("El factorial de", x, "es", factorial, )

if z == "2":
    cantidad = input("Ingrese cuantos términos de la secuencia de Fibonacci que desea calcular: ")
    cantidad = int(cantidad)

    actual = 0
    siguiente = 1

    print("Resultado:")
    for i in range(cantidad):
        print(actual, end=" ")

        actual = siguiente
        siguiente = actual ++ siguiente

    print()

if z == "3":
    print("de nada, vuelva pronto :)")
