import pygame as pg
from movimiento import Movimiento

class AdministradorDeEventos:
    def __init__(self, tablero, arbitro):
        self.tablero = tablero
        self.arbitro = arbitro
        self.acciones = {
            pg.QUIT: self.salirDelJuego,
            pg.MOUSEBUTTONDOWN: self.manejarClick
        }


    def manejarEventos(self):
        for evento in pg.event.get():
            if evento.type in self.acciones:
                self.acciones[evento.type]()


    def manejarClick(self):
        coordenadasClick = pg.mouse.get_pos()
        casillaClickeada = self.getCasillaClickeada(coordenadasClick)
        casillaSeleccionada = self.tablero.getCasillaSeleccionada()
        jugadorActivo = self.arbitro.getJugadorActivo()
        piezaSeleccionada = jugadorActivo.getPiezaSeleccionada()

        if casillaSeleccionada is casillaClickeada:
            
            self.quitarSeleccionACasilla(casillaSeleccionada)
            if casillaClickeada.pieza:
                self.quitarSeleccionAPieza(casillaClickeada.pieza)

        else:

            if self.tablero.getCasillaSeleccionada():
                if piezaSeleccionada:
                    movimiento = Movimiento(self.tablero, casillaSeleccionada, casillaClickeada)
                    if self.arbitro.validarMovimiento(movimiento):
                        jugadorActivo.moverPieza(movimiento)
                        piezaSeleccionada.generarRuta(movimiento)
                        self.arbitro.terminarTurno()
                        self.arbitro.setJugadorActivo()

                    self.quitarSeleccionACasilla(casillaSeleccionada)
                    self.quitarSeleccionAPieza(piezaSeleccionada)                    

                else:
                    self.quitarSeleccionACasilla(casillaSeleccionada)
                    self.seleccionarCasilla(casillaClickeada)
                    if casillaClickeada.pieza and (jugadorActivo.color == casillaClickeada.pieza.color):
                        self.seleccionarPieza(casillaClickeada.pieza)

            else:
                self.seleccionarCasilla(casillaClickeada)
                if casillaClickeada.pieza and (jugadorActivo.color == casillaClickeada.pieza.color):
                    self.seleccionarPieza(casillaClickeada.pieza)
    

    def salirDelJuego(self):
        pg.quit()
        exit()


    def getCasillaClickeada(self, coordenadasClick):
        for casilla in self.tablero.casillas:
            if casilla.rect.collidepoint(coordenadasClick):
                return casilla
    

    def seleccionarCasilla(self, casilla):
        casilla.seleccionada = True
    

    def quitarSeleccionACasilla(self, casilla):
        casilla.seleccionada = False


    def seleccionarPieza(self, pieza):
        pieza.seleccionada = True
    

    def quitarSeleccionAPieza(self, pieza):
        pieza.seleccionada = False