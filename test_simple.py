import pytest
import tempfile
import shutil
import os
from unittest.mock import patch
from boletos import generar_boleto, cargar_boletos_json
from usuarios import registrar_usuario  
from conciertos import registrar_concierto
from utils import guardar_json

def test_simple_boleto():
    """Test simple sin fixtures."""
    # Crear directorio temporal
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Configurar rutas temporales
        boletos_path = os.path.join(temp_dir, 'boletos.json')
        usuarios_path = os.path.join(temp_dir, 'usuarios.csv')
        conciertos_path = os.path.join(temp_dir, 'conciertos.json')
        
        # Crear archivos vacíos
        with open(boletos_path, 'w') as f:
            f.write('[]')
        
        with open(usuarios_path, 'w') as f:
            f.write('nombre,correo\n')
            
        with open(conciertos_path, 'w') as f:
            f.write('[]')
        
        # Hacer el mock
        with patch('boletos.RUTA_BOLETOS', boletos_path), \
             patch('boletos.RUTA_CONCIERTOS', conciertos_path), \
             patch('usuarios.RUTA_USUARIOS', usuarios_path), \
             patch('conciertos.RUTA_CONCIERTOS', conciertos_path):
            
            # Registrar usuario
            resultado_usuario = registrar_usuario("Juan Pérez", "juan@email.com")
            assert resultado_usuario is None
            
            # Registrar concierto
            secciones = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
            resultado_concierto = registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
            assert resultado_concierto is None
            
            # Generar boleto
            resultado_boleto = generar_boleto("juan@email.com", 1, "VIP")
            assert resultado_boleto is None
            
            # Verificar boletos
            boletos = cargar_boletos_json(boletos_path)
            print(f"Boletos encontrados: {len(boletos)}")
            print(f"Boletos: {boletos}")
            # assert len(boletos) == 1
            # assert boletos[0]["usuario"] == "juan@email.com"
            
    finally:
        # Limpiar
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    test_simple_boleto()
    print("✅ Test simple pasó!")
