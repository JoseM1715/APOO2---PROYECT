import json
import os
from config.configuracion import ARCHIVO_PUNTUACIONES

class GestorPuntuaciones:
    @staticmethod
    def guardar_puntuacion(nombre, tiempo, nivel):
        try:
            puntuaciones = GestorPuntuaciones.cargar_puntuaciones()
        except:
            puntuaciones = []
        
        puntuaciones.append({
            'nombre': nombre,
            'tiempo': tiempo,
            'nivel': nivel
        })
        
        puntuaciones.sort(key=lambda x: x['tiempo']) # Ordenar por tiempo (menor es mejor)
        
        os.makedirs(os.path.dirname(ARCHIVO_PUNTUACIONES), exist_ok=True) # Crear directorio si no existe
        
        with open(ARCHIVO_PUNTUACIONES, 'w') as archivo:
            json.dump(puntuaciones, archivo, indent=2)
    
    @staticmethod
    def cargar_puntuaciones():
        try:
            with open(ARCHIVO_PUNTUACIONES, 'r') as archivo:
                return json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    @staticmethod
    def obtener_mejores_puntuaciones(limite=5):
        puntuaciones = GestorPuntuaciones.cargar_puntuaciones()
        return puntuaciones[:limite]
    
    @staticmethod
    def es_record(tiempo):
        puntuaciones = GestorPuntuaciones.cargar_puntuaciones()
        if not puntuaciones:
            return True
        return tiempo < puntuaciones[0]['tiempo'] 