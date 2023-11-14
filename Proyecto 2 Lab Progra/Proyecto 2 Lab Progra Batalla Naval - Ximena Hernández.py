class Tablero:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tablero = [[" "  for _ in range(tamaño)] for _ in range(tamaño)]

    def tiro_valido(self, objetivo):
        fila, colu = self.convertir_coordenadas(objetivo)
        return 0 <= fila < self.tamaño and 0 <= colu < self.tamaño and self.tablero[fila][colu] not in ["O", "X"]
    
    def conjunto_celda(self, fila, columna, contenido):
        self.tablero[fila][columna] = contenido
    
    def lugar_barco(self, barco, start, orientacion):
        if orientacion.lower() not in ["horizontal", "vertical"]:
            print("La orientación ingresada no es válida. Por favor ingresar 'horizontal' o 'vertical'.")
            return

        fila, colu = self.convertir_coordenadas(start)  

        
        if not self.colocacion_valida(fila, colu, barco, orientacion):
            print("No puede colocar barcos en tales coordenadas.")
            return

        
        if orientacion == "horizontal":
            for i in range(barco.tamaño):
                if barco.tamaño == 5 and (colu == 6 or colu == 7 or colu == 8 or colu == 9): 
                    self.tablero[fila][colu - i] = "X"
                elif barco.tamaño == 3 and (colu == 8 or colu == 9): 
                    self.tablero[fila][colu - i] = "X"
                else:
                    self.tablero[fila][colu + i] = "X"
        else:
            for i in range(barco.tamaño):
                if fila == 8 or fila == 9:
                    self.tablero[fila - i][colu] = "X"
                else:
                    self.tablero[fila + i][colu] = "X"

        barco.coordenadas = [(fila, colu + i) if orientacion == "horizontal" else (fila + i, colu) for i in range(barco.tamaño)]
        

    
    def convertir_coordenadas(self, coord):
        colu = ord(coord[0].upper()) - ord('A')
        fila = int(coord[1:]) - 1
        return fila, colu

    def colocacion_valida(self, fila, colu, barco, orientacion):
        if orientacion == "horizontal" or orientacion == "vertical":
            if colu > self.tamaño or fila > self.tamaño:
                return False
        
        for i in range(barco.tamaño):
            if self.tablero[fila][colu] == 'X' and orientacion == "horizontal":
                return False
            if self.tablero[fila][colu] == 'X' and orientacion == "vertical":
                return False

        return True

    def print_tablero(self):
        print("  " + " ".join([chr(65 + i) for i in range(self.tamaño)]))
        for i, fila in enumerate(self.tablero):
            print(str(i + 1) + " " + " ".join(fila))

    def convertir_coordenadas(self, coord):
        colu = ord(coord[0].upper()) - ord('A')
        fila = int(coord[1:]) - 1
        return fila, colu

def tomar_disparo(self, oponente, objetivo):
    if oponente.tablero.tiro_valido(objetivo):
        if oponente.tablero.obtener_celda(objetivo) == 'X':
            self.disparos_acertados.append((objetivo, "Barco impactado"))
            oponente.tablero.conjunto_celda(objetivo, "*")  
            for barco in oponente.barcos:
                if objetivo in barco.coordenadas:
                    barco.hit()  
        else:
            self.disparos_fallidos.append((objetivo,))
            oponente.tablero.conjunto_celda(objetivo, "O")  
    else:
        print("La coordenada para el disparo ingresada no es válida.")

class Jugador:
    def __init__(self, name):
        self.name = name
        self.tablero = {}  
        self.barcos = []
        self.disparos_acertados = []
        self.disparos_fallidos = []
        self.tiros = []
        self.tablero = Tablero(10) 

    def lugar_barco(self, barco, start, orientacion):
        if orientacion.lower() not in ["horizontal", "vertical"]:
            print("La orientación ingresada no es válida. Por favor ingresar 'horizontal' o 'vertical'.")
            return

        fila, colu = self.tablero.convertir_coordenadas(start)  

    
        if not self.tablero.colocacion_valida(fila, colu, barco, orientacion):
            print("No puede colocar barcos en tales coordenadas.")
            return

        
        self.tablero.lugar_barco(barco, start, orientacion)
        self.barcos.append(barco)

    def tomar_disparo(self, oponente, objetivo):

        if self.no_objetivo(objetivo):
            print("La coordenada ingresada fue fuera del cuadro, pierdes tu turno")
            return

        
        if self.ya_disparado(objetivo):
            print("Ya has disparado en esa coordenada, pierdes tu turno")
            return

        
        fila, colu = self.tablero.convertir_coordenadas(objetivo)

        
        hit = False
        for barco in oponente.barcos:
            if (fila, colu) in barco.coordenadas:
                self.tiros.append((fila, colu))
                hit = True
                barco.hit(fila, colu)
                oponente.tablero.conjunto_celda(fila, colu, "*")  
                self.disparos_acertados.append((objetivo, "Barco impactado"))
                if barco.hundido:
                    print(f"¡Lograste hundir el barco {barco.name} del oponente!")
                    oponente.barcos.remove(barco)
                break

        if not hit:
            oponente.tablero.conjunto_celda(fila, colu, "O")  
            self.disparos_fallidos.append((objetivo,))


    def comprobar_victoria(self, oponente):
        return len(oponente.barcos) == 0

    
    def print_tablero(self):
        self.tablero.print_tablero()

    def no_objetivo(self, objetivo):
        fila, colu = self.tablero.convertir_coordenadas(objetivo)
        if fila >= self.tablero.tamaño or colu >= self.tablero.tamaño:
            return True


    def ya_disparado(self, objetivo):
        fila, colu = self.tablero.convertir_coordenadas(objetivo)
        if (fila, colu) in self.tiros:
            return True
        
class Barco:
    def __init__(self, name, tamaño):
        self.name = name
        self.tamaño = tamaño
        self.coordenadas = []
        self.hit_count = 0
        self.hundido = False

    def hit(self, fila, colu):
        self.hit_count += 1
        self.coordenadas.remove((fila, colu))
        if self.hit_count >= self.tamaño:
            
            self.hundir()

    def hundir(self):
        self.hundido = True

if __name__ == "__main__":
    print("Juego Batalla Naval")

    
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")

    
    print("Jugador 1, coloca tus barcos en el tablero:")
    for i in range(3):
        barco = Barco("Barco Pequeño " + str(i + 1), 3)  
        start = input("Barco Pequeño " + str(i + 1) + ":\nCoordenada de inicio (por ejemplo, A1): ")
        orientacion = input("Orientación (horizontal o vertical): ")
        print("\033c", end='')
        jugador1.lugar_barco(barco, start, orientacion)
        jugador1.print_tablero()     
  

    for i in range(2):
        barco = Barco("Barco Grande " + str(i + 1), 5)  
        start = input("Barco Grande " + str(i + 1) + ":\nCoordenada de inicio (por ejemplo, A1): ")
        orientacion = input("Orientación (horizontal o vertical): ")
        print("\033c", end='')
        jugador1.lugar_barco(barco, start, orientacion)
        jugador1.print_tablero()  
        
        

    
    print("Jugador 2, coloca tus barcos en el tablero:")
    for i in range(3):
        barco = Barco("Barco Pequeño " + str(i + 1), 3)  
        start = input("Barco Pequeño " + str(i + 1) + ":\nCoordenada de inicio (por ejemplo, A1): ")
        orientacion = input("Orientación (horizontal o vertical): ")
        print("\033c", end='')
        jugador2.lugar_barco(barco, start, orientacion)
        jugador2.print_tablero()  

    for i in range(2):
        barco = Barco("Barco Grande " + str(i + 1), 5)  
        start = input("Barco Grande " + str(i + 1) + ":\nCoordenada de inicio (por ejemplo, A1): ")
        orientacion = input("Orientación (horizontal o vertical): ")
        print("\033c", end='')
        jugador2.lugar_barco(barco, start, orientacion)
        jugador2.print_tablero()

    
    print("\033c", end='')
    while True:
        print("Turno de " + jugador1.name)
        objetivo = input("Coordenada para disparar (por ejemplo, A1): ")
        jugador1.tomar_disparo(jugador2, objetivo)
        jugador2.tablero.print_tablero()  

        if jugador1.comprobar_victoria(jugador2):
            print("¡Jugador 1 ha ganado!")
            break

        print("Turno de " + jugador2.name)
        objetivo = input("Coordenada para disparar (por ejemplo, A1): ")
        jugador2.tomar_disparo(jugador1, objetivo)
        jugador1.tablero.print_tablero() 

        if jugador2.comprobar_victoria(jugador1):
            print("¡Jugador 2 ha ganado!")
            break