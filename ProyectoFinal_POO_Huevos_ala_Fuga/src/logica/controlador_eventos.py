import pygame
from model.estados import EstadoJuego


class ControladorEventos:

    @staticmethod
    def procesar_eventos(estado_actual, nivel_actual, huevo, mostrar_puntuaciones, cargar_puntuaciones_callback):
        ejecutando = True
        nuevo_estado = estado_actual
        nuevo_nivel = nivel_actual
        puntuaciones = []

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            elif estado_actual == EstadoJuego.MENU:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        nuevo_estado = EstadoJuego.JUGANDO
                    elif evento.key == pygame.K_p:
                        mostrar_puntuaciones = not mostrar_puntuaciones
                        if mostrar_puntuaciones:
                            puntuaciones = cargar_puntuaciones_callback()

            elif estado_actual == EstadoJuego.JUGANDO:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                        huevo.saltar()
                    elif evento.key == pygame.K_ESCAPE:
                        nuevo_estado = EstadoJuego.PAUSA

            elif estado_actual == EstadoJuego.PAUSA:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        nuevo_estado = EstadoJuego.JUGANDO
                    elif evento.key == pygame.K_q:
                        nuevo_estado = EstadoJuego.MENU

            elif estado_actual in [EstadoJuego.GAME_OVER, EstadoJuego.VICTORIA]:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        # Reiniciar el juego
                        nuevo_estado = EstadoJuego.MENU
                        nuevo_nivel = 1

        return ejecutando, nuevo_estado, nuevo_nivel, mostrar_puntuaciones, puntuaciones

    @staticmethod
    def procesar_movimiento(huevo):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            huevo.mover(-1)
        elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            huevo.mover(1)
        else:
            huevo.mover(0)