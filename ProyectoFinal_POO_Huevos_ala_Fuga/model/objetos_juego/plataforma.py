import pygame

class Plataforma:
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.rect = pygame.Rect(x, y, ancho, alto)

    def actualizar(self):
        self.rect.x = self.x
        self.rect.y = self.y