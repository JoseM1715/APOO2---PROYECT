from model.estados import EstadoJuego
from config.configuracion import MAX_GRIETAS, MAX_NIVEL, ALTO_PANTALLA

class GestorColisiones:
    @staticmethod
    def procesar_colisiones_obstaculos(huevo, obstaculos):
        for obstaculo in obstaculos:
            if huevo.rect.colliderect(obstaculo.rect):
                resultado = obstaculo.efecto(huevo)
                if resultado == "muerte":
                    return True
        return False
    
    @staticmethod
    def procesar_colisiones_powerups(huevo, powerups):
        for powerup in powerups[:]:
            if powerup.activo and huevo.rect.colliderect(powerup.rect):
                powerup.aplicar(huevo)
                powerups.remove(powerup)
    
    @staticmethod
    def verificar_meta(huevo, meta, nivel_actual):
        if huevo.rect.colliderect(meta):
            if nivel_actual < MAX_NIVEL:
                return True, EstadoJuego.JUGANDO, nivel_actual + 1
            else:
                return False, EstadoJuego.VICTORIA, nivel_actual
        return False, None, nivel_actual
    
    @staticmethod
    def verificar_muerte_huevo(huevo):
        if huevo.grietas >= MAX_GRIETAS:
            return True
        # Muerte por caída fuera de la pantalla
        if huevo.rect.x > ALTO_PANTALLA:
            return True
        return False 