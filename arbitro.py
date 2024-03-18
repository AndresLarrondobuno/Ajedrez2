
class Arbitro:
    def __init__(self, partida):
        self.partida = partida
    

    def setJugadorActivo(self):
        self.partida.jugadorActivo = self.partida.jugadorBlancas if self.partida.turno % 2 else self.partida.jugadorNegras


    def getJugadorActivo(self):
        return self.partida.jugadorActivo
    

    def terminarTurno(self):
        self.partida.turno += 1


    def validarMovimiento(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada = movimiento.casillaAtacada
        piezaAtacante = movimiento.casillaDePartida.pieza
        piezaAtacada = movimiento.casillaAtacada.pieza

        jugadorValido = self.jugadorValido(movimiento)
        respetaPatronDeMovimiento = piezaAtacante.respetaPatronDeMovimiento(movimiento)
        #no_ataca_pieza_aliada = pieza_atacante.color != pieza_atacada.color if pieza_atacante
        return True

        #validar ruta despejada
        #validar autojaque


    def jugadorValido(self, movimiento):
        jugadorActivo = self.getJugadorActivo()
        piezaAtacante = movimiento.casillaDePartida.pieza
        if piezaAtacante in jugadorActivo.piezas:
            return True