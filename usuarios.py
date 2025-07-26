import re
from utils import cargar_csv, guardar_csv

RUTA_USUARIOS = 'data/usuarios.csv'

def cargar_usuarios_csv():
    return cargar_csv(RUTA_USUARIOS)

def guardar_usuarios_csv(usuarios):
    guardar_csv(RUTA_USUARIOS, usuarios, ['nombre', 'correo'])

def registrar_usuario(nombre, correo):
    if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
        return "El nombre no puede estar vacío y solo puede contener letras y espacios."
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo):
        return "Correo electrónico inválido."

    usuarios = cargar_usuarios_csv()
    if any(u['correo'] == correo for u in usuarios):
        return "El correo ya está registrado."

    usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(usuario)
    guardar_usuarios_csv(usuarios)
    return None

def validar_usuario_registrado(correo):
    if not correo:
        return "El correo no puede estar vacío."
    
    usuarios = cargar_usuarios_csv()
    if not any(u['correo'] == correo for u in usuarios):
        return "El correo electrónico no está registrado. Por favor, regístrese primero."
    
    return None  # Todo correcto
