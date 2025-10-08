import pygame

class PowerUp:
    def __init__(self, x, y, tipo_powerup):
        self.x = x
        self.y = y
        self.tipo = tipo_powerup
        
        if tipo_powerup == "cascara":
            self.ancho = 25
            self.alto = 25
            self.color = (255, 255, 255)  
        elif tipo_powerup == "turbo":
            self.ancho = 25
            self.alto = 25
            self.color = (255, 165, 0) 
        elif tipo_powerup == "papel":
            self.ancho = 25
            self.alto = 25
            self.color = (192, 192, 192)  
        self.rect = pygame.Rect(x, y, self.ancho, self.alto)
        self.activo = True
        
    def actualizar(self):
        self.rect.x = self.x
        self.rect.y = self.y
        
    def aplicar(self, huevo):
        if not self.activo:
            return
        if self.tipo == "cascara":
            huevo.grietas = max(0, huevo.grietas - 1)
        elif self.tipo == "turbo":
            huevo.vel_x *= 1.5
            huevo.invulnerable = True
            huevo.tiempo_invulnerable = 180  
        elif self.tipo == "papel":
            huevo.invulnerable = True
            huevo.tiempo_invulnerable = 180  
            
        self.activo = False 