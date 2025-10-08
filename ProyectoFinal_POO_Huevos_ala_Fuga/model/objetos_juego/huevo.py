import pygame
from ..estados import EstadoJuego
from config.configuracion import (
    VELOCIDAD_MOVIMIENTO, FUERZA_SALTO, GRAVEDAD, 
    ANCHO_PANTALLA, ALTO_PANTALLA, ANCHO_HUEVO, 
    ALTO_HUEVO, TIEMPO_INVULNERABILIDAD, 
    TIEMPO_INVULNERABILIDAD_POWERUP
)

class Huevo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 30
        self.alto = 40
        self.rect = pygame.Rect(x, y, self.ancho, self.alto)
        self.vel_x = 0
        self.vel_y = 0
        self.en_suelo = False
        self.grietas = 0
        self.invulnerable = False
        self.tiempo_invulnerable = 0
        self.aterrizaje_suave = False
        self.tiempo_aterrizaje_suave = 0

    def mover(self, direccion):
        self.vel_x = direccion * VELOCIDAD_MOVIMIENTO

    def saltar(self):
        if self.en_suelo:
            self.vel_y = FUERZA_SALTO
            self.en_suelo = False
            return True  
        return False     
    def recibir_daño(self):
        if not self.invulnerable:
            self.grietas += 1
            self.invulnerable = True
            self.tiempo_invulnerable = 60

    def aplicar_powerup(self, tipo_powerup):
        if tipo_powerup == "cascara":
            self.grietas = max(0, self.grietas - 1)
        elif tipo_powerup == "papel":
            self.invulnerable = True
            self.tiempo_invulnerable = 180
        elif tipo_powerup == "turbo":
            self.vel_x *= 1.5
            self.invulnerable = True
            self.tiempo_invulnerable = 180

    def actualizar(self, plataformas):
        if not self.en_suelo:
            self.vel_y += GRAVEDAD

        
        x_anterior = self.x
        y_anterior = self.y
        
        self.x += self.vel_x
        
        if self.x < 0:
            self.x = 0
        
        self.rect.x = self.x
        
        colision_x = False
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                colision_x = True
                if self.vel_x > 0:
                    self.x = plataforma.rect.left - self.ancho
                elif self.vel_x < 0:
                    self.x = plataforma.rect.right
                self.rect.x = self.x
                self.vel_x = 0
                break
        
        self.y += self.vel_y
        
        self.rect.y = self.y
        
        self.en_suelo = False
        
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                if self.vel_y > 0 and y_anterior + self.alto <= plataforma.rect.top + 5:
                    self.y = plataforma.rect.top - self.alto
                    self.vel_y = 0
                    self.en_suelo = True
                elif self.vel_y < 0 and y_anterior >= plataforma.rect.bottom - 5:
                    self.y = plataforma.rect.bottom
                    self.vel_y = 0
                self.rect.y = self.y
        
        if self.invulnerable:
            self.tiempo_invulnerable -= 1
            if self.tiempo_invulnerable <= 0:
                self.invulnerable = False

        if self.aterrizaje_suave:
            self.tiempo_aterrizaje_suave -= 1
            if self.tiempo_aterrizaje_suave <= 0:
                self.aterrizaje_suave = False