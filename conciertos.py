from utils import cargar_json, guardar_json
import datetime
import re

RUTA_CONCIERTOS = 'data/conciertos.json'

def listar_conciertos():
    """
    Carga los conciertos desde el archivo JSON y los devuelve.
    También imprime la lista en la consola para uso en CLI.
    """
    conciertos = cargar_json(RUTA_CONCIERTOS)
    if not conciertos:
        print("No hay conciertos disponibles.")
        return []
    for concierto in conciertos:
        for seccion in concierto.get('secciones', []):
            if 'precio' in seccion: 
                try:
                    seccion['precio'] = int(seccion['precio'])
                except ValueError:
                    pass # Handle error or log if necessary
            if 'stock' in seccion:
                try:
                    seccion['stock'] = int(seccion['stock'])
                except ValueError:
                    pass # Handle error or log if necessary
    return conciertos


def registrar_concierto(artista, fecha_str, ciudad, secciones):
    conciertos = cargar_json(RUTA_CONCIERTOS)
    nuevo_id = max([c['id'] for c in conciertos]) + 1 if conciertos else 1

    if not artista:
        return "El nombre del artista no puede estar vacío."

    try:
        fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
        if fecha <= datetime.date.today():
            return "La fecha debe ser en el futuro."
    except ValueError:
        return "Formato de fecha inválido. Use YYYY-MM-DD."

    if not ciudad:
        return "La ciudad no puede estar vacía."
    if not re.match(r"^[a-zA-Z0-9\s]+$", ciudad):
        return "La ciudad solo puede contener letras, números y espacios."

    if not secciones:
        return "Debe agregar al menos una sección."

    for seccion in secciones:
        if not seccion['nombre']:
            return "El nombre de la sección no puede estar vacío."
        try:
            seccion['precio'] = int(seccion['precio'])
            if seccion['precio'] <= 0:
                return "El precio debe ser positivo."
        except ValueError:
            return "Precio inválido."
        try:
            seccion['stock'] = int(seccion['stock'])
            if seccion['stock'] <= 0 or seccion['stock'] == '':
                return "El stock no puede estar vacio y debe ser positivo."
        except ValueError:
            return "Stock inválido."

    nuevo_concierto = {
        "id": nuevo_id,
        "artista": artista,
        "fecha": fecha_str,
        "ciudad": ciudad,
        "secciones": secciones
    }

    conciertos.append(nuevo_concierto)
    guardar_json(RUTA_CONCIERTOS, conciertos)
    return None

def buscar_concierto_por_id(id_concierto):
    conciertos = cargar_json(RUTA_CONCIERTOS)
    for concierto in conciertos:
        if concierto['id'] == id_concierto:
            return concierto
    return None