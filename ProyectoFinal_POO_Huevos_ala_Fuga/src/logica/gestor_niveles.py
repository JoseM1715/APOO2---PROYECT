import pygame
from model.objetos_juego import Plataforma, Obstaculo, PowerUp
from config.configuracion import ANCHO_PANTALLA, ALTO_PANTALLA

ANCHO_NIVEL_1 = ANCHO_PANTALLA * 3  
ANCHO_NIVEL_2 = ANCHO_PANTALLA * 4  
ANCHO_NIVEL_3 = ANCHO_PANTALLA * 5  

def cargar_nivel(numero_nivel):
    plataformas = []
    obstaculos = []
    powerups = []
    
    if numero_nivel == 1:
        ancho_nivel = ANCHO_NIVEL_1
        
        plataformas.append(Plataforma(0, ALTO_PANTALLA - 50, ancho_nivel, 50))
        
        plataformas.append(Plataforma(200, 450, 100, 20))
        plataformas.append(Plataforma(400, 350, 100, 20))
        plataformas.append(Plataforma(600, 250, 100, 20))
        plataformas.append(Plataforma(900, 400, 100, 20))
        plataformas.append(Plataforma(1100, 300, 100, 20))
        plataformas.append(Plataforma(1400, 350, 100, 20))
        plataformas.append(Plataforma(1700, 250, 100, 20))
        plataformas.append(Plataforma(2000, 300, 100, 20))
        
        obstaculos.append(Obstaculo(300, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(500, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(750, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(1000, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(1250, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(1500, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(1800, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(2100, ALTO_PANTALLA - 70, "aceite"))
        
        obstaculos.append(Obstaculo(230, 430, "aceite")) 
        obstaculos.append(Obstaculo(430, 330, "aceite")) 
        obstaculos.append(Obstaculo(930, 380, "aceite")) 
        obstaculos.append(Obstaculo(1430, 330, "aceite"))
        
        powerups.append(PowerUp(250, 420, "cascara"))
        powerups.append(PowerUp(450, 320, "turbo"))
        powerups.append(PowerUp(950, 370, "papel"))
        powerups.append(PowerUp(1350, 320, "cascara"))
        powerups.append(PowerUp(1650, 220, "turbo"))
        
        meta = pygame.Rect(ancho_nivel - 100, ALTO_PANTALLA - 150, 30, 50)
        
    elif numero_nivel == 2:
        ancho_nivel = ANCHO_NIVEL_2
        
        plataformas.append(Plataforma(0, ALTO_PANTALLA - 50, ancho_nivel, 50))
        
        plataformas.append(Plataforma(150, 450, 100, 20))
        plataformas.append(Plataforma(350, 400, 100, 20))
        plataformas.append(Plataforma(550, 350, 100, 20))
        plataformas.append(Plataforma(800, 300, 100, 20))
        plataformas.append(Plataforma(1050, 400, 100, 20))
        plataformas.append(Plataforma(1300, 350, 100, 20))
        plataformas.append(Plataforma(1550, 300, 100, 20))
        plataformas.append(Plataforma(1800, 250, 100, 20))
        plataformas.append(Plataforma(2050, 300, 100, 20))
        plataformas.append(Plataforma(2300, 350, 100, 20))
        plataformas.append(Plataforma(2550, 300, 100, 20))
        plataformas.append(Plataforma(2800, 250, 100, 20))
        
        obstaculos.append(Obstaculo(200, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(400, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(600, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(900, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(1200, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(1500, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(1800, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(2100, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(2400, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(2700, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(300, 380, "aceite"))
        obstaculos.append(Obstaculo(1100, 380, "aceite"))
        obstaculos.append(Obstaculo(2000, 280, "aceite"))
        
        powerups.append(PowerUp(200, 420, "papel"))
        powerups.append(PowerUp(500, 320, "cascara"))
        powerups.append(PowerUp(900, 270, "turbo"))
        powerups.append(PowerUp(1400, 320, "papel"))
        powerups.append(PowerUp(1900, 220, "cascara"))
        powerups.append(PowerUp(2400, 320, "turbo"))

        meta = pygame.Rect(ancho_nivel - 100, ALTO_PANTALLA - 150, 30, 50)
        
    elif numero_nivel == 3:
        ancho_nivel = ANCHO_NIVEL_3
        
        plataformas.append(Plataforma(0, ALTO_PANTALLA - 50, ancho_nivel, 50))
        
        plataformas.append(Plataforma(100, 450, 80, 20))
        plataformas.append(Plataforma(250, 400, 80, 20))
        plataformas.append(Plataforma(400, 350, 80, 20))
        plataformas.append(Plataforma(550, 300, 80, 20))
        plataformas.append(Plataforma(700, 250, 80, 20))
        plataformas.append(Plataforma(850, 300, 80, 20))
        plataformas.append(Plataforma(1000, 350, 80, 20))
        plataformas.append(Plataforma(1150, 400, 80, 20))
        plataformas.append(Plataforma(1300, 450, 80, 20))
        plataformas.append(Plataforma(1450, 400, 80, 20))
        plataformas.append(Plataforma(1600, 350, 80, 20))
        plataformas.append(Plataforma(1750, 300, 80, 20))
        plataformas.append(Plataforma(1900, 250, 80, 20))
        plataformas.append(Plataforma(2050, 300, 80, 20))
        plataformas.append(Plataforma(2200, 350, 80, 20))
        plataformas.append(Plataforma(2350, 400, 80, 20))
        plataformas.append(Plataforma(2500, 350, 80, 20))
        plataformas.append(Plataforma(2650, 300, 80, 20))
        plataformas.append(Plataforma(2800, 250, 80, 20))
        plataformas.append(Plataforma(2950, 300, 80, 20))
        plataformas.append(Plataforma(3100, 350, 80, 20))
        plataformas.append(Plataforma(3250, 300, 80, 20))
        plataformas.append(Plataforma(3400, 250, 80, 20))
        plataformas.append(Plataforma(3550, 200, 80, 20))
        plataformas.append(Plataforma(3700, 250, 80, 20))
        
        obstaculos.append(Obstaculo(150, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(300, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(450, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(600, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(900, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(1200, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(1500, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(1800, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(2100, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(2400, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(2700, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(3000, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(3300, ALTO_PANTALLA - 70, "sarten"))
        obstaculos.append(Obstaculo(3600, ALTO_PANTALLA - 70, "aceite"))
        obstaculos.append(Obstaculo(300, 380, "aceite"))
        obstaculos.append(Obstaculo(900, 280, "aceite"))
        obstaculos.append(Obstaculo(1500, 380, "aceite"))
        obstaculos.append(Obstaculo(2100, 280, "aceite"))
        obstaculos.append(Obstaculo(2700, 230, "aceite"))
        obstaculos.append(Obstaculo(3300, 280, "aceite"))
        
        powerups.append(PowerUp(150, 420, "papel"))
        powerups.append(PowerUp(400, 320, "turbo"))
        powerups.append(PowerUp(850, 270, "cascara"))
        powerups.append(PowerUp(1300, 420, "papel"))
        powerups.append(PowerUp(1750, 270, "turbo"))
        powerups.append(PowerUp(2200, 320, "cascara"))
        powerups.append(PowerUp(2650, 270, "papel"))
        powerups.append(PowerUp(3100, 320, "turbo"))
        powerups.append(PowerUp(3550, 170, "cascara"))
        
        meta = pygame.Rect(ancho_nivel - 100, ALTO_PANTALLA - 150, 30, 50)
    return plataformas, obstaculos, powerups, meta, ancho_nivel 