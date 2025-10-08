import pygame
from config.configuracion import *

def dibujar_menu_principal(pantalla):
    fuente = pygame.font.SysFont(None, 48)
    titulo = fuente.render("HUEVOS A LA FUGA", True, BLANCO)
    instruccion1 = fuente.render("Presiona ENTER para comenzar", True, BLANCO)
    instruccion2 = fuente.render("Presiona P para ver puntuaciones", True, BLANCO)
    
    pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 300)) # Centrar verticalmente en la pantalla
    pantalla.blit(instruccion1, (ANCHO_PANTALLA//2 - instruccion1.get_width()//2, 450))
    pantalla.blit(instruccion2, (ANCHO_PANTALLA//2 - instruccion2.get_width()//2, 520))

def dibujar_tabla_puntuaciones(pantalla, puntuaciones):
    fuente_titulo = pygame.font.SysFont(None, 48)
    fuente_lista = pygame.font.SysFont(None, 28)
    titulo = fuente_titulo.render("MEJORES PUNTUACIONES", True, BLANCO)
    pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 100))

    if not puntuaciones:
        mensaje = fuente_lista.render("No hay puntuaciones registradas", True, BLANCO)
        pantalla.blit(mensaje, (ANCHO_PANTALLA//2 - mensaje.get_width()//2, 300))
    else:
        for i, p in enumerate(puntuaciones[:5]): # Mostrar las 5 mejores puntuaciones
            texto = fuente_lista.render(f"{i+1}. {p['nombre']} - Nivel {p['nivel']} - {p['tiempo']}s", True, BLANCO)
            pantalla.blit(texto, (ANCHO_PANTALLA//2 - texto.get_width()//2, 200 + i*45))
    
    volver = fuente_lista.render("Presiona P para volver", True, BLANCO)
    pantalla.blit(volver, (ANCHO_PANTALLA//2 - volver.get_width()//2, 650))

def dibujar_menu_pausa(pantalla):
    fuente = pygame.font.SysFont(None, 48)
    titulo = fuente.render("PAUSA", True, BLANCO)
    instruccion1 = fuente.render("ESC - Continuar", True, BLANCO)
    instruccion2 = fuente.render("Q - Salir al menú", True, BLANCO)
    
    pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 350))
    pantalla.blit(instruccion1, (ANCHO_PANTALLA//2 - instruccion1.get_width()//2, 450))
    pantalla.blit(instruccion2, (ANCHO_PANTALLA//2 - instruccion2.get_width()//2, 520))

def dibujar_game_over(pantalla, nivel_actual):
    fuente = pygame.font.SysFont(None, 48)
    titulo = fuente.render("¡HUEVO ROTO!", True, ROJO)
    info_nivel = fuente.render(f"Llegaste al nivel {nivel_actual}", True, BLANCO)
    instruccion = fuente.render("Presiona ENTER para volver al menú", True, BLANCO)
    
    pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 300))
    pantalla.blit(info_nivel, (ANCHO_PANTALLA//2 - info_nivel.get_width()//2, 400))
    pantalla.blit(instruccion, (ANCHO_PANTALLA//2 - instruccion.get_width()//2, 500))

def dibujar_victoria(pantalla, tiempo_transcurrido):
    fuente = pygame.font.SysFont(None, 48)
    titulo = fuente.render("¡VICTORIA!", True, VERDE)
    info_tiempo = fuente.render(f"Tiempo: {tiempo_transcurrido} segundos", True, BLANCO)
    instruccion = fuente.render("Presiona ENTER para volver al menú", True, BLANCO)
    
    pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 300))
    pantalla.blit(info_tiempo, (ANCHO_PANTALLA//2 - info_tiempo.get_width()//2, 400))
    pantalla.blit(instruccion, (ANCHO_PANTALLA//2 - instruccion.get_width()//2, 500)) 