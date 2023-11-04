class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def obtener_perimetro(self):
        return (2 * 3.14 * self.radio)

    def obtener_area(self):
        return (self.radio) ** 2 * 3.14

    def obtener_volumen(self):
        return ((4*3.14)*(self.radio)**3)/3

cantidad_circulos = int(input("Ingrese la cantidad de círculos que desea crear: "))
if cantidad_circulos <= 0:
    print("Por favor escriba una cantidad válida de circulos [1, ∞]")

for i in range(cantidad_circulos):
    radio = float(input(f"Ingrese el radio del círculo {i+1}: "))
    c = Circulo(radio)
    print(f"Círculo {i+1}:")
    print("Perímetro:", c.obtener_perimetro())
    print("Área:", c.obtener_area())
    print("Volumen:", c.obtener_volumen())
    print()
