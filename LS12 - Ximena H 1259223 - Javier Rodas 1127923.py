class Persona:
    def __init__(self):
        self.nombres = ""
        self.apellidos = ""
        self.apecasada = ""

    def nombres_(self, nombres):
        self.nombres = nombres

    def apellidos_(self, apellidos):
        self.apellidos = apellidos

    def apecasada_(self, apecasada):
        self.apecasada = apecasada

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        if self.apecasada:
            return f"{self.apellidos} {self.apecasada}"
        else:
            return self.apellidos

    def nombre_completo(self):
        return f"{self.nombres} {self.obtener_apellidos()}"

p1 = Persona()


p1.nombres_("Carla María")
p1.apellidos_("Valladares Castro")
p1.apecasada_("Juarez")

print("Nombres:", p1.obtener_nombres())
print("Apellidos:", p1.obtener_apellidos())

print("Nombre Completo:", p1.nombre_completo())
