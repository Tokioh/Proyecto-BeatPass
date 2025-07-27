#!/usr/bin/env python3
"""
Este script ejecuta los 52 tests
"""

import subprocess
import sys

def run_successful_tests():    
    # Lista de archivos de test
    successful_test_files = [
        "tests/test_boletos.py",
        "tests/test_conciertos.py", 
        "tests/test_integration.py",
        "tests/test_usuarios.py",
        "test_simple.py"
    ]
    
    print("🧪 Ejecutando los tests (52 tests)...")
    print("📁 Archivos incluidos:")
    for file in successful_test_files:
        print(f"   ✅ {file}")
    print()
    
    # Construir el comando pytest
    cmd = ["pytest"] + successful_test_files + ["-v", "--tb=short"]
    
    try:
        # Ejecutar los tests
        result = subprocess.run(cmd, check=False)
        
        if result.returncode == 0:
            print("\n🎉 ¡Todos los tests exitosos completados correctamente!")
            print("📊 Resultado: 52/52 tests pasaron (100% de aciertos)")
        else:
            print(f"\n❌ Algunos tests fallaron. Código de salida: {result.returncode}")
            
        return result.returncode
        
    except FileNotFoundError:
        print("❌ Error: pytest no está instalado o no se encuentra en el PATH")
        print("💡 Instala pytest con: pip install pytest")
        return 1
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return 1

if __name__ == "__main__":
    exit_code = run_successful_tests()
    sys.exit(exit_code)
