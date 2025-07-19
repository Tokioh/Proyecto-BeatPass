import pytest
from usuarios import guardar_usuarios_json, cargar_usuarios_json

RUTA_TEST_USUARIOS = 'data/test_usuarios.json'

@pytest.fixture
def limpiar_usuarios():
    guardar_usuarios_json([], RUTA_TEST_USUARIOS)
    yield
    guardar_usuarios_json([], RUTA_TEST_USUARIOS)

def test_guardar_y_cargar(limpiar_usuarios):
    datos = [{"nombre": "Ana", "correo": "ana@mail.com"}]
    guardar_usuarios_json(datos, RUTA_TEST_USUARIOS)
    assert cargar_usuarios_json(RUTA_TEST_USUARIOS) == datos
