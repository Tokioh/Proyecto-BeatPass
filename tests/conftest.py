import pytest
import os
import json
import csv
import tempfile
import shutil
from unittest.mock import patch

@pytest.fixture
def temp_data_dir():
    """Crea un directorio temporal para datos de test."""
    temp_dir = tempfile.mkdtemp()
    
    # Configurar rutas temporales
    paths = {
        'usuarios': os.path.join(temp_dir, 'usuarios.csv'),
        'conciertos': os.path.join(temp_dir, 'conciertos.json'),
        'boletos': os.path.join(temp_dir, 'boletos.json')
    }
    
    # Crear archivos vacíos
    with open(paths['usuarios'], 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['nombre', 'correo'])
        writer.writeheader()
    
    with open(paths['conciertos'], 'w') as f:
        json.dump([], f)
    
    with open(paths['boletos'], 'w') as f:
        json.dump([], f)
    
    # Hacer el mock de las rutas
    with patch('usuarios.RUTA_USUARIOS', paths['usuarios']), \
         patch('conciertos.RUTA_CONCIERTOS', paths['conciertos']), \
         patch('boletos.RUTA_BOLETOS', paths['boletos']), \
         patch('boletos.RUTA_CONCIERTOS', paths['conciertos']), \
         patch('boletos.guardar_boletos_json') as mock_guardar, \
         patch('boletos.cargar_boletos_json') as mock_cargar:
        
        # Configurar mocks para usar archivos temporales
        def guardar_mock(boletos, ruta=None):
            if ruta is None:
                ruta = paths['boletos']
            with open(ruta, 'w') as f:
                import json
                json.dump(boletos, f, indent=4)
        
        def cargar_mock(ruta=None):
            if ruta is None:
                ruta = paths['boletos']
            try:
                with open(ruta, 'r') as f:
                    import json
                    return json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                return []
        
        mock_guardar.side_effect = guardar_mock
        mock_cargar.side_effect = cargar_mock
        
        yield paths
    
    # Limpiar
    shutil.rmtree(temp_dir)

@pytest.fixture
def sample_usuarios():
    """Datos de usuarios de ejemplo para tests."""
    return [
        {"nombre": "Juan Pérez", "correo": "juan@email.com"},
        {"nombre": "María García", "correo": "maria@email.com"},
        {"nombre": "Carlos López", "correo": "carlos@email.com"}
    ]

@pytest.fixture
def sample_conciertos():
    """Datos de conciertos de ejemplo para tests."""
    return [
        {
            "id": 1,
            "artista": "Coldplay",
            "fecha": "2025-12-25",
            "ciudad": "Quito",
            "secciones": [
                {"nombre": "VIP", "precio": 200, "stock": 10},
                {"nombre": "General", "precio": 100, "stock": 50}
            ]
        },
        {
            "id": 2,
            "artista": "Imagine Dragons",
            "fecha": "2025-11-15",
            "ciudad": "Guayaquil",
            "secciones": [
                {"nombre": "Platino", "precio": 150, "stock": 20},
                {"nombre": "Popular", "precio": 75, "stock": 100}
            ]
        }
    ]

@pytest.fixture
def sample_boletos():
    """Datos de boletos de ejemplo para tests."""
    return [
        {
            "usuario": "juan@email.com",
            "concierto_id": 1,
            "seccion": "VIP",
            "precio": 200
        },
        {
            "usuario": "maria@email.com",
            "concierto_id": 1,
            "seccion": "General",
            "precio": 100
        }
    ]
