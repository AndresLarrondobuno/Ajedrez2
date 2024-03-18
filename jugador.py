from movimiento import Movimiento
from pieza import Peon

class Jugador:
    def __init__(self, color:str, piezas):
        self.color = color
        self.piezas = piezas
    

    def __repr__(self) -> str:
        return f'Jugador de {self.color}'


    def moverPieza(self, movimiento: Movimiento):
        piezaAtacante = movimiento.casillaDePartida.pieza
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada = movimiento.casillaAtacada

        #chequeos de legalidad del movimiento por el arbitro como caller
        if not piezaAtacante.respetaPatronDeMovimiento(movimiento):
            return False
            
        if casillaAtacada.pieza:
            casillaAtacada.pieza.sprite.kill()
        

        casillaAtacada.pieza = piezaAtacante
        casillaDePartida.pieza = None

        if type(piezaAtacante) == Peon and piezaAtacante.enCasillaInicial:
            piezaAtacante.enCasillaInicial = False

        #guardar la jugada


    def comerPieza(self):
        pass


    def getPiezaSeleccionada(self):
        for pieza in self.piezas:
            if pieza.seleccionada:
                return pieza