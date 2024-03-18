import pygame as pg

class SpriteCasilla(pg.sprite.Sprite):
    def __init__(self, imagen):
        super().__init__()
        self.image = imagen
        self.rect = pg.Rect(self.image.get_rect())
    

    def update(self, ventana:pg.Surface):
        x, y = self.rect.x, self.rect.y
        ventana.blit(self.image, (x,y))


    def actualizarPosicion(self, casilla):
        self.rect.x = casilla.rect.x
        self.rect.y = casilla.rect.y



class SpritePieza(pg.sprite.Sprite):
    def __init__(self, imagen):
        super().__init__()
        self.image = imagen
        self.rect = pg.Rect(self.image.get_rect())


    def __repr__(self) -> str:
        return str(self.rect)


    def update(self, ventana:pg.Surface):
        x, y = self.rect.x, self.rect.y
        ventana.blit(self.image, (x,y))
    

    def actualizarPosicion(self, casilla):
        if casilla.pieza.seleccionada:
            x, y = pg.mouse.get_pos()
            self.rect.x = x - 25
            self.rect.y = y - 25
        else:
            x, y = casilla.rect.x, casilla.rect.y
            self.rect.x = x + 10
            self.rect.y = y + 10