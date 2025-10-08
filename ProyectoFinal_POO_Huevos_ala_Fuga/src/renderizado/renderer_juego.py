import pygame
from config.configuracion import *
from .renderer_huevo import dibujar_huevo

def dibujar_plataformas(pantalla, plataformas):
    for plataforma in plataformas:
        pygame.draw.rect(pantalla, AZUL, plataforma.rect)

def dibujar_obstaculos(pantalla, obstaculos):
    for obstaculo in obstaculos:
        if obstaculo.tipo == "sarten":
            pygame.draw.rect(pantalla, ROJO, obstaculo.rect)
        elif obstaculo.tipo == "aceite":
            pygame.draw.rect(pantalla, AMARILLO, obstaculo.rect)

def dibujar_powerups(pantalla, powerups):
    for powerup in powerups:
        if powerup.activo:
            pygame.draw.rect(pantalla, powerup.color, powerup.rect)

def dibujar_meta(pantalla, meta):
    pygame.draw.rect(pantalla, VERDE, meta)
    fuente_meta = pygame.font.SysFont(None, 24)
    texto_meta = fuente_meta.render("META", True, BLANCO)
    pantalla.blit(texto_meta, (meta.x - 20, meta.y - 30))

def dibujar_info_juego(pantalla, huevo, nivel_actual, tiempo_transcurrido):
    fuente = pygame.font.SysFont(None, 24)
    info_grietas = fuente.render(f"Grietas: {huevo.grietas}/{MAX_GRIETAS}", True, BLANCO)
    info_nivel = fuente.render(f"Nivel: {nivel_actual}", True, BLANCO)
    info_tiempo = fuente.render(f"Tiempo: {tiempo_transcurrido}s", True, BLANCO)
    
    pantalla.blit(info_grietas, (10, 10))
    pantalla.blit(info_nivel, (10, 40))
    pantalla.blit(info_tiempo, (10, 70))

def dibujar_nivel_completo(pantalla, plataformas, obstaculos, powerups, meta, huevo, nivel_actual, tiempo_transcurrido):
    dibujar_plataformas(pantalla, plataformas)
    dibujar_obstaculos(pantalla, obstaculos)
    dibujar_powerups(pantalla, powerups)
    dibujar_meta(pantalla, meta)
    dibujar_huevo(pantalla, huevo)
    dibujar_info_juego(pantalla, huevo, nivel_actual, tiempo_transcurrido) 