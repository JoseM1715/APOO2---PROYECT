import pygame
from config.configuracion import ANCHO_PANTALLA, ALTO_PANTALLA


class Camara:
    def __init__(self, ancho_nivel=2000):
        self.desplazamiento = 0
        self.ancho_nivel = ancho_nivel
        
    def actualizar(self, huevo):
        """Actualiza la posición de la cámara siguiendo al huevo"""
        # Mantener al huevo en el centro de la pantalla
        objetivo = huevo.x - ANCHO_PANTALLA // 2
        
        # Limitar el desplazamiento para no salir de los límites del nivel
        self.desplazamiento = max(0, min(objetivo, self.ancho_nivel - ANCHO_PANTALLA))
    
    def aplicar(self, rect):
        """Aplica el desplazamiento de la cámara a un rectángulo"""
        if isinstance(rect, pygame.Rect):
            return pygame.Rect(rect.x - self.desplazamiento, rect.y, rect.width, rect.height)
        else:
            # Si es una tupla (x, y, width, height)
            return pygame.Rect(rect[0] - self.desplazamiento, rect[1], rect[2], rect[3])

    def posicion_mundial_a_pantalla(self, x, y):
        return x - self.desplazamiento, y

    def posicion_pantalla_a_mundial(self, x, y):
        return x + self.desplazamiento, y