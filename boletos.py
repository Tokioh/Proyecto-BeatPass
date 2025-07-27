from utils import cargar_json, guardar_json
from conciertos import buscar_concierto_por_id, guardar_json, RUTA_CONCIERTOS
from usuarios import validar_usuario_registrado

RUTA_BOLETOS = 'data/boletos.json'

def cargar_boletos_json(ruta=RUTA_BOLETOS):
    return cargar_json(ruta)

def guardar_boletos_json(boletos, ruta=RUTA_BOLETOS):
    guardar_json(ruta, boletos)

def generar_boleto(correo, id_concierto, nombre_seccion):
    
    #validar correo
    mensaje_error = validar_usuario_registrado(correo)
    if mensaje_error:
        return mensaje_error

    concierto = buscar_concierto_por_id(id_concierto)
    if not concierto:
        return "Concierto no encontrado."

    seccion_encontrada = None
    for s in concierto['secciones']:
        if s['nombre'].lower() == nombre_seccion.lower():
            seccion_encontrada = s
            break

    if not seccion_encontrada:
        return "Sección no encontrada."

    if seccion_encontrada['stock'] <= 0:
        return f"No hay más boletos para la sección {seccion_encontrada['nombre']}."

    seccion_encontrada['stock'] -= 1
    conciertos = cargar_json(RUTA_CONCIERTOS)
    for i, c in enumerate(conciertos):
        if c['id'] == id_concierto:
            conciertos[i] = concierto
            break
    guardar_json(RUTA_CONCIERTOS, conciertos)

    boleto = {
        "usuario": correo,
        "concierto_id": id_concierto,
        "seccion": seccion_encontrada['nombre'],
        "precio": seccion_encontrada['precio']
    }
    boletos = cargar_boletos_json()
    boletos.append(boleto)
    guardar_boletos_json(boletos)
    return None

def mostrar_boletos_usuario(correo):
    mensaje_error = validar_usuario_registrado(correo)
    if mensaje_error:
        return mensaje_error
    
    boletos = cargar_boletos_json()
    boletos_usuario = [b for b in boletos if b['usuario'] == correo]
    return boletos_usuario

