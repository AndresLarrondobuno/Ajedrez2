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

casillas = casillasRecorridasPorAlfil((1,8), (7,2))
print(casillas)




