class Movimiento:
    def __init__(self, tablero, casillaDePartida, casillaAtacada):
        self.tablero = tablero
        self.casillaDePartida = casillaDePartida
        self.casillaAtacada = casillaAtacada
        self.eje = self.getEje()
    

    def getEje(self):
        if self.casillaDePartida.comparteFilaCon(self.casillaAtacada):
            return 'horizontal'
        elif self.casillaDePartida.comparteColumnaCon(self.casillaAtacada):
            return 'vertical'
        elif self.casillaDePartida.comparteDiagonalCon(self.casillaAtacada):
            return 'diagonal'
    

    def saltaPiezas(self):
        if self.eje == 'horizontal':
            fila = [casilla for casilla in self.tablero if casilla.y == self.casillaDePartida.y]
            casillas_entre_inicio_destino = [casilla for casilla in fila if (self.casillaDePartida.y <= casilla.y <= self.casillaAtacada.y) or (self.casillaDePartida.y >= casilla.y >= self.casillaAtacada.y)]
            for casilla in casillas_entre_inicio_destino:
                if casilla.pieza:
                    return True
        elif self.eje == 'vertical':
            columna = [casilla for casilla in self.tablero if casilla.x == self.casillaDePartida.x]
            casillas_entre_inicio_destino = [casilla for casilla in columna if (self.casillaDePartida.x <= casilla.x <= self.casillaAtacada.x) or (self.casillaDePartida.x >= casilla.x >= self.casillaAtacada.x)]
            for casilla in casillas_entre_inicio_destino:
                if casilla.pieza:
                    return True
        elif self.eje == 'diagonal':
            def casillasRecorridas(casillaDePartida, casillaDeDestino):
                deltaX = casillaDeDestino.x - casillaDePartida.x
                deltaY = casillaDeDestino.y - casillaDePartida.y

                # Determinar la dirección del movimiento del alfil
                direccion_x = 1 if deltaX > 0 else -1
                direccion_y = 1 if deltaY > 0 else -1

                casillas_recorridas = []

                # Iterar a lo largo de la diagonal desde la casilla de partida hacia la casilla de destino
                x = casillaDePartida.x + direccion_x
                y = casillaDePartida.y + direccion_y
                while x != casillaDeDestino.x and y != casillaDeDestino.y:
                    casillas_recorridas.append((x, y))
                    x += direccion_x
                    y += direccion_y

                return casillas_recorridas
            
            casillas_entre_inicio_destino = casillasRecorridas(self.casillaAtacada, self.casillaDePartida)


            for casilla in casillas_entre_inicio_destino:
                if casilla.pieza:
                    return True