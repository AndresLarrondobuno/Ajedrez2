import numpy as np
import pygame as pg

class Casilla:

    def __init__(self, coordenadas:np.ndarray):
        self.coordenadas = coordenadas
        self.x, self.y = coordenadas
        self.rect = self.getRect()

        self.pieza = None
        self.color = None
        self.sprite = None
        self.seleccionada = False
    

    def __repr__(self) -> str:
        return str(self.coordenadas) + ' ' + self.pieza.nombre if self.pieza else str(self.coordenadas)
    

    def getRect(self):
        from tablero import Tablero
        rect = pg.Rect((0,0,0,0))
        rect.x = self.x*Tablero.anchoCasilla
        rect.y = self.y*Tablero.altoCasilla
        rect.width = Tablero.anchoCasilla
        rect.height = Tablero.altoCasilla
        return rect


    def ocupada(self):
        return True if self.pieza else False


    def distanciaHorizontal(self, casilla):
        if isinstance(casilla, Casilla):
            return abs(self.x - casilla.x)
        else:
            return abs(self.x - casilla)


    def distanciaVertical(self, casilla):
        if isinstance(casilla, Casilla):
            return abs(self.y - casilla.y)
        else:
            return abs(self.y - casilla)


    def distanciaOrtogonal(self, casilla):
        distanciaHorizontal = self.distanciaHorizontal(casilla)
        distanciaVertical = self.distanciaVertical(casilla)
        return distanciaHorizontal + distanciaVertical


    def comparteDiagonalCon(self, casilla: 'Casilla'):
        xi, yi = self.x,  self.y
        xf, yf =  casilla.x,  casilla.y
        return True if abs(xf-xi) == abs(yf-yi) else False


    def comparteFilaCon(self, casilla: 'Casilla'):
        yi = self.y
        yf = casilla.y
        return True if yf == yi else False


    def comparteColumnaCon(self, casilla: 'Casilla'):
        xi = self.x
        xf = casilla.x
        return True if xf == xi else False
    

    def ortogonalCon(self, casilla: 'Casilla'):
        return True if self.comparteFilaCon(casilla) or self.comparteColumnaCon(casilla) else False
    

    def perteneceARutaDelMovimiento(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada = movimiento.casillaAtacada
        ejeDelMovimiento = movimiento.getEje()
        direccionHaciaCasillaDePartida = casillaDePartida.getDireccion(self, ejeDelMovimiento)
        direccionHaciaCasillaAtacada = casillaAtacada.getDireccion(self, ejeDelMovimiento)

        print(f'C: {self}  / direccion_hacia_c_partida: {direccionHaciaCasillaDePartida}  / direccion_hacia_casilla_atacada: {direccionHaciaCasillaAtacada}')
        return direccionHaciaCasillaDePartida != direccionHaciaCasillaAtacada
    

    def getDireccion(self, casilla, eje):
        if eje == 'horizontal' and self.comparteFilaCon(casilla):
            direccion = True if (self.x - casilla.x) > 0 else False

        elif eje == 'vertical' and self.comparteColumnaCon(casilla):
            direccion = True if (self.y - casilla.y) > 0 else False

        elif eje == 'diagonal' and self.comparteDiagonalCon(casilla):
            direccion = True if self.getPendiente(casilla) > 0 else False

        else:
            direccion = None

        return direccion


    def getPendiente(self, casilla):
        return (self.x - casilla.x) / (self.y - casilla.y)