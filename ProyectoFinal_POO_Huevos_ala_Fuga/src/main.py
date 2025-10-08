import pygame
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.objetos_juego import Huevo
from model.estados import EstadoJuego
from src.logica.gestor_niveles import cargar_nivel
from model.objetos_juego.camara import Camara
from src.ui.render import (
    dibujar_menu, dibujar_juego, dibujar_pausa, 
    dibujar_game_over, dibujar_victoria, dibujar_ingreso_nombre
)
from src.utils.puntuaciones import guardar_puntuacion, cargar_puntuaciones
from config.configuracion import ANCHO_PANTALLA, ALTO_PANTALLA, MAX_NIVEL

def inicializar_pygame():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Huevos a la Fuga")
    reloj = pygame.time.Clock()
    return pantalla, reloj

def juego():
    pantalla, reloj = inicializar_pygame()
    
    estado_actual = EstadoJuego.MENU
    nivel_actual = 1
    tiempo_inicio = 0
    tiempo_transcurrido = 0
    
    nombre_actual = ""
    cursor_visible = True
    ultimo_cambio_cursor = pygame.time.get_ticks()
    
    plataformas, obstaculos, powerups, meta, ancho_nivel = cargar_nivel(nivel_actual)
    huevo = Huevo(50, ALTO_PANTALLA - 150)
    
    camara = Camara(ancho_nivel)
    
    mostrar_puntuaciones = False
    puntuaciones = []
    
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                
            if estado_actual == EstadoJuego.MENU:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        estado_actual = EstadoJuego.INGRESO_NOMBRE
                        nombre_actual = ""
                    elif evento.key == pygame.K_p:
                        mostrar_puntuaciones = not mostrar_puntuaciones
                        if mostrar_puntuaciones:
                            puntuaciones = cargar_puntuaciones()
            
            elif estado_actual == EstadoJuego.INGRESO_NOMBRE:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if nombre_actual.strip(): 
                            estado_actual = EstadoJuego.JUGANDO
                            tiempo_inicio = pygame.time.get_ticks()
                    elif evento.key == pygame.K_BACKSPACE:
                        nombre_actual = nombre_actual[:-1]
                    elif evento.key in [pygame.K_ESCAPE, pygame.K_TAB]:
                        pass
                    else:
                        if len(nombre_actual) < 15:
                            char = evento.unicode
                            if char.isprintable():
                                nombre_actual += char
                        
            elif estado_actual == EstadoJuego.JUGANDO:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        huevo.saltar()
                    elif evento.key == pygame.K_ESCAPE:
                        estado_actual = EstadoJuego.PAUSA
                        
            elif estado_actual == EstadoJuego.PAUSA:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        estado_actual = EstadoJuego.JUGANDO
                    elif evento.key == pygame.K_q:
                        estado_actual = EstadoJuego.MENU
                        
            elif estado_actual in [EstadoJuego.GAME_OVER, EstadoJuego.VICTORIA]:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        estado_actual = EstadoJuego.MENU
                        nivel_actual = 1
                        plataformas, obstaculos, powerups, meta, ancho_nivel = cargar_nivel(nivel_actual)
                        huevo = Huevo(50, ALTO_PANTALLA - 150)
                        camara = Camara(ancho_nivel)
        
        if estado_actual == EstadoJuego.INGRESO_NOMBRE:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - ultimo_cambio_cursor > 500:
                cursor_visible = not cursor_visible
                ultimo_cambio_cursor = tiempo_actual
        
        elif estado_actual == EstadoJuego.JUGANDO:
            tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio) // 1000
            
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
                huevo.mover(-1)
            elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
                huevo.mover(1)
            else:
                huevo.mover(0)
                
            if teclas[pygame.K_SPACE]:
                huevo.saltar()
            
            huevo.actualizar(plataformas)
            
            camara.actualizar(huevo)
            
            for obstaculo in obstaculos:
                obstaculo.actualizar()
                
            for powerup in powerups:
                powerup.actualizar()
            
            for obstaculo in obstaculos:
                rect_obstaculo = pygame.Rect(obstaculo.rect)
                rect_huevo = pygame.Rect(huevo.rect)
                
                if rect_huevo.colliderect(rect_obstaculo):
                    resultado = obstaculo.efecto(huevo)
                    if resultado == "muerte":
                        estado_actual = EstadoJuego.GAME_OVER
            
            for powerup in powerups[:]:
                if powerup.activo:
                    rect_powerup = pygame.Rect(powerup.rect)
                    rect_huevo = pygame.Rect(huevo.rect)
                    
                    if rect_huevo.colliderect(rect_powerup):
                        powerup.aplicar(huevo)
                        powerups.remove(powerup)
            
            rect_meta = pygame.Rect(meta)
            rect_huevo = pygame.Rect(huevo.rect)
            
            if rect_huevo.colliderect(rect_meta):
                if nivel_actual < MAX_NIVEL:
                    nivel_actual += 1
                    plataformas, obstaculos, powerups, meta, ancho_nivel = cargar_nivel(nivel_actual)
                    huevo = Huevo(50, ALTO_PANTALLA - 150)
                    camara = Camara(ancho_nivel) 
                else:
                    estado_actual = EstadoJuego.VICTORIA
                    guardar_puntuacion(nombre_actual, tiempo_transcurrido, nivel_actual)
            
            if huevo.grietas >= 3:
                estado_actual = EstadoJuego.GAME_OVER
        
        pantalla.fill((0, 0, 0)) 
        
        if estado_actual == EstadoJuego.MENU:
            dibujar_menu(pantalla, mostrar_puntuaciones, puntuaciones)
        
        elif estado_actual == EstadoJuego.INGRESO_NOMBRE:
            dibujar_ingreso_nombre(pantalla, nombre_actual, cursor_visible)
            
        elif estado_actual == EstadoJuego.JUGANDO:
            dibujar_juego(pantalla, plataformas, obstaculos, powerups, 
                         meta, huevo, nivel_actual, tiempo_transcurrido, camara)
            
        elif estado_actual == EstadoJuego.PAUSA:
            dibujar_pausa(pantalla)
            
        elif estado_actual == EstadoJuego.GAME_OVER:
            dibujar_game_over(pantalla, nivel_actual)
            
        elif estado_actual == EstadoJuego.VICTORIA:
            dibujar_victoria(pantalla, tiempo_transcurrido)
        
        pygame.display.flip()
        reloj.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    juego() 