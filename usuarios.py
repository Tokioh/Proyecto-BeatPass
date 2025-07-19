from utils import cargar_json, guardar_json

RUTA_USUARIOS = 'data/usuarios.json'

def cargar_usuarios_json(ruta=RUTA_USUARIOS):
    return cargar_json(ruta)

def guardar_usuarios_json(usuarios, ruta=RUTA_USUARIOS):
    guardar_json(ruta, usuarios)

def registrar_usuario():
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    while True:
        correo = input("Correo electrónico: ").strip()
        if "@" in correo and "." in correo:
            break
        print("Correo electrónico inválido.")

    usuarios = cargar_usuarios_json()
    if any(u['correo'] == correo for u in usuarios):
        print("El correo ya está registrado.")
        return

    usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(usuario)
    guardar_usuarios_json(usuarios)
    print(f"¡Usuario {nombre} registrado con éxito!")
