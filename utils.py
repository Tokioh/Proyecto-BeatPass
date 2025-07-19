import json

def cargar_json(ruta):
    """Carga datos desde un archivo JSON."""
    try:
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_json(ruta, datos):
    """Guarda datos en un archivo JSON."""
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
