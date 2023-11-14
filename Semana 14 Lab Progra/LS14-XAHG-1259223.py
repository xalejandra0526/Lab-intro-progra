class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = False
        self.tipoCambioDolar = 0.0
        self.descuentoAplicado = 0.0

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def MostrarInformacion(self):
        precio_dolares = self.precio / self.tipoCambioDolar
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares: ${precio_dolares}. {self.MostrarDisponibilidad()}"

    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        precio_con_descuento = self.precio - (self.precio * self.descuentoAplicado)
        self.DefinirPrecio(precio_con_descuento)

# Ejemplo de uso:
automovil_ejemplo = Automovil()
automovil_ejemplo.DefinirModelo(2015)
automovil_ejemplo.DefinirPrecio(28580.0)
automovil_ejemplo.DefinirMarca("Toyota")
automovil_ejemplo.DefinirTipoCambio(7.60)
automovil_ejemplo.CambiarDisponibilidad()

print(automovil_ejemplo.MostrarInformacion())

automovil_ejemplo.AplicarDescuento(0.2)

print(automovil_ejemplo.MostrarInformacion())
