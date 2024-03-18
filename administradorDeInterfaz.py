import pygame as pg
import numpy as np
from tablero import Tablero
from sprite import SpriteCasilla, SpritePieza

class AdministradorDeInterfaz:

    pg.font.init()
    fuente_base = pg.font.SysFont("Arialblack", 16)
    tamanoVentanaPrincipal = Tablero.tamano
    tamanoCasilla = (tamanoVentanaPrincipal[0]/8, tamanoVentanaPrincipal[1]/8)
    origenDeDibujo = (0,0)

    mapaPiezas = {
    "peon_b" : pg.image.load(r"imagenes de piezas\w_pawn_png_128px.png"),
    "peon_n" : pg.image.load(r"imagenes de piezas\b_pawn_png_128px.png"),
    "alfil_b" : pg.image.load(r"imagenes de piezas\w_bishop_png_128px.png"),
    "alfil_n" : pg.image.load(r"imagenes de piezas\b_bishop_png_128px.png"),
    "caballo_b" : pg.image.load(r"imagenes de piezas\w_knight_png_128px.png"),
    "caballo_n" : pg.image.load(r"imagenes de piezas\b_knight_png_128px.png"),
    "torre_b" : pg.image.load(r"imagenes de piezas\w_rook_png_128px.png"),
    "torre_n" : pg.image.load(r"imagenes de piezas\b_rook_png_128px.png"),
    "reina_b" : pg.image.load(r"imagenes de piezas\w_queen_png_128px.png"),
    "reina_n" : pg.image.load(r"imagenes de piezas\b_queen_png_128px.png"),
    "rey_b" : pg.image.load(r"imagenes de piezas\w_king_png_128px.png"),
    "rey_n" : pg.image.load(r"imagenes de piezas\b_king_png_128px.png")
    }

    def __init__(self, tablero: Tablero):
        self.ventanaPrincipal = pg.display.set_mode(AdministradorDeInterfaz.tamanoVentanaPrincipal)
        self.setSpritesACasillas(tablero.casillas)
        self.setSpritesAPiezas(tablero.piezas)
        spritesCasillas = [casilla.sprite for casilla in tablero.casillas]
        spritesPiezas = [pieza.sprite for pieza in tablero.piezas]

        self.grupoSpritesCasillas = pg.sprite.Group(spritesCasillas) 
        self.grupoSpritesPiezas = pg.sprite.Group(spritesPiezas) 


    def setSpritesACasillas(self, casillas):
        imagenCasillaOscura = pg.image.load('imagenes de piezas\square_brown_dark_png_128px.png')
        imagenCasillaClara = pg.image.load('imagenes de piezas\square_gray_light_png_128px.png')
        listaCasillas = np.ravel(casillas)

        for casilla in listaCasillas:
            casilla.sprite = SpriteCasilla(imagenCasillaOscura) if casilla.color == 'oscura' else SpriteCasilla(imagenCasillaClara)
            casilla.sprite.actualizarPosicion(casilla)


    def setSpriteAPieza(self, pieza):
        nombre_de_pieza_sin_sufijo = pieza.nombre[:-2]
        imagen = AdministradorDeInterfaz.mapaPiezas[nombre_de_pieza_sin_sufijo]
        pieza.sprite = SpritePieza(self.aplicarAntialiasing(imagen, pieza.rect.size))


    def setSpritesAPiezas(self, piezas):
        for pieza in piezas:
            self.setSpriteAPieza(pieza)


    def imprimirTablero(self):
        self.grupoSpritesCasillas.update(self.ventanaPrincipal)
        self.grupoSpritesPiezas.update(self.ventanaPrincipal)
    

    def actualizarPosicionDePiezas(self, tablero):
        for casilla in tablero.casillas:
            if casilla.pieza:
                casilla.pieza.sprite.actualizarPosicion(casilla)


    def aplicarAntialiasing(self, imagen, tamano):
        imagen = imagen.convert_alpha()
        imagenEscaladaConAntialiasing = pg.transform.smoothscale(imagen, tamano)
        return imagenEscaladaConAntialiasing
    

    def mostrarMenuDePromocion(self):
        pass