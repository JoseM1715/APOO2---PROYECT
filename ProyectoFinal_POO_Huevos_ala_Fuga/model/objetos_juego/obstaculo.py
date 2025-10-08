import pygame

class Obstaculo:
    def __init__(self, x, y, tipo_obstaculo):
        self.x = x
        self.y = y
        self.tipo = tipo_obstaculo
        
        if tipo_obstaculo == "sarten":
            self.ancho = 80
            self.alto = 30
            self.letal = True
        elif tipo_obstaculo == "aceite":
            self.ancho = 50
            self.alto = 20
            self.letal = False
            
        self.rect = pygame.Rect(x, y, self.ancho, self.alto)

    def actualizar(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def efecto(self, huevo):
        if self.tipo == "sarten" and not huevo.invulnerable:
            return "muerte"
        elif self.tipo == "aceite":
            huevo.vel_x *= 1.5
            if not huevo.aterrizaje_suave and not huevo.invulnerable:
                huevo.recibir_daño()
            return None