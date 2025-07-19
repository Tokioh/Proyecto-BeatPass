from utils import cargar_json, guardar_json
from conciertos import listar_conciertos , buscar_concierto_por_id, guardar_json as guardar_conciertos_json, RUTA_CONCIERTOS
from usuarios import cargar_usuarios_json

RUTA_BOLETOS = 'data/boletos.json'

def cargar_boletos_json(ruta=RUTA_BOLETOS):
    return cargar_json(ruta)

def guardar_boletos_json(boletos, ruta=RUTA_BOLETOS):
    guardar_json(ruta, boletos)

def generar_boleto():
    correo = input("Ingrese su correo electrónico: ").strip()
    if not correo:
        print("El correo no puede estar vacío.")
        return

    usuarios = cargar_usuarios_json()
    if not any(u['correo'] == correo for u in usuarios):
        print("El correo electrónico no está registrado. Por favor, regístrese primero.")
        return

    listar_conciertos()
    if not cargar_json(RUTA_CONCIERTOS):
        print("No hay conciertos disponibles.")
        return

    try:
        id_concierto = int(input("Ingrese el ID del concierto: "))
    except ValueError:
        print("ID de concierto inválido. Debe ser un número.")
        return

    concierto = buscar_concierto_por_id(id_concierto)
    if not concierto:
        print("Concierto no encontrado.")
        return

    nombre_seccion = input("Ingrese el nombre de la sección: ").strip()
    seccion_encontrada = None
    for s in concierto['secciones']:
        if s['nombre'].lower() == nombre_seccion.lower():
            seccion_encontrada = s
            break

    if not seccion_encontrada:
        print("Sección no encontrada.")
        return

    if seccion_encontrada['stock'] <= 0:
        print(f"No hay más boletos para la sección {seccion_encontrada['nombre']}.")
        return

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
    print("¡Boleto comprado con éxito!")

def mostrar_boletos_usuario():
    while True:
        correo = input("Ingrese su correo para ver sus boletos: ").strip()
        if "@" in correo and "." in correo:
            break
        print("Correo electrónico inválido.")

    usuarios = cargar_usuarios_json()
    if not any(u['correo'] == correo for u in usuarios):
        print("El correo electrónico no está registrado.")
        return

    boletos = cargar_boletos_json()
    boletos_usuario = [b for b in boletos if b['usuario'] == correo]
    if not boletos_usuario:
        print("No se encontraron boletos para este usuario.")
        return
    for b in boletos_usuario:
        print(f"Concierto ID: {b['concierto_id']}, Sección: {b['seccion']}, Precio: ${b['precio']}")
