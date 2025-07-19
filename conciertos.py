from utils import cargar_json, guardar_json
import datetime

RUTA_CONCIERTOS = 'data/conciertos.json'

def listar_conciertos():
    conciertos = cargar_json(RUTA_CONCIERTOS)
    if not conciertos:
        print("No hay conciertos disponibles.")
        return
    for c in conciertos:
        print(f"\nID: {c['id']} - {c['artista']} en {c['ciudad']} ({c['fecha']})")
        for s in c['secciones']:
            print(f"  - Sección: {s['nombre']}, Precio: ${s['precio']}, Stock: {s['stock']}")

def buscar_concierto_por_id(id_concierto):
    conciertos = cargar_json(RUTA_CONCIERTOS)
    for c in conciertos:
        if c['id'] == id_concierto:
            return c
    return None

def registrar_concierto():
    conciertos = cargar_json(RUTA_CONCIERTOS)
    nuevo_id = max([c['id'] for c in conciertos]) + 1 if conciertos else 1

    while True:
        artista = input("Nombre del artista: ").strip()
        if artista:
            break
        print("El nombre del artista no puede estar vacío.")

    while True:
        fecha_str = input("Fecha del concierto (YYYY-MM-DD): ").strip()
        try:
            fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
            if fecha > datetime.date.today():
                break
            else:
                print("La fecha debe ser en el futuro.")
        except ValueError:
            print("Formato de fecha inválido. Use YYYY-MM-DD.")

    while True:
        ciudad = input("Ciudad del concierto: ").strip()
        if ciudad:
            break
        print("La ciudad no puede estar vacía.")

    secciones = []
    while True:
        agregar = input("¿Agregar una nueva sección? (s/n): ").lower()
        if agregar != 's':
            break
        
        nombre_seccion = input("Nombre de la sección: ").strip()
        while True:
            try:
                precio_seccion = int(input(f"Precio para {nombre_seccion}: "))
                if precio_seccion > 0:
                    break
                else:
                    print("El precio debe ser positivo.")
            except ValueError:
                print("Precio inválido.")

        while True:
            try:
                stock_seccion = int(input(f"Stock para {nombre_seccion}: "))
                if stock_seccion > 0:
                    break
                else:
                    print("El stock debe ser positivo.")
            except ValueError:
                print("Stock inválido.")

        secciones.append({"nombre": nombre_seccion, "precio": precio_seccion, "stock": stock_seccion})

    if not secciones:
        print("Debe agregar al menos una sección.")
        return

    nuevo_concierto = {
        "id": nuevo_id,
        "artista": artista,
        "fecha": fecha_str,
        "ciudad": ciudad,
        "secciones": secciones
    }

    conciertos.append(nuevo_concierto)
    guardar_json(RUTA_CONCIERTOS, conciertos)
    print(f"¡Concierto de {artista} registrado con éxito!")
