import pytest
from boletos import guardar_boletos_json, cargar_boletos_json

RUTA_TEST_BOLETOS = 'data/test_boletos.json'

@pytest.fixture
def limpiar_boletos():
    guardar_boletos_json([], RUTA_TEST_BOLETOS)
    yield
    guardar_boletos_json([], RUTA_TEST_BOLETOS)

def test_guardar_y_cargar_boletos(limpiar_boletos):
    datos = [
        {
            "usuario": "test@test.com",
            "concierto_id": 1,
            "seccion": "Loba VIP",
            "precio": 120
        }
    ]
    guardar_boletos_json(datos, RUTA_TEST_BOLETOS)
    assert cargar_boletos_json(RUTA_TEST_BOLETOS) == datos