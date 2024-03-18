import numpy as np
from casilla import Casilla
from pieza import Peon, Alfil, Caballo, Torre, Rey, Reina

class Tablero:
    tamano = (650, 650)
    tamanoCasilla = (tamano[0] / 8, tamano[1] / 8)
    anchoCasilla, altoCasilla = tamanoCasilla
    def __init__(self):
        self.casillas = self.agregarCasillas()
        self.piezas = self.agregarPiezas()
        self.piezasBlancas = self.piezas[:16]
        self.piezasNegras = self.piezas[16:]
        self.filaDePromocionDeNegras = 0
        self.filaDePromocionDeBlancas = 7
        self.setColorACasillas()
        self.acomodarPiezasEnPosicionInicial()
        self.setRectAPiezas()


    def __repr__(self) -> str:
        return self.casillas
    

    def agregarCasillas(self):
        x = np.arange(8)
        y = np.arange(8)
        X, Y = np.meshgrid(x,y)
        martizDeCoordenadasParaTablero = np.stack((X,Y), axis=-1)
        casillas = []
        for fila in martizDeCoordenadasParaTablero:
            for coordenadas in fila:
                casillas.append(Casilla(coordenadas))
        return casillas
    

    def crearPieza(self, nombre):
        if 'peon' in nombre:
            return Peon(self, nombre)
        elif 'alfil' in nombre:
            return Alfil(self, nombre)
        elif 'caballo' in nombre:
            return Caballo(self, nombre)
        elif 'torre' in nombre:
            return Torre(self, nombre)
        elif 'rey' in nombre:
            return Rey(self, nombre)
        elif 'reina' in nombre:
            return Reina(self, nombre)


    def agregarPiezas(self):
        nombres_ordenados_de_piezas = [
            "peon_b_0",
            "peon_b_1",
            "peon_b_2",
            "peon_b_3",
            "peon_b_4",
            "peon_b_5",
            "peon_b_6",
            "peon_b_7",
            "torre_b_0",
            "caballo_b_1",
            "alfil_b_2",
            "reina_b_3",
            "rey_b_4",
            "alfil_b_5",
            "caballo_b_6",
            "torre_b_7",
            "peon_n_0",
            "peon_n_1",
            "peon_n_2",
            "peon_n_3",
            "peon_n_4",
            "peon_n_5",
            "peon_n_6",
            "peon_n_7",
            "torre_n_0",
            "caballo_n_1",
            "alfil_n_2",
            "reina_n_3",
            "rey_n_4",
            "alfil_n_5",
            "caballo_n_6",
            "torre_n_7"]
        
        piezas = []
        for nombre in nombres_ordenados_de_piezas:
            pieza = self.crearPieza(nombre)
            piezas.append(pieza)

        piezas = np.array(piezas)

        indicesParaOrdenarPiezas = [ 0,1,2,3,4,5,6,7,
                                        8,9,10,11,12,13,14,15,

                                        16,17,18,19,20,21,22,23,
                                        24,25,26,27,28,29,30,31]

        piezasOrdenadas = piezas[indicesParaOrdenarPiezas]
        return list(piezasOrdenadas)


    def setColorACasillas(self):
        matrizTablero = np.reshape(self.casillas, (8,8))
        filasConIndices = enumerate(matrizTablero)
        for numeroDeFila, fila in filasConIndices:
            for casilla in fila:
                if numeroDeFila % 2:
                    casilla.color = 'clara' if casilla.x % 2 else 'oscura'
                else:
                    casilla.color = 'oscura' if casilla.x % 2 else 'clara'


    def setRectAPiezas(self):
        for casilla in self.casillas:
            if casilla.pieza:
                casilla.pieza.rect.x = casilla.rect[0] + 10
                casilla.pieza.rect.y = casilla.rect[1] + 10
                casilla.pieza.rect.width = casilla.rect.width * 0.8
                casilla.pieza.rect.height = casilla.rect.height * 0.8


    def colocarPiezasEnCasillas(self, casillas, piezas):
        for casilla, pieza in zip(casillas, piezas):
            casilla.pieza = pieza
            pieza.casilla = casilla


    def acomodarPiezasEnPosicionInicial(self):
        matrizTablero = np.reshape(self.casillas, (8,8))
        filaSiete = matrizTablero[7]
        filaSeis = matrizTablero[6]
        filaUno = matrizTablero[1]
        filaCero = matrizTablero[0]

        piezasBlancas = self.piezasBlancas[8:]
        peonesBlancas = self.piezasBlancas[:8]
        piezasNegras = self.piezasNegras[8:]
        peonesNegras = self.piezasNegras[:8]

        self.colocarPiezasEnCasillas(filaSiete, piezasBlancas)
        self.colocarPiezasEnCasillas(filaSeis, peonesBlancas)
        self.colocarPiezasEnCasillas(filaUno, peonesNegras)
        self.colocarPiezasEnCasillas(filaCero, piezasNegras)


    def getCasillaSeleccionada(self):
        for casilla in self.casillas:
            if casilla.seleccionada:
                return casilla