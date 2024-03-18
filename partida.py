import pygame as pg
from jugador import Jugador
from administradorDeInterfaz import AdministradorDeInterfaz
from tablero import Tablero
import numpy as np

class Partida:
    FPS = 60

    def __init__(self):
        self.tablero = Tablero()
        self.reloj = pg.time.Clock()

        self.arbitro = None
        self.administradorDeEventos = None
        self.administradorDeInterfaz = AdministradorDeInterfaz(self.tablero)
        self.jugadorBlancas = Jugador('blancas', self.tablero.piezasBlancas)
        self.jugadorNegras = Jugador('negras', self.tablero.piezasNegras)
        
        self.historialDePartida = np.array(list())
        self.turno = 1
        self.jugadorActivo = self.jugadorBlancas


    def guardarEstadoDeTableroEnHistorial(self):
        self.historialDePartida = np.append(self.historialDePartida, self.tablero.casillas.copy())


    def mostrarhistorialDePartida(self):
        for estadoDePartida in self.historialDePartida:
            print(estadoDePartida)
            print()