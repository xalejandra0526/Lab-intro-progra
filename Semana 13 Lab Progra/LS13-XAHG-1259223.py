class circulo:
    def __init__ (self, radio):
        self.radio = radio

    def obtener_perimetro (self):
        return (2*3.14*self.radio)
    
    def obtener_area (self):
        return (self.radio)**2 * 3.14
    
    def obtener_volumen (self):
        return ((4*3.14)*(self.radio)**3)/3

circulo1 = circulo(10)
print("Perimetro: ", circulo1.obtener_perimetro())
print("Área: ", circulo1.obtener_area())
print("Volumen: ", circulo1.obtener_volumen())