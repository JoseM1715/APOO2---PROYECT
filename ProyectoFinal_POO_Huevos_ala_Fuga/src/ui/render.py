import pygame
import math
import random
from config.configuracion import (
    ANCHO_PANTALLA, ALTO_PANTALLA, 
    BLANCO, NEGRO, ROJO, VERDE, AZUL, AMARILLO
)

CREMA = (255, 253, 208)
MARRON_CLARO = (210, 180, 140)
MARRON_OSCURO = (139, 69, 19)  
ROJO_COCINA = (178, 34, 34)
VERDE_COCINA = (0, 128, 0)
AZUL_COCINA = (70, 130, 180)
AMARILLO_COCINA = (255, 215, 0)

def obtener_nombre_nivel(nivel):
    nombres_niveles = {
        1: "Cocina Inicial",
        2: "Zona de Cocción", 
        3: "Gran Escape"
    }
    return nombres_niveles.get(nivel, f"Nivel {nivel}")

def dibujar_menu(pantalla, mostrar_puntuaciones, puntuaciones):
    pantalla.fill(CREMA)
    
    tamaño_azulejo = 50
    for y in range(0, ALTO_PANTALLA, tamaño_azulejo):
        for x in range(0, ANCHO_PANTALLA, tamaño_azulejo):
            pygame.draw.rect(pantalla, (240, 240, 200), (x, y, tamaño_azulejo, tamaño_azulejo), 1)
            
    for i in range(5):
        x = 100 + i * 150
        pygame.draw.rect(pantalla, MARRON_OSCURO, (x, 50, 80, 10))
        if i % 3 == 0:
            pygame.draw.circle(pantalla, MARRON_CLARO, (x + 40, 100), 20)
            pygame.draw.rect(pantalla, MARRON_CLARO, (x + 35, 100, 10, 40))
        elif i % 3 == 1:
            pygame.draw.circle(pantalla, (100, 100, 100), (x + 40, 110), 25)
            pygame.draw.rect(pantalla, MARRON_CLARO, (x + 60, 90, 15, 10))
        else:
            pygame.draw.rect(pantalla, MARRON_CLARO, (x + 30, 80, 20, 50))
            pygame.draw.rect(pantalla, MARRON_CLARO, (x + 25, 80, 30, 10))
    
    if mostrar_puntuaciones:
        pygame.draw.rect(pantalla, BLANCO, (ANCHO_PANTALLA//2 - 250, 180, 500, 300))
        pygame.draw.rect(pantalla, MARRON_OSCURO, (ANCHO_PANTALLA//2 - 250, 180, 500, 300), 5)
        fuente_titulo = pygame.font.SysFont("arial", 40, bold=True)
        titulo = fuente_titulo.render("MEJORES TIEMPOS", True, MARRON_OSCURO)
        pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 200))
        pygame.draw.line(pantalla, MARRON_OSCURO, 
                       (ANCHO_PANTALLA//2 - 200, 245), 
                       (ANCHO_PANTALLA//2 + 200, 245), 3)
        fuente_lista = pygame.font.SysFont("arial", 24)
        
        if not puntuaciones:
            mensaje = fuente_lista.render("Aún no hay puntuaciones registradas", True, MARRON_OSCURO)
            pantalla.blit(mensaje, (ANCHO_PANTALLA//2 - mensaje.get_width()//2, 300))
        else:
            encabezado = fuente_lista.render("Nombre         Nivel         Tiempo", True, MARRON_OSCURO)
            pantalla.blit(encabezado, (ANCHO_PANTALLA//2 - 200, 260))
            for i, p in enumerate(puntuaciones[:5]):
                color_fila = MARRON_OSCURO
                texto = fuente_lista.render(f"{p['nombre']}            {p['nivel']}             {p['tiempo']}s", True, color_fila)
                pantalla.blit(texto, (ANCHO_PANTALLA//2 - 200, 300 + i*40))
        boton_volver = pygame.Rect(ANCHO_PANTALLA//2 - 150, 500, 300, 50)
        pygame.draw.rect(pantalla, MARRON_CLARO, boton_volver, border_radius=10)
        pygame.draw.rect(pantalla, MARRON_OSCURO, boton_volver, 2, border_radius=10)
        fuente_boton = pygame.font.SysFont("arial", 22)
        volver = fuente_boton.render("Presiona P para volver", True, MARRON_OSCURO)
        pantalla.blit(volver, (boton_volver.centerx - volver.get_width()//2, 
                               boton_volver.centery - volver.get_height()//2))
    else:
        pygame.draw.rect(pantalla, MARRON_CLARO, (ANCHO_PANTALLA//2 - 300, 120, 600, 200), border_radius=15)
        pygame.draw.rect(pantalla, MARRON_OSCURO, (ANCHO_PANTALLA//2 - 300, 120, 600, 200), 5, border_radius=15)
        
        fuente_titulo = pygame.font.SysFont("arial", 60, bold=True)
        titulo = fuente_titulo.render("HUEVOS A LA FUGA", True, MARRON_OSCURO)
        pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 150))
        
        fuente_subtitulo = pygame.font.SysFont("arial", 24, italic=True)
        subtitulo = fuente_subtitulo.render("¡Ayuda al huevo a escapar de la cocina!", True, MARRON_OSCURO)
        pantalla.blit(subtitulo, (ANCHO_PANTALLA//2 - subtitulo.get_width()//2, 220))
        
        tamaño_huevo = 100
        pos_huevo_x = ANCHO_PANTALLA//2
        pos_huevo_y = 350
        
        pygame.draw.ellipse(pantalla, BLANCO, 
                          (pos_huevo_x - tamaño_huevo//2, pos_huevo_y, tamaño_huevo, tamaño_huevo * 1.3))
        
        ojo_izq_x = pos_huevo_x - 20
        ojo_der_x = pos_huevo_x + 20
        ojos_y = pos_huevo_y + 40
        
        pygame.draw.circle(pantalla, NEGRO, (ojo_izq_x, ojos_y), 8)
        pygame.draw.circle(pantalla, NEGRO, (ojo_der_x, ojos_y), 8)
        
        pygame.draw.arc(pantalla, NEGRO, 
                      (pos_huevo_x - 30, pos_huevo_y + 60, 60, 30), 
                      math.pi, 2*math.pi, 3)
    
    fuente_botones = pygame.font.SysFont("arial", 22)
    
    boton_jugar = pygame.Rect(ANCHO_PANTALLA//2 - 180, 500, 360, 50)
    pygame.draw.rect(pantalla, MARRON_CLARO, boton_jugar, border_radius=10)
    pygame.draw.rect(pantalla, MARRON_OSCURO, boton_jugar, 2, border_radius=10)
    
    instruccion1 = fuente_botones.render("Presiona ENTER para jugar", True, MARRON_OSCURO)
    pantalla.blit(instruccion1, (boton_jugar.centerx - instruccion1.get_width()//2, 
                                boton_jugar.centery - instruccion1.get_height()//2))
    
    boton_puntuaciones = pygame.Rect(ANCHO_PANTALLA//2 - 180, 570, 360, 50)
    pygame.draw.rect(pantalla, MARRON_CLARO, boton_puntuaciones, border_radius=10)
    pygame.draw.rect(pantalla, MARRON_OSCURO, boton_puntuaciones, 2, border_radius=10)
    
    instruccion2 = fuente_botones.render("Presiona P para puntuaciones", True, MARRON_OSCURO)
    pantalla.blit(instruccion2, (boton_puntuaciones.centerx - instruccion2.get_width()//2, 
                                boton_puntuaciones.centery - instruccion2.get_height()//2))

def dibujar_pausa(pantalla):
    s = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
    s.set_alpha(150)
    s.fill((50, 50, 50))
    pantalla.blit(s, (0, 0))

    pygame.draw.rect(pantalla, BLANCO, (ANCHO_PANTALLA//2 - 200, 150, 400, 300), border_radius=15)
    pygame.draw.rect(pantalla, MARRON_OSCURO, (ANCHO_PANTALLA//2 - 200, 150, 400, 300), 5, border_radius=15)
    fuente_titulo = pygame.font.SysFont("arial", 48, bold=True)
    titulo = fuente_titulo.render("PAUSA", True, MARRON_OSCURO)
    pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 180))
    pygame.draw.line(pantalla, MARRON_OSCURO, 
                   (ANCHO_PANTALLA//2 - 150, 230), 
                   (ANCHO_PANTALLA//2 + 150, 230), 3)

    fuente_botones = pygame.font.SysFont("arial", 22) 
    
    boton_continuar = pygame.Rect(ANCHO_PANTALLA//2 - 150, 280, 300, 50)
    pygame.draw.rect(pantalla, MARRON_CLARO, boton_continuar, border_radius=10)
    pygame.draw.rect(pantalla, MARRON_OSCURO, boton_continuar, 2, border_radius=10)
    
    instruccion1 = fuente_botones.render("ESC - Continuar", True, MARRON_OSCURO)
    pantalla.blit(instruccion1, (boton_continuar.centerx - instruccion1.get_width()//2, 
                               boton_continuar.centery - instruccion1.get_height()//2))
    
    boton_salir = pygame.Rect(ANCHO_PANTALLA//2 - 150, 350, 300, 50)
    pygame.draw.rect(pantalla, MARRON_CLARO, boton_salir, border_radius=10)
    pygame.draw.rect(pantalla, MARRON_OSCURO, boton_salir, 2, border_radius=10)
    
    instruccion2 = fuente_botones.render("Q - Salir al menú", True, MARRON_OSCURO)

    pantalla.blit(instruccion2, (boton_salir.centerx - instruccion2.get_width()//2, 
                               boton_salir.centery - instruccion2.get_height()//2))

def dibujar_game_over(pantalla, nivel_actual):
    pantalla.fill((50, 50, 50))
    pygame.draw.circle(pantalla, (100, 100, 100), (ANCHO_PANTALLA//2, ALTO_PANTALLA//2), 250)
    pygame.draw.circle(pantalla, (80, 80, 80), (ANCHO_PANTALLA//2, ALTO_PANTALLA//2), 230)
    pygame.draw.rect(pantalla, MARRON_CLARO, (ANCHO_PANTALLA//2 + 200, ALTO_PANTALLA//2 - 40, 150, 80), border_radius=10)
    centro_x = ANCHO_PANTALLA//2
    centro_y = ALTO_PANTALLA//2
    radio_clara = 120
    
    pygame.draw.ellipse(pantalla, (240, 240, 240), 
                      (centro_x - radio_clara, centro_y - radio_clara//1.3, 
                       radio_clara*2, radio_clara*1.8))
    
    for i in range(8):
        angulo = i * (math.pi / 4)
        offset_x = int(math.cos(angulo) * (radio_clara * 0.8))
        offset_y = int(math.sin(angulo) * (radio_clara * 0.8))
        tamaño_x = random.randint(30, 60)
        tamaño_y = random.randint(30, 60)
        pygame.draw.ellipse(pantalla, (240, 240, 240), 
                          (centro_x + offset_x - tamaño_x//2, centro_y + offset_y - tamaño_y//2,
                           tamaño_x, tamaño_y))
    
    for i in range(12):
        angulo = i * (math.pi / 6)
        offset_x = int(math.cos(angulo) * (radio_clara * 0.9))
        offset_y = int(math.sin(angulo) * (radio_clara * 0.9))
        
        pygame.draw.circle(pantalla, (220, 220, 220), 
                         (centro_x + offset_x, centro_y + offset_y), 15)
    radio_yema = 45
    pygame.draw.circle(pantalla, (255, 200, 30), (centro_x, centro_y), radio_yema)
    pygame.draw.circle(pantalla, (240, 180, 0), (centro_x, centro_y), radio_yema, 3)
    pygame.draw.ellipse(pantalla, (255, 230, 80), 
                      (centro_x - radio_yema//3, centro_y - radio_yema//2, 
                       radio_yema//2, radio_yema//3))
                       
    for i in range(8):
        burbuja_x = centro_x + random.randint(-radio_clara+20, radio_clara-20)
        burbuja_y = centro_y + random.randint(-radio_clara+20, radio_clara-20)
        distancia_centro = math.sqrt((burbuja_x - centro_x)**2 + (burbuja_y - centro_y)**2)
        if distancia_centro > radio_yema * 1.2:
            tamaño_burbuja = random.randint(3, 8)
            pygame.draw.circle(pantalla, (255, 255, 255), (burbuja_x, burbuja_y), tamaño_burbuja)
    
    pygame.draw.rect(pantalla, BLANCO, (ANCHO_PANTALLA//2 - 200, 150, 400, 300), border_radius=15)
    pygame.draw.rect(pantalla, ROJO_COCINA, (ANCHO_PANTALLA//2 - 200, 150, 400, 300), 5, border_radius=15)
    
    fuente_titulo = pygame.font.SysFont("arial", 48, bold=True)
    titulo = fuente_titulo.render("HUEVO ROTO", True, ROJO_COCINA)
    pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 180))
    pos_huevo_x = ANCHO_PANTALLA//2
    pos_huevo_y = 270
    
    pygame.draw.ellipse(pantalla, (240, 240, 240), 
                      (pos_huevo_x - 40, pos_huevo_y - 30, 80, 60))
    
    pygame.draw.circle(pantalla, AMARILLO_COCINA, (pos_huevo_x, pos_huevo_y), 20)
    pygame.draw.circle(pantalla, (240, 180, 0), (pos_huevo_x, pos_huevo_y), 20, 2)
    
    fuente_info = pygame.font.SysFont("arial", 24)
    info_nivel = fuente_info.render(f"Llegaste al nivel {nivel_actual}", True, MARRON_OSCURO)
    pantalla.blit(info_nivel, (ANCHO_PANTALLA//2 - info_nivel.get_width()//2, 350))
    
    boton_reiniciar = pygame.Rect(ANCHO_PANTALLA//2 - 180, 400, 360, 50)
    pygame.draw.rect(pantalla, MARRON_CLARO, boton_reiniciar, border_radius=10)
    pygame.draw.rect(pantalla, MARRON_OSCURO, boton_reiniciar, 2, border_radius=10)
    
    fuente_boton = pygame.font.SysFont("arial", 22)
    instruccion = fuente_boton.render("Presiona ENTER para volver al menú", True, MARRON_OSCURO)
    pantalla.blit(instruccion, (boton_reiniciar.centerx - instruccion.get_width()//2, 
                              boton_reiniciar.centery - instruccion.get_height()//2))


def dibujar_juego(pantalla, plataformas, obstaculos, powerups, meta, huevo, nivel_actual, tiempo_transcurrido, camara):
    tiempo_actual = pygame.time.get_ticks()
    superficie = pantalla
    if nivel_actual == 3:
        superficie = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
    superficie.fill(CREMA)
    tamaño_azulejo = 50
    for y in range(0, ALTO_PANTALLA - 50, tamaño_azulejo):
        for x in range(0, ANCHO_PANTALLA, tamaño_azulejo):
            x_ajustado = (x - int(camara.desplazamiento * 0.3) % tamaño_azulejo)
            pygame.draw.rect(superficie, (220, 220, 200), (x_ajustado, y, tamaño_azulejo, tamaño_azulejo), 1)
    pygame.draw.rect(superficie, MARRON_CLARO, (0, ALTO_PANTALLA - 50, ANCHO_PANTALLA, 50))
    pygame.draw.line(superficie, MARRON_OSCURO, (0, ALTO_PANTALLA - 50), (ANCHO_PANTALLA, ALTO_PANTALLA - 50), 3)
    nevera_x = 50 - camara.desplazamiento
    if -200 <= nevera_x <= ANCHO_PANTALLA:
        pygame.draw.rect(superficie, (230, 230, 230), (nevera_x, ALTO_PANTALLA - 300, 120, 250))
        pygame.draw.rect(superficie, (200, 200, 200), (nevera_x, ALTO_PANTALLA - 300, 120, 250), 3)
        pygame.draw.rect(superficie, (240, 240, 240), (nevera_x + 5, ALTO_PANTALLA - 295, 110, 80))
        pygame.draw.rect(superficie, (200, 200, 200), (nevera_x + 5, ALTO_PANTALLA - 295, 110, 80), 2)
        pygame.draw.rect(superficie, (240, 240, 240), (nevera_x + 5, ALTO_PANTALLA - 210, 110, 155))
        pygame.draw.rect(superficie, (200, 200, 200), (nevera_x + 5, ALTO_PANTALLA - 210, 110, 155), 2)
        pygame.draw.rect(superficie, (180, 180, 180), (nevera_x + 100, ALTO_PANTALLA - 260, 10, 30))
        pygame.draw.rect(superficie, (180, 180, 180), (nevera_x + 100, ALTO_PANTALLA - 140, 10, 30))
        if huevo.x < 200:
            pygame.draw.rect(superficie, (220, 220, 220), (nevera_x + 5, ALTO_PANTALLA - 210, 110, 155), 0)
            pygame.draw.line(superficie, (200, 200, 200),
                             (nevera_x + 115, ALTO_PANTALLA - 210),
                             (nevera_x + 115, ALTO_PANTALLA - 55), 2)
            pygame.draw.rect(superficie, (250, 250, 255), (nevera_x + 10, ALTO_PANTALLA - 205, 100, 145))
            pygame.draw.line(superficie, (230, 230, 230),
                             (nevera_x + 10, ALTO_PANTALLA - 150),
                             (nevera_x + 110, ALTO_PANTALLA - 150), 2)
            pygame.draw.line(superficie, (230, 230, 230),
                             (nevera_x + 10, ALTO_PANTALLA - 100),
                             (nevera_x + 110, ALTO_PANTALLA - 100), 2)
            if huevo.x < 100:
                pygame.draw.rect(superficie, (250, 240, 230), (nevera_x + 30, ALTO_PANTALLA - 130, 60, 20))
                for i in range(3):
                    pygame.draw.circle(superficie, (245, 245, 245),
                                       (nevera_x + 40 + i * 20, ALTO_PANTALLA - 120), 8)
        pygame.draw.circle(superficie, (255, 255, 100, 50), (nevera_x + 60, ALTO_PANTALLA - 180),
                           40 if huevo.x < 200 else 0)
    fuente_nivel = pygame.font.SysFont("arial", 20, bold=True)
    nombre_nivel = obtener_nombre_nivel(nivel_actual)
    texto_nivel = fuente_nivel.render(nombre_nivel, True, MARRON_OSCURO)
    ancho_panel = texto_nivel.get_width() + 20
    panel_nivel = pygame.Rect(ANCHO_PANTALLA // 2 - ancho_panel // 2, 5, ancho_panel, 30)
    pygame.draw.rect(superficie, BLANCO, panel_nivel, border_radius=8)
    pygame.draw.rect(superficie, MARRON_OSCURO, panel_nivel, 2, border_radius=8)
    superficie.blit(texto_nivel, (panel_nivel.centerx - texto_nivel.get_width() // 2,
                                  panel_nivel.centery - texto_nivel.get_height() // 2))
    ancho_nivel = camara.ancho_nivel
    progreso = min(1.0, huevo.x / ancho_nivel)
    pygame.draw.rect(superficie, (100, 100, 100), (10, 40, ANCHO_PANTALLA - 20, 20), border_radius=5)
    pygame.draw.rect(superficie, ROJO_COCINA, (10, 40, int((ANCHO_PANTALLA - 20) * progreso), 20), border_radius=5)
    meta_pantalla = camara.aplicar(meta)
    if meta_pantalla.right >= -50 and meta_pantalla.left <= ANCHO_PANTALLA + 50:
        pygame.draw.rect(superficie, (160, 82, 45),
                         (meta_pantalla.x - 20, meta_pantalla.y - 30,
                          meta_pantalla.width + 40, meta_pantalla.height + 40))
        pygame.draw.rect(superficie, (135, 206, 235), meta_pantalla)
        pygame.draw.line(superficie, (160, 82, 45),
                         (meta_pantalla.x, meta_pantalla.y + meta_pantalla.height // 2),
                         (meta_pantalla.x + meta_pantalla.width, meta_pantalla.y + meta_pantalla.height // 2), 4)
        pygame.draw.line(superficie, (160, 82, 45),
                         (meta_pantalla.x + meta_pantalla.width // 2, meta_pantalla.y),
                         (meta_pantalla.x + meta_pantalla.width // 2, meta_pantalla.y + meta_pantalla.height), 4)
        brillo_offset = int(math.sin(tiempo_actual / 500) * 10)
        pygame.draw.polygon(superficie, (255, 255, 255, 128), [
            (meta_pantalla.x + 10, meta_pantalla.y + 10),
            (meta_pantalla.x + 30 + brillo_offset, meta_pantalla.y + 5),
            (meta_pantalla.x + 20, meta_pantalla.y + 30 + brillo_offset)
        ])
        fuente_pequeña = pygame.font.SysFont("arial", 14)
        texto_meta = fuente_pequeña.render("META", True, VERDE_COCINA)
        superficie.blit(texto_meta, (meta_pantalla.x + meta_pantalla.width // 2 - texto_meta.get_width() // 2,
                                     meta_pantalla.y - 25))
    for i, plataforma in enumerate(plataformas):
        rect_pantalla = camara.aplicar(plataforma.rect)
        if rect_pantalla.right >= -50 and rect_pantalla.left <= ANCHO_PANTALLA + 50:
            offset_y = 0
            rotacion = 0
            if i % 4 == 0:
                pygame.draw.rect(superficie, MARRON_CLARO, rect_pantalla)
                pygame.draw.rect(superficie, MARRON_OSCURO, rect_pantalla, 2)
                for j in range(0, rect_pantalla.width, 10):
                    pygame.draw.line(superficie, MARRON_OSCURO,
                                     (rect_pantalla.x + j, rect_pantalla.y),
                                     (rect_pantalla.x + j, rect_pantalla.y + rect_pantalla.height), 1)
                for j in range(3):
                    x_mancha = rect_pantalla.x + j * rect_pantalla.width // 4 + rect_pantalla.width // 8
                    y_mancha = rect_pantalla.y + rect_pantalla.height // 2
                    radio = rect_pantalla.height // 4
                    pygame.draw.circle(superficie, MARRON_OSCURO, (x_mancha, y_mancha), radio, 1)

            elif i % 4 == 1:
                offset_y = int(math.sin(tiempo_actual / 300 + i) * 5)
                rotacion = math.sin(tiempo_actual / 500 + i) * 10
                ancho_cuchillo = rect_pantalla.width
                alto_cuchillo = rect_pantalla.height
                cuchillo_surf = pygame.Surface((ancho_cuchillo * 1.5, alto_cuchillo * 1.5), pygame.SRCALPHA)
                pygame.draw.rect(cuchillo_surf, (192, 192, 192),
                                 (ancho_cuchillo * 0.25, alto_cuchillo * 0.6,
                                  ancho_cuchillo * 0.6, alto_cuchillo * 0.2))
                pygame.draw.polygon(cuchillo_surf, (192, 192, 192), [
                    (ancho_cuchillo * 0.85, alto_cuchillo * 0.6),
                    (ancho_cuchillo * 0.95, alto_cuchillo * 0.7),
                    (ancho_cuchillo * 0.85, alto_cuchillo * 0.8),
                ])
                pygame.draw.rect(cuchillo_surf, MARRON_OSCURO,
                                 (ancho_cuchillo * 0.15, alto_cuchillo * 0.65,
                                  ancho_cuchillo * 0.2, alto_cuchillo * 0.1), border_radius=2)
                cuchillo_rot = pygame.transform.rotate(cuchillo_surf, rotacion)
                rot_rect = cuchillo_rot.get_rect(center=(rect_pantalla.centerx, rect_pantalla.centery + offset_y))
                superficie.blit(cuchillo_rot, rot_rect)
            elif i % 4 == 2:
                offset_y = int(math.sin(tiempo_actual / 400 + i) * 8)
                pygame.draw.rect(superficie, MARRON_CLARO,
                                 (rect_pantalla.x, rect_pantalla.y + offset_y + rect_pantalla.height // 4,
                                  rect_pantalla.width * 0.7, rect_pantalla.height // 2))
                pygame.draw.rect(superficie, (200, 200, 200),
                                 (rect_pantalla.x + rect_pantalla.width * 0.7, rect_pantalla.y + offset_y,
                                  rect_pantalla.width * 0.3, rect_pantalla.height), border_radius=5)
            elif i % 4 == 3:
                centro_x = rect_pantalla.centerx
                centro_y = rect_pantalla.centery
                rotacion = (tiempo_actual / 100) % 360
                tam_batidor = max(rect_pantalla.width, rect_pantalla.height) * 1.2
                batidor_surf = pygame.Surface((tam_batidor, tam_batidor), pygame.SRCALPHA)
                pygame.draw.rect(batidor_surf, MARRON_CLARO,
                                 (tam_batidor // 2 - 5, tam_batidor // 4,
                                  10, tam_batidor // 2))
                for j in range(8):
                    angulo = j * math.pi / 4
                    x1 = tam_batidor // 2 + int(math.cos(angulo) * tam_batidor // 8)
                    y1 = tam_batidor // 4 + int(math.sin(angulo) * tam_batidor // 8)
                    x2 = tam_batidor // 2 + int(math.cos(angulo) * tam_batidor // 4)
                    y2 = tam_batidor // 4 + int(math.sin(angulo) * tam_batidor // 4)
                    pygame.draw.line(batidor_surf, (150, 150, 150), (x1, y1), (x2, y2), 2)
                pygame.draw.circle(batidor_surf, (150, 150, 150),
                                   (tam_batidor // 2, tam_batidor // 4), tam_batidor // 8, 1)
                pygame.draw.circle(batidor_surf, (150, 150, 150),
                                   (tam_batidor // 2, tam_batidor // 4), tam_batidor // 6, 1)
                pygame.draw.circle(batidor_surf, (150, 150, 150),
                                   (tam_batidor // 2, tam_batidor // 4), tam_batidor // 4, 1)
                batidor_rot = pygame.transform.rotate(batidor_surf, rotacion)
                rot_rect = batidor_rot.get_rect(center=(centro_x, centro_y))
                pantalla.blit(batidor_rot, rot_rect)
    for obstaculo in obstaculos:
        rect_pantalla = camara.aplicar(obstaculo.rect)
        if rect_pantalla.right >= -50 and rect_pantalla.left <= ANCHO_PANTALLA + 50:
            if obstaculo.tipo == "sarten":
                centro_x = rect_pantalla.x + rect_pantalla.width // 2
                centro_y = rect_pantalla.y + rect_pantalla.height // 2
                angulo = math.sin(tiempo_actual / 500) * 15
                tamaño_sarten = max(rect_pantalla.width, rect_pantalla.height) * 1.5
                sarten_surf = pygame.Surface((tamaño_sarten, tamaño_sarten), pygame.SRCALPHA)
                pygame.draw.ellipse(sarten_surf, (80, 80, 80),
                                    (tamaño_sarten // 4, tamaño_sarten // 4,
                                     tamaño_sarten // 2, tamaño_sarten // 2))
                pygame.draw.ellipse(sarten_surf, (40, 40, 40),
                                    (tamaño_sarten // 4 + 4, tamaño_sarten // 4 + 4,
                                     tamaño_sarten // 2 - 8, tamaño_sarten // 2 - 8))
                pygame.draw.rect(sarten_surf, MARRON_CLARO,
                                 (tamaño_sarten // 4 + tamaño_sarten // 2 - 5, tamaño_sarten // 2 - 8,
                                  tamaño_sarten // 4, 16), border_radius=5)
                pygame.draw.arc(sarten_surf, (120, 120, 120),
                                (tamaño_sarten // 4 + 8, tamaño_sarten // 4 + 8,
                                 tamaño_sarten // 4, tamaño_sarten // 4),
                                math.pi / 4, math.pi, 2)
                sarten_rot = pygame.transform.rotate(sarten_surf, angulo)
                rot_rect = sarten_rot.get_rect(center=(centro_x, centro_y))
                pantalla.blit(sarten_rot, rot_rect)
            elif obstaculo.tipo == "aceite":
                pygame.draw.ellipse(pantalla, (200, 180, 20), rect_pantalla)
                for i in range(3):
                    factor = 0.8 - i * 0.2
                    color = (220, 200, 20)
                    pygame.draw.ellipse(pantalla, color,
                                        rect_pantalla.inflate(-rect_pantalla.width * 0.3 * i,
                                                              -rect_pantalla.height * 0.3 * i))
                num_brillos = 3
                for i in range(num_brillos):
                    offset_x = math.sin((tiempo_actual / 1000) + i * math.pi * 2 / num_brillos) * (
                                rect_pantalla.width * 0.3)
                    offset_y = math.cos((tiempo_actual / 800) + i * math.pi * 2 / num_brillos) * (
                                rect_pantalla.height * 0.3)
                    tam_brillo = 3 + math.sin((tiempo_actual / 600) + i) * 2
                    pygame.draw.circle(pantalla, (255, 255, 180),
                                       (rect_pantalla.x + rect_pantalla.width // 2 + int(offset_x),
                                        rect_pantalla.y + rect_pantalla.height // 2 + int(offset_y)),
                                       tam_brillo)
    for powerup in powerups:
        if powerup.activo:
            rect_pantalla = camara.aplicar(powerup.rect)
            if rect_pantalla.right >= -50 and rect_pantalla.left <= ANCHO_PANTALLA + 50:
                if powerup.tipo == "cascara":
                    pygame.draw.ellipse(pantalla, BLANCO, rect_pantalla)
                    pygame.draw.ellipse(pantalla, (240, 240, 240), rect_pantalla.inflate(-4, -4))
                elif powerup.tipo == "turbo":
                    pygame.draw.rect(pantalla, MARRON_OSCURO, rect_pantalla)
                    pygame.draw.rect(pantalla, BLANCO,
                                     (rect_pantalla.x - 3, rect_pantalla.y + 3,
                                      rect_pantalla.width + 6, rect_pantalla.height))
                    pygame.draw.arc(pantalla, BLANCO,
                                    (rect_pantalla.x + rect_pantalla.width, rect_pantalla.y,
                                     10, rect_pantalla.height),
                                    -math.pi / 2, math.pi / 2, 2)
                elif powerup.tipo == "papel":
                    pygame.draw.rect(pantalla, (192, 192, 192), rect_pantalla)
                    pygame.draw.line(pantalla, (220, 220, 220),
                                     (rect_pantalla.x, rect_pantalla.y),
                                     (rect_pantalla.x + rect_pantalla.width, rect_pantalla.y + rect_pantalla.height), 1)
                    pygame.draw.line(pantalla, (220, 220, 220),
                                     (rect_pantalla.x + rect_pantalla.width, rect_pantalla.y),
                                     (rect_pantalla.x, rect_pantalla.y + rect_pantalla.height), 1)
    color_huevo = BLANCO
    if huevo.invulnerable:
        if pygame.time.get_ticks() % 200 < 100:
            color_huevo = (220, 220, 255)
    huevo_rect_pantalla = camara.aplicar(huevo.rect)
    pygame.draw.ellipse(pantalla, color_huevo, huevo_rect_pantalla)
    ojo_izq_x = huevo_rect_pantalla.x + huevo_rect_pantalla.width // 3
    ojo_der_x = huevo_rect_pantalla.x + huevo_rect_pantalla.width * 2 // 3
    ojos_y = huevo_rect_pantalla.y + huevo_rect_pantalla.height // 3
    pygame.draw.circle(pantalla, NEGRO, (ojo_izq_x, ojos_y), 4)
    pygame.draw.circle(pantalla, NEGRO, (ojo_der_x, ojos_y), 4)
    pygame.draw.arc(pantalla, NEGRO,
                    (huevo_rect_pantalla.x + huevo_rect_pantalla.width // 4,
                     huevo_rect_pantalla.y + huevo_rect_pantalla.height // 2,
                     huevo_rect_pantalla.width // 2, 15),
                    math.pi, 2 * math.pi, 2)
    if huevo.grietas > 0:
        for i in range(huevo.grietas):
            inicio_x = huevo_rect_pantalla.x + huevo_rect_pantalla.width * (0.3 + i * 0.2)
            inicio_y = huevo_rect_pantalla.y + huevo_rect_pantalla.height * 0.2
            fin_y = huevo_rect_pantalla.y + huevo_rect_pantalla.height * 0.6
            medio_x = inicio_x + (5 if i % 2 == 0 else -5)
            medio_y = (inicio_y + fin_y) / 2
            pygame.draw.line(pantalla, (100, 100, 100), (inicio_x, inicio_y), (medio_x, medio_y), 2)
            pygame.draw.line(pantalla, (100, 100, 100), (medio_x, medio_y), (inicio_x, fin_y), 2)
    pygame.draw.rect(pantalla, BLANCO, (5, 70, 180, 100), border_radius=5)
    pygame.draw.rect(pantalla, MARRON_OSCURO, (5, 70, 180, 100), 2, border_radius=5)
    fuente = pygame.font.SysFont("arial", 16)
    info_grietas = fuente.render(f"Grietas: {huevo.grietas}/3", True, MARRON_OSCURO)
    info_nivel = fuente.render(f"Nivel: {nivel_actual}", True, MARRON_OSCURO)
    info_tiempo = fuente.render(f"Tiempo: {tiempo_transcurrido}s", True, MARRON_OSCURO)
    pantalla.blit(info_grietas, (15, 80))
    pantalla.blit(info_nivel, (15, 105))
    pantalla.blit(info_tiempo, (15, 130))
    recuadro_controles = pygame.Rect(ANCHO_PANTALLA // 2 - 180, ALTO_PANTALLA - 30, 360, 25)
    s_controles = pygame.Surface((recuadro_controles.width, recuadro_controles.height))
    s_controles.set_alpha(180)
    s_controles.fill((50, 50, 50))
    pantalla.blit(s_controles, recuadro_controles)
    fuente_controles = pygame.font.SysFont("arial", 14)
    texto_controles = fuente_controles.render("← → : Mover   ESPACIO : Saltar   ESC : Pausa", True, BLANCO)
    pantalla.blit(texto_controles, (recuadro_controles.centerx - texto_controles.get_width() // 2,
                                    recuadro_controles.centery - texto_controles.get_height() // 2))

def dibujar_victoria(pantalla, tiempo_transcurrido):
        pantalla.fill((220, 240, 255))
        pygame.draw.circle(pantalla, (255, 255, 200), (ANCHO_PANTALLA // 2, 100), 80)
        pygame.draw.circle(pantalla, (255, 255, 150), (ANCHO_PANTALLA // 2, 100), 50)
        for y in range(200, ALTO_PANTALLA, 150):
            pygame.draw.rect(pantalla, (200, 200, 200), (50, y, ANCHO_PANTALLA - 100, 5))

        pygame.draw.rect(pantalla, BLANCO, (ANCHO_PANTALLA // 2 - 200, 150, 400, 300), border_radius=15)
        pygame.draw.rect(pantalla, VERDE_COCINA, (ANCHO_PANTALLA // 2 - 200, 150, 400, 300), 5, border_radius=15)
        fuente_titulo = pygame.font.SysFont("arial", 48, bold=True)
        titulo = fuente_titulo.render("¡VICTORIA!", True, VERDE_COCINA)
        pantalla.blit(titulo, (ANCHO_PANTALLA // 2 - titulo.get_width() // 2, 180))

        tamaño_huevo = 80
        pos_huevo_x = ANCHO_PANTALLA // 2
        pos_huevo_y = 270

        pygame.draw.ellipse(pantalla, BLANCO,
                            (pos_huevo_x - tamaño_huevo // 2, pos_huevo_y,
                             tamaño_huevo, tamaño_huevo * 1.3))

        pygame.draw.rect(pantalla, BLANCO,
                         (pos_huevo_x - tamaño_huevo // 2 - 10, pos_huevo_y - 10,
                          tamaño_huevo + 20, 20))
        pygame.draw.rect(pantalla, BLANCO,
                         (pos_huevo_x - tamaño_huevo // 4, pos_huevo_y - 40,
                          tamaño_huevo // 2, 40))

        pygame.draw.circle(pantalla, NEGRO, (pos_huevo_x - tamaño_huevo // 4, pos_huevo_y + tamaño_huevo // 2), 5)
        pygame.draw.circle(pantalla, NEGRO, (pos_huevo_x + tamaño_huevo // 4, pos_huevo_y + tamaño_huevo // 2), 5)
        pygame.draw.arc(pantalla, NEGRO,
                        (pos_huevo_x - tamaño_huevo // 4, pos_huevo_y + tamaño_huevo // 2 + 10,
                         tamaño_huevo // 2, tamaño_huevo // 4),
                        math.pi, 2 * math.pi, 2)

        fuente_info = pygame.font.SysFont("arial", 24)
        info_tiempo = fuente_info.render(f"Tiempo: {tiempo_transcurrido} segundos", True, MARRON_OSCURO)
        pantalla.blit(info_tiempo, (ANCHO_PANTALLA // 2 - info_tiempo.get_width() // 2, 370))

        boton_volver = pygame.Rect(ANCHO_PANTALLA // 2 - 180, 400, 360, 50)
        pygame.draw.rect(pantalla, MARRON_CLARO, boton_volver, border_radius=10)
        pygame.draw.rect(pantalla, MARRON_OSCURO, boton_volver, 2, border_radius=10)

        fuente_boton = pygame.font.SysFont("arial", 22)
        instruccion = fuente_boton.render("Presiona ENTER para volver al menú", True, MARRON_OSCURO)
        pantalla.blit(instruccion, (boton_volver.centerx - instruccion.get_width() // 2,
                                    boton_volver.centery - instruccion.get_height() // 2))

def dibujar_ingreso_nombre(pantalla, nombre_actual="", cursor_visible=True):
        pantalla.fill(CREMA)
        tamaño_azulejo = 50
        for y in range(0, ALTO_PANTALLA, tamaño_azulejo):
            for x in range(0, ANCHO_PANTALLA, tamaño_azulejo):
                pygame.draw.rect(pantalla, (240, 240, 200), (x, y, tamaño_azulejo, tamaño_azulejo), 1)
        for i in range(5):
            x = 100 + i * 150
            pygame.draw.rect(pantalla, MARRON_OSCURO, (x, 50, 80, 10))
            if i % 3 == 0:
                pygame.draw.circle(pantalla, MARRON_CLARO, (x + 40, 100), 20)
                pygame.draw.rect(pantalla, MARRON_CLARO, (x + 35, 100, 10, 40))
            elif i % 3 == 1:
                pygame.draw.circle(pantalla, (100, 100, 100), (x + 40, 110), 25)
                pygame.draw.rect(pantalla, MARRON_CLARO, (x + 60, 90, 15, 10))
            else:
                pygame.draw.rect(pantalla, MARRON_CLARO, (x + 30, 80, 20, 50))
                pygame.draw.rect(pantalla, MARRON_CLARO, (x + 25, 80, 30, 10))
        panel_rect = pygame.Rect(ANCHO_PANTALLA // 2 - 250, 170, 500, 300)
        pygame.draw.rect(pantalla, BLANCO, panel_rect, border_radius=15)
        pygame.draw.rect(pantalla, MARRON_OSCURO, panel_rect, 5, border_radius=15)
        fuente_titulo = pygame.font.SysFont("arial", 36, bold=True)
        titulo = fuente_titulo.render("Ingresa tu nombre", True, MARRON_OSCURO)
        pantalla.blit(titulo, (ANCHO_PANTALLA // 2 - titulo.get_width() // 2, 200))
        pygame.draw.line(pantalla, MARRON_OSCURO,
                         (ANCHO_PANTALLA // 2 - 150, 250),
                         (ANCHO_PANTALLA // 2 + 150, 250), 3)
        caja_texto_rect = pygame.Rect(ANCHO_PANTALLA // 2 - 150, 300, 300, 40)
        pygame.draw.rect(pantalla, (240, 240, 240), caja_texto_rect, border_radius=5)
        pygame.draw.rect(pantalla, MARRON_OSCURO, caja_texto_rect, 2, border_radius=5)
        fuente_texto = pygame.font.SysFont("arial", 24)
        texto_mostrar = nombre_actual
        if cursor_visible:
            texto_mostrar += "|"
        texto_render = fuente_texto.render(texto_mostrar, True, NEGRO)
        if texto_render.get_width() > caja_texto_rect.width - 20:
            offset = texto_render.get_width() - (caja_texto_rect.width - 20)
            pantalla.blit(texto_render, (caja_texto_rect.x + 10 - offset, caja_texto_rect.y + 10))
        else:
            pantalla.blit(texto_render, (caja_texto_rect.x + 10, caja_texto_rect.y + 10))
        fuente_instrucciones = pygame.font.SysFont("arial", 18)
        instruccion1 = fuente_instrucciones.render("Usa el teclado para escribir tu nombre", True, MARRON_OSCURO)
        instruccion2 = fuente_instrucciones.render("Presiona ENTER para confirmar", True, MARRON_OSCURO)
        pantalla.blit(instruccion1, (ANCHO_PANTALLA // 2 - instruccion1.get_width() // 2, 360))
        pantalla.blit(instruccion2, (ANCHO_PANTALLA // 2 - instruccion2.get_width() // 2, 390))
        huevo_x = ANCHO_PANTALLA // 2 + 180
        huevo_y = 300
        pygame.draw.ellipse(pantalla, BLANCO, (huevo_x - 20, huevo_y - 30, 40, 50))
        pygame.draw.circle(pantalla, NEGRO, (huevo_x - 7, huevo_y - 15), 3)
        pygame.draw.circle(pantalla, NEGRO, (huevo_x + 7, huevo_y - 15), 3)
        pygame.draw.arc(pantalla, NEGRO, (huevo_x - 10, huevo_y - 10, 20, 15), math.pi,2 * math.pi,2)
