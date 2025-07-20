import re
from utils import cargar_json, guardar_json

RUTA_USUARIOS = 'data/usuarios.json'

def cargar_usuarios_json(ruta=RUTA_USUARIOS):
    return cargar_json(ruta)

def guardar_usuarios_json(usuarios, ruta=RUTA_USUARIOS):
    guardar_json(ruta, usuarios)

def registrar_usuario():
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre and all(c.isalpha() or c.isspace() for c in nombre):
            break
        print("El nombre no puede estar vacío y solo puede contener letras y espacios.")

    while True:
        correo = input("Correo electrónico: ").strip()
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo):
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
