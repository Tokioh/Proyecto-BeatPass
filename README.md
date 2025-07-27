
# 🎵 BeatPass - Sistema de Gestión de Boletos para Conciertos

![Python](https://img.shields.io/badge/python-v3.13+-blue.svg)
![Tests](https://img.shields.io/badge/tests-52%2F52%20✅-brightgreen.svg)
![Coverage](https://img.shields.io/badge/coverage-90%25-green.svg)
![Status](https://img.shields.io/badge/status-production%20ready-success.svg)

**BeatPass** es un sistema integral de gestión de boletos para conciertos desarrollado en Python usando programación estructurada. El proyecto incluye validaciones robustas, testing automatizado completo y persistencia de datos confiable.

## 🎯 Características Principales

- ✅ **Gestión Completa de Usuarios** - Registro y validación con correos únicos
- ✅ **Administración de Conciertos** - Eventos con múltiples secciones y precios
- ✅ **Sistema de Venta de Boletos** - Control de stock en tiempo real
- ✅ **Persistencia de Datos** - Almacenamiento en JSON y CSV
- ✅ **Testing Automatizado** - 52 tests con 100% de éxito
- ✅ **Validaciones Robustas** - Control exhaustivo de datos de entrada
- ✅ **Arquitectura Modular** - Código organizado y escalable

## 📁 Estructura del Proyecto

```
BeatPass/
├── 📄 main.py                    # Punto de entrada principal
├── 👥 usuarios.py               # Gestión y validación de usuarios
├── 🎤 conciertos.py             # Administración de eventos
├── 🎫 boletos.py                # Sistema de venta de boletos
├── 🔧 utils.py                  # Funciones utilitarias
├── 🖼️ gui.py                    # Interfaz gráfica (opcional)
├── 📄 __init__.py               # Inicialización del paquete
├── 💾 data/                     # Almacenamiento de datos
│   ├── 📊 usuarios.csv          # Base de datos de usuarios
│   ├── 🎵 conciertos.json       # Catálogo de conciertos
│   └── 🎟️ boletos.json          # Registro de boletos vendidos
├── 🧪 tests/                    # Sistema de testing
│   ├── ⚙️ conftest.py           # Configuración de tests
│   ├── 👥 test_usuarios.py      # Tests de usuarios (17/17 ✅)
│   ├── 🎤 test_conciertos.py    # Tests de conciertos (19/19 ✅)
│   ├── 🎫 test_boletos.py       # Tests de boletos (9/9 ✅)
│   ├── 🔄 test_integration.py   # Tests de integración (6/6 ✅)
│   └── 📄 test_simple.py        # Test general (1/1 ✅)
├── 📚 docs/                     # Documentación
│   ├── 📋 INFORME_TECNICO.md    # Documentación técnica completa
│   ├── 📊 INFORME_EJECUTIVO.md  # Resumen ejecutivo
│   ├── 🎯 PRESENTACION.md       # Diapositivas para presentación
│   ├── ✅ CHECKLIST_PRESENTACION.md  # Lista de verificación
│   └── 🧪 TESTING.md            # Guía de testing
├── 🚀 demo_presentacion.py      # Script de demostración
├── ⚙️ pytest.ini               # Configuración de pytest
└── 🏃 run_tests.py              # Script para ejecutar tests
```

## 🔧 Módulos Principales

### 🎮 `main.py` - Centro de Control
- **Función:** Menú principal interactivo de la aplicación
- **Características:** Navegación intuitiva entre funcionalidades
- **Estado:** ✅ Completamente funcional

### 👥 `usuarios.py` - Gestión de Usuarios
- **Funciones principales:**
  - `registrar_usuario()` - Registro con validación completa
  - `validar_usuario_registrado()` - Verificación de usuarios existentes
  - `cargar_usuarios_csv()` / `guardar_usuarios_csv()` - Persistencia
- **Validaciones:** Email único, formato válido, nombres con solo letras
- **Estado:** ✅ 17/17 tests pasando (100%)

### 🎤 `conciertos.py` - Administración de Eventos
- **Funciones principales:**
  - `registrar_concierto()` - Creación de eventos con múltiples secciones
  - `listar_conciertos()` - Catálogo de eventos disponibles
  - `buscar_concierto_por_id()` - Búsqueda específica
- **Validaciones:** Fechas futuras, precios positivos, stock no negativo
- **Estado:** ✅ 19/19 tests pasando (100%)

### 🎫 `boletos.py` - Sistema de Ventas
- **Funciones principales:**
  - `generar_boleto()` - Venta con control de stock
  - `mostrar_boletos_usuario()` - Historial de compras
  - `cargar_boletos_json()` / `guardar_boletos_json()` - Persistencia
- **Características:** Control de stock en tiempo real, validación de usuarios
- **Estado:** ✅ 9/9 tests pasando (100%)

### 🔧 `utils.py` - Funciones Utilitarias
- **Funciones principales:**
  - `cargar_json()` / `guardar_json()` - Manejo de archivos JSON
  - `cargar_csv()` / `guardar_csv()` - Manejo de archivos CSV
- **Características:** Manejo robusto de errores, recuperación ante archivos corruptos
- **Estado:** ✅ Completamente funcional

## ⚡ Funcionalidades

### 👤 Para Usuarios:

1. **🔐 Registrarse**
   - Crear cuenta con nombre y correo electrónico
   - Validación automática de formato de email
   - Prevención de correos duplicados

2. **🎵 Ver Conciertos**
   - Lista completa de eventos disponibles
   - Información detallada: artista, fecha, ciudad, secciones
   - Precios y stock en tiempo real

3. **🛒 Comprar Entrada**
   - Selección de concierto y sección específica
   - Verificación automática de stock disponible
   - Confirmación instantánea de compra

4. **📋 Ver Mis Boletos**
   - Historial completo de compras
   - Detalles de cada boleto: concierto, sección, precio
   - Consulta por correo electrónico

### 👨‍💼 Para Administradores:

1. **➕ Registrar Concierto**
   - Añadir nuevos eventos al sistema
   - Configurar múltiples secciones con precios diferenciados
   - Establecer stock individual por sección
   - Validación de fechas futuras

## 🚀 Instalación y Uso

### 📋 Requisitos Previos

- **Python 3.13+** (recomendado)
- **pytest** para ejecutar tests
- **pytest-cov** para reportes de cobertura (opcional)

### 🔧 Instalación

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/Tokioh/Proyecto-BeatPass.git
   cd Proyecto-BeatPass
   ```

2. **Instalar Dependencias** (opcional, solo para testing):
   ```bash
   pip install pytest pytest-cov pytest-mock
   ```

### ▶️ Ejecución

1. **Ejecutar la Aplicación Principal**:
   ```bash
   python main.py
   ```

2. **Ejecutar Demostración Interactiva**:
   ```bash
   python demo_presentacion.py
   ```

3. **Ejecutar Tests**:
   ```bash
   # Opción 1: Comando básico
   pytest
   
   # Opción 2: Con script personalizado
   python run_tests.py all
   
   # Opción 3: Con cobertura
   python run_tests.py coverage
   ```

## 💾 Archivos de Datos

El sistema utiliza archivos locales para persistencia:

- **📊 `data/usuarios.csv`** - Base de datos de usuarios registrados
  ```csv
  nombre,correo
  Juan Pérez,juan@email.com
  María García,maria@email.com
  ```

- **🎵 `data/conciertos.json`** - Catálogo de conciertos disponibles
  ```json
  [
    {
      "id": 1,
      "artista": "Coldplay",
      "fecha": "2025-12-25",
      "ciudad": "Quito",
      "secciones": [
        {"nombre": "VIP", "precio": 300, "stock": 10},
        {"nombre": "General", "precio": 100, "stock": 200}
      ]
    }
  ]
  ```

- **🎟️ `data/boletos.json`** - Registro de boletos vendidos
  ```json
  [
    {
      "usuario": "juan@email.com",
      "concierto_id": 1,
      "seccion": "VIP",
      "precio": 300
    }
  ]
  ```

## 🧪 Sistema de Testing

BeatPass incluye un sistema de testing automatizado completo con **52 tests que pasan al 100%**:

### 📊 Estadísticas de Tests

| Módulo | Tests | Éxito | Cobertura |
|--------|-------|-------|-----------|
| 👥 Usuarios | 17/17 | ✅ 100% | Validaciones completas |
| 🎤 Conciertos | 19/19 | ✅ 100% | Casos de uso completos |
| 🎫 Boletos | 9/9 | ✅ 100% | Flujos de compra |
| 🔄 Integración | 6/6 | ✅ 100% | Flujos end-to-end |
| 📄 General | 1/1 | ✅ 100% | Tests básicos |
| **🎯 TOTAL** | **52/52** | **✅ 100%** | **🎯 Perfecto** |

### 🏗️ Arquitectura de Testing

- **🔧 Fixtures Automatizadas**: Aislamiento completo entre tests
- **📁 Directorios Temporales**: Datos de test no afectan producción
- **🎭 Mocking Avanzado**: Simulación de archivos y dependencias
- **🔄 Tests de Integración**: Validación de flujos completos

### ▶️ Comandos de Testing

```bash
# Ejecutar todos los tests
pytest

# Tests con salida detallada
pytest -v

# Tests con cobertura
python run_tests.py coverage

# Tests rápidos
python run_tests.py fast

# Test específico
pytest tests/test_usuarios.py::TestRegistrarUsuario::test_registrar_usuario_exitoso
```

### 📋 Tipos de Tests Implementados

1. **🧪 Tests Unitarios**
   - Validación de funciones individuales
   - Casos de éxito y error
   - Validaciones de entrada

2. **🔄 Tests de Integración**
   - Flujos completos del sistema
   - Interacción entre módulos
   - Persistencia de datos

3. **✅ Tests de Validación**
   - Formatos de correo electrónico
   - Fechas y rangos válidos
   - Control de stock

4. **🚫 Tests de Casos de Error**
   - Datos inválidos
   - Archivos corruptos
   - Usuarios no registrados

## 🛡️ Validaciones Implementadas

### 👤 Validaciones de Usuario
- ✅ **Nombres**: Solo letras y espacios permitidos
- ✅ **Correos**: Formato RFC 5322 validado con regex
- ✅ **Unicidad**: Prevención de correos duplicados
- ✅ **Campos requeridos**: No se permiten campos vacíos

### 🎤 Validaciones de Concierto
- ✅ **Fechas**: Solo fechas futuras permitidas
- ✅ **Precios**: Valores numéricos positivos
- ✅ **Stock**: Números enteros no negativos
- ✅ **Secciones**: Al menos una sección requerida

### 🎫 Validaciones de Boleto
- ✅ **Usuario registrado**: Verificación previa a compra
- ✅ **Concierto existente**: Validación de ID de concierto
- ✅ **Stock disponible**: Control en tiempo real
- ✅ **Sección válida**: Verificación de sección existente

## 🏗️ Arquitectura y Patrones

### 📐 Principios de Diseño
- **🔧 Programación Estructurada**: Funciones bien definidas y modulares
- **📦 Separación de Responsabilidades**: Cada módulo tiene un propósito específico
- **🔄 DRY (Don't Repeat Yourself)**: Reutilización de código común
- **✅ Validación Temprana**: Errores detectados en el punto de entrada

### 🎯 Patrones Implementados
- **📁 Repository Pattern**: Abstracción de persistencia de datos
- **🔧 Factory Pattern**: Creación consistente de objetos
- **✅ Validation Pattern**: Validación centralizada y reutilizable
- **🧪 Test Fixtures**: Configuración automática de entorno de pruebas

## 📈 Métricas del Proyecto

### 📊 Estadísticas de Código
- **📝 Líneas de código principal**: ~500 líneas
- **🧪 Líneas de tests**: ~400 líneas (optimizadas)
- **📁 Módulos principales**: 4 módulos core
- **🔧 Funciones públicas**: 15+ funciones principales
- **✅ Cobertura de tests**: 90%

### 🎯 Indicadores de Calidad
- **🧪 Tests exitosos**: 52/52 (100%)
- **🚫 Bugs conocidos**: 0
- **📚 Documentación**: Completa
- **🔄 Compatibilidad**: Python 3.13+

## 📚 Documentación Adicional

### 📋 Documentos Técnicos
- **📄 [INFORME_TECNICO.md](docs/INFORME_TECNICO.md)** - Documentación técnica completa
- **📊 [INFORME_EJECUTIVO.md](docs/INFORME_EJECUTIVO.md)** - Resumen ejecutivo
- **🎯 [PRESENTACION.md](docs/PRESENTACION.md)** - Diapositivas para presentación
- **🧪 [TESTING.md](docs/TESTING.md)** - Guía completa de testing

### 🚀 Scripts Útiles
- **🎬 [demo_presentacion.py](demo_presentacion.py)** - Demostración interactiva
- **🏃 [run_tests.py](run_tests.py)** - Ejecutor de tests personalizado

## 🤝 Contribución

### 💻 Para Desarrolladores
1. Fork del repositorio
2. Crear branch para feature: `git checkout -b feature/nueva-funcionalidad`
3. Commit cambios: `git commit -m 'Agregar nueva funcionalidad'`
4. Push al branch: `git push origin feature/nueva-funcionalidad`
5. Crear Pull Request

### ✅ Estándares de Código
- Seguir PEP 8 para estilo de Python
- Agregar tests para nueva funcionalidad
- Mantener cobertura de tests >90%
- Documentar funciones públicas
- Validar entrada de datos

## 🐛 Solución de Problemas

### ❓ Problemas Comunes

**Q: Error "ModuleNotFoundError"**
A: Asegúrate de ejecutar desde el directorio raíz del proyecto

**Q: Tests fallan intermitentemente**
A: Los tests usan fixtures temporales, ejecuta `pytest --cache-clear`

**Q: Archivos de datos corruptos**
A: Elimina archivos en `data/` - se recrearán automáticamente

**Q: Problemas de permisos en Windows**
A: Ejecuta terminal como administrador si es necesario

## 🙏 Agradecimientos

- **🏫 Universidad ULEAM** - Por el apoyo educativo
- **👨‍🏫 Profesores del curso** - Por la guía en programación estructurada
- **🐍 Comunidad Python** - Por la documentación y herramientas
- **🧪 Equipo pytest** - Por el framework de testing

## 📄 Licencia

Este proyecto es desarrollado con fines educativos como parte del curso de Programación Estructurada 2025-1 en ULEAM.

---

**Desarrollado con ❤️ usando Python 3.13 | Testing con pytest | Documentado con Markdown**

*🎵 BeatPass - Donde la música se encuentra con la tecnología 🎵*
