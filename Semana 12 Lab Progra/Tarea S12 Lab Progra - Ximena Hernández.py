ciclo = True
while ciclo:
    print("\nA continuacion se muestra un menu de operaciones que puede realizar")
    print(" 1 = suma")
    print(" 2 = resta")
    print(" 3 = multiplicacion")
    print(" 4 = division")
    print(" 5 = salir")
    
    z = input("Seleccione el número de la operacion que desea realizar ")

    if z not in ["1", "2", "3", "4", "5"]:
        print("El número que ingresó no se encuentra en el menú de operaciones. Por favor ingresar un número válido")

    else:
        if z == "5":
            ciclo = False
            print("De nada, vuelva pronto :) ")
    
        else:
            class Calculadora:
                def __init__(self):
                    self.numero1 = float
                    self.numero2 = float

                def numero1_(self, numero):
                    self.numero1 = numero

                def numero2_(self, numero):
                    self.numero2 = numero

                def obtenersuma(self):
                    return self.numero1 + self.numero2

                def obtenerresta(self):
                    return self.numero1 - self.numero2

                def obtenermulti(self):
                    return self.numero1 * self.numero2

                def obtenerdivi(self):
                    if self.numero2 != 0:
                        return self.numero1 / self.numero2
                    else:
                        return "División entre cero no permitida"

            mi_calculadora = Calculadora()

            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))

            mi_calculadora.numero1_(numero1)
            mi_calculadora.numero2_(numero2)

            if z == "1":
                print("Resultado de la suma:", mi_calculadora.obtenersuma())
            if z == "2":
                print("Resultado de la resta:", mi_calculadora.obtenerresta())
            if z == "3":
                print("Resultado de la multiplicación:", mi_calculadora.obtenermulti())
            if z == "4":
                print("Resultado de la división:", mi_calculadora.obtenerdivi())
            
        
        


