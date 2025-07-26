import json
import csv

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

def cargar_csv(ruta):
    """Carga datos desde un archivo CSV."""
    try:
        with open(ruta, 'r', newline='') as archivo:
            return list(csv.DictReader(archivo))
    except FileNotFoundError:
        return []

def guardar_csv(ruta, datos, headers):
    """Guarda datos en un archivo CSV."""
    with open(ruta, 'w', newline='') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=headers)
        writer.writeheader()
        writer.writerows(datos)
