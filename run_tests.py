#!/usr/bin/env python3
"""
Script para ejecutar tests de BeatPass con diferentes opciones.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Ejecuta un comando y muestra el resultado."""
    print(f"\n{'='*60}")
    print(f"🧪 {description}")
    print('='*60)
    
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=False, text=True)
        print(f"✅ {description} completado exitosamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}")
        print(f"Código de salida: {e.returncode}")
        return False

def main():
    """Función principal del script."""
    print("🚀 BeatPass - Sistema de Testing")
    print("================================")
    
    # Verificar que estamos en el directorio correcto
    if not os.path.exists("pytest.ini"):
        print("❌ Error: No se encontró pytest.ini")
        print("Asegúrate de ejecutar este script desde la raíz del proyecto")
        sys.exit(1)
    
    if len(sys.argv) > 1:
        option = sys.argv[1].lower()
    else:
        print("\nOpciones disponibles:")
        print("1. all       - Ejecutar todos los tests")
        print("2. unit      - Solo tests unitarios")
        print("3. integration - Solo tests de integración")
        print("4. coverage  - Tests con reporte de cobertura")
        print("5. verbose   - Tests con salida detallada")
        print("6. fast      - Tests rápidos (sin cobertura)")
        
        option = input("\nSelecciona una opción (1-6): ").strip()
    
    commands = {
        "1": ("pytest", "Ejecutando todos los tests"),
        "all": ("pytest", "Ejecutando todos los tests"),
        
        "2": ("pytest tests/test_utils.py tests/test_usuarios.py tests/test_conciertos.py tests/test_boletos.py", 
              "Ejecutando tests unitarios"),
        "unit": ("pytest tests/test_utils.py tests/test_usuarios.py tests/test_conciertos.py tests/test_boletos.py", 
                 "Ejecutando tests unitarios"),
        
        "3": ("pytest tests/test_integration.py", "Ejecutando tests de integración"),
        "integration": ("pytest tests/test_integration.py", "Ejecutando tests de integración"),
        
        "4": ("pytest --cov=. --cov-report=html --cov-report=term-missing", 
              "Ejecutando tests con reporte de cobertura"),
        "coverage": ("pytest --cov=. --cov-report=html --cov-report=term-missing", 
                     "Ejecutando tests con reporte de cobertura"),
        
        "5": ("pytest -v -s", "Ejecutando tests con salida detallada"),
        "verbose": ("pytest -v -s", "Ejecutando tests con salida detallada"),
        
        "6": ("pytest --tb=short", "Ejecutando tests rápidos"),
        "fast": ("pytest --tb=short", "Ejecutando tests rápidos"),
    }
    
    if option in commands:
        command, description = commands[option]
        success = run_command(command, description)
        
        if option in ["4", "coverage"] and success:
            print(f"\n📊 Reporte de cobertura generado en: htmlcov/index.html")
            print("Para ver el reporte, abre el archivo en tu navegador")
        
        if success:
            print(f"\n🎉 ¡Todos los tests pasaron correctamente!")
        else:
            print(f"\n❌ Algunos tests fallaron. Revisa la salida anterior.")
            sys.exit(1)
    else:
        print(f"❌ Opción '{option}' no válida")
        sys.exit(1)

if __name__ == "__main__":
    main()
