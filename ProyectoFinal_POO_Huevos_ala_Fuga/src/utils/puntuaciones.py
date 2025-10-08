import json
import os

RUTA_PUNTUACIONES = os.path.join('Puntuaciones', 'scores.json')

def guardar_puntuacion(nombre, tiempo, nivel):
    os.makedirs(os.path.dirname(RUTA_PUNTUACIONES), exist_ok=True)
    
    try:
        with open(RUTA_PUNTUACIONES, 'r') as archivo:
            puntuaciones = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        puntuaciones = []
    
    puntuaciones.append({
        'nombre': nombre,
        'tiempo': tiempo,
        'nivel': nivel
    })
    
    puntuaciones.sort(key=lambda x: x['tiempo'])
    
    with open(RUTA_PUNTUACIONES, 'w') as archivo:
        json.dump(puntuaciones, archivo)

def cargar_puntuaciones():
    try:
        with open(RUTA_PUNTUACIONES, 'r') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 