#!/usr/bin/env python3
"""
Script para limpiar los tests y actualizar para usar temp_data_dir.
"""

import os
import re

def update_test_file(filepath):
    """Actualiza un archivo de test para usar temp_data_dir."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reemplazar definiciones de función de test
    content = re.sub(r'def (test_[^(]+)\(self\):', r'def \1(self, temp_data_dir):', content)
    content = re.sub(r'def (test_[^(]+)\(self, sample_([a-z_]+)\):', r'def \1(self, temp_data_dir, sample_\2):', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Actualizado: {filepath}")

def main():
    """Función principal."""
    test_files = [
        'tests/test_usuarios.py',
        'tests/test_conciertos.py',
        'tests/test_boletos.py', 
        'tests/test_integration.py'
    ]
    
    for test_file in test_files:
        if os.path.exists(test_file):
            update_test_file(test_file)
        else:
            print(f"❌ No encontrado: {test_file}")

if __name__ == "__main__":
    main()
