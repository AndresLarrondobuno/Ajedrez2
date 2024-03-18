import pygame as pg
from movimiento import Movimiento

class Pieza:
    def __init__(self, tablero, nombre):
        self.nombre = nombre
        self.casilla = None #se asigna al instanciarse el tablero
        self.tablero = tablero
        self.color = 'blancas' if '_b' in self.nombre else 'negras'
        self.sprite = None
        self.rect = pg.Rect((0,0,0,0))
        self.seleccionada = False


    def __repr__(self) -> str:
        return self.nombre
    

    def columna(self):
        pass
    

    def esPiezaEnemiga(self, piezaAtacada):
        return True if self.color != piezaAtacada.color else False
    

    def getCasillaOcupada(self):
        for casilla in self.tablero.casillas:
            if casilla.pieza == self:
                return casilla
    

    def getPiezasAtacadas(self):
        pass

    

    def respetaPatronDeMovimiento(self, movimiento):
        pass


    def comerPieza(self):
        pass


    def generarRuta(self, movimiento):
        pass
        

    def rutaDespejada(self):
        pass
    

    def diagonalDespejada(self):
        pass


    def filaDespejada(self):
        pass


    def columnaDespejada(self):
        pass


    def promoverA(self, nombre):
        nuevaPieza = self.tablero.crearPieza(nombre)
        nuevaPieza.sprite
   

class Peon(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)
        self.enCasillaInicial = True
        self.casilla_de_promocion = False
    

    def respetaPatronDeAtaque(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada =  movimiento.casillaAtacada

        comparteDiagonalConCasillaAtacada = casillaDePartida.comparteDiagonalCon(casillaAtacada)
        avanzaHaciaPromocion = self.avanzaHaciaPromocion(movimiento)
        return comparteDiagonalConCasillaAtacada and avanzaHaciaPromocion


    def respetaPatronDeMovimiento(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada =  movimiento.casillaAtacada

        atacaPiezaEnemiga = casillaAtacada.pieza and self.esPiezaEnemiga(casillaAtacada.pieza)
        distanciaOrtogonal = casillaDePartida.distanciaOrtogonal(casillaAtacada)
        compartenColumna = casillaDePartida.comparteColumnaCon(casillaAtacada)

        if self.avanzaHaciaPromocion(movimiento):

            if atacaPiezaEnemiga:
                if self.respetaPatronDeAtaque(movimiento):
                    return True
                else:
                    return False
                
            else:
                if self.enCasillaInicial:
                    return True if compartenColumna and (distanciaOrtogonal <= 2) else False
                else:
                    return True if compartenColumna and (distanciaOrtogonal == 1) else False


    def avanzaHaciaPromocion(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada =  movimiento.casillaAtacada
        if self.color == 'blancas':
            distanciaPreviaAlMovimiento = casillaDePartida.distanciaVertical(self.tablero.filaDePromocionDeBlancas)
            distanciaPosteriorAlMovimiento = casillaAtacada.distanciaVertical(self.tablero.filaDePromocionDeBlancas)
        else:
            distanciaPreviaAlMovimiento = casillaDePartida.distanciaVertical(self.tablero.filaDePromocionDeNegras)
            distanciaPosteriorAlMovimiento = casillaAtacada.distanciaVertical(self.tablero.filaDePromocionDeNegras)
        return True if distanciaPreviaAlMovimiento > distanciaPosteriorAlMovimiento else False
    

    def rutaDespejada(self):
        pass


    def columnaDespejada(self):
        pass


class Alfil(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)
        self.sprite = None


    def respetaPatronDeMovimiento(self, movimiento: Movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada =  movimiento.casillaAtacada
        return True if casillaDePartida.comparteDiagonalCon(casillaAtacada) else False


    def rutaDespejada(self):
        return True if self.diagonalDespejada() else False
    

    def diagonalDespejada(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada = movimiento.casillaAtacada
        casillasEnDiagonal = [casilla for casilla in self.tablero.casillas if casilla.comparteDiagonalCon(casillaDePartida)]

        for casilla in casillasEnDiagonal:
            if casillaDePartida.distanciaOrtogonal(casillaAtacada) > casillaDePartida.distanciaOrtogonal(casilla):
                return False
        return True


    def generarRuta(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada =  movimiento.casillaAtacada
        pendiente = (casillaDePartida.x - casillaAtacada.x) / (casillaDePartida.y - casillaAtacada.y)

    

class Caballo(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)
        self.sprite = None
        self.salta_piezas = True
    

    def respetaPatronDeMovimiento(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada =  movimiento.casillaAtacada

        noCompartenDiagonal = not casillaDePartida.comparteDiagonalCon(casillaAtacada)
        noSonOrtogonales = not casillaDePartida.ortogonalCon(casillaAtacada)
        distanciaOrtogonalValida = casillaDePartida.distanciaOrtogonal(casillaAtacada) <= 3

        return True if noCompartenDiagonal and noSonOrtogonales and distanciaOrtogonalValida else False


class Torre(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)
        self.sprite = None


    def respetaPatronDeMovimiento(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada =  movimiento.casillaAtacada
        return True if casillaDePartida.ortogonalCon(casillaAtacada) else False


    def generarRuta(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada =  movimiento.casillaAtacada
        ruta = list()

        for casilla in self.tablero.casillas:
            if casilla.perteneceARutaDelMovimiento(movimiento):
                if casilla not in  [casillaDePartida, casillaAtacada]:
                    ruta.append(casilla)
        print(len(ruta), ruta)
        return ruta


class Rey(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)
        self.enJaque = False



    def respetaPatronDeMovimiento(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada =  movimiento.casillaAtacada

        distanciaOrtogonal = casillaDePartida.distanciaOrtogonal(casillaAtacada)
        sonOrtogonales = casillaDePartida.ortogonalCon(casillaAtacada)
        compartenDiagonal = casillaDePartida.comparteDiagonalCon(casillaAtacada)
        
        condicionUno = sonOrtogonales and distanciaOrtogonal == 1
        condicionDos = compartenDiagonal and distanciaOrtogonal == 2
        return True if condicionUno or condicionDos else False


class Reina(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)
    
    def respetaPatronDeMovimiento(self, movimiento):
        casillaDePartida = movimiento.casillaDePartida
        casillaAtacada =  movimiento.casillaAtacada
        sonOrtogonales = casillaDePartida.ortogonalCon(casillaAtacada)
        compartenDiagonal = casillaDePartida.comparteDiagonalCon(casillaAtacada)
        return True if sonOrtogonales or compartenDiagonal else False