import pygame
import math
from config.configuracion import BLANCO, NEGRO, AZUL_CLARO


def dibujar_huevo(pantalla, huevo):
    color_huevo = BLANCO
    if huevo.invulnerable:
        if pygame.time.get_ticks() % 200 < 100:  # Parpadeo cuando es invulnerable
            color_huevo = AZUL_CLARO

    pygame.draw.ellipse(pantalla, color_huevo, huevo.rect)  # Dibujar el cuerpo del huevo
    pygame.draw.ellipse(pantalla, NEGRO, huevo.rect, 2)  # Borde negro

    centro_x = huevo.rect.centerx  # Dibujar la cara sonriente
    centro_y = huevo.rect.centery - 5

    pygame.draw.circle(pantalla, NEGRO, (centro_x - 6, centro_y - 5), 3)  # Ojos
    pygame.draw.circle(pantalla, NEGRO, (centro_x + 6, centro_y - 5), 3)

    pygame.draw.arc(pantalla, NEGRO, (centro_x - 8, centro_y + 2, 16, 10), math.pi, 2 * math.pi, 2)  # Boca hacia arriba

    if huevo.grietas > 0:  # Dibujar grietas
        for i in range(huevo.grietas):
            x_grieta = huevo.rect.x + 8 + i * 6
            y_grieta = huevo.rect.y + 10 + i * 8
            pygame.draw.line(pantalla, NEGRO, (x_grieta, y_grieta), (x_grieta + 8, y_grieta + 12), 2)