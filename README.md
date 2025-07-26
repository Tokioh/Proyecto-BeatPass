
El proyecto "BeatPass" es un sistema de gestión de boletos para conciertos, implementado en Python. Permite a los usuarios registrarse, ver conciertos disponibles, comprar boletos y ver sus boletos. También incluye funcionalidades para que los administradores registren nuevos conciertos.

## Estructura del Proyecto

```
beatpass/
├───__init__.py
├───.gitattributes
├───boletos.py
├───conciertos.py
├───gui.py
├───main.py
├───usuarios.py
├───utils.py
├───__pycache__/
├───.git/...
├───data/
│   ├───boletos.json
│   ├───conciertos.json
│   └───usuarios.csv
└───tests/
    ├───test_boletos.py
    ├───test_usuarios.py
    └───__pycache__/
```

## Módulos Principales

-   `main.py`: Contiene el menú principal de la aplicación y orquesta las interacciones entre los diferentes módulos.
-   `usuarios.py`: Gestiona el registro y validación de usuarios. Los datos de los usuarios se almacenan en `data/usuarios.csv`.
-   `conciertos.py`: Maneja la creación, listado y búsqueda de conciertos. Los datos de los conciertos se almacenan en `data/conciertos.json`.
-   `boletos.py`: Permite la generación y visualización de boletos. Los boletos se almacenan en `data/boletos.json`.
-   `utils.py`: Proporciona funciones de utilidad para cargar y guardar datos en formatos JSON y CSV.
-   `gui.py`: (No implementado en el código proporcionado, pero presente en la estructura) Posiblemente destinado a una interfaz gráfica de usuario.

## Funcionalidades

### Para Usuarios:

1.  **Registrarse**: Los usuarios pueden crear una cuenta proporcionando un nombre y un correo electrónico.
2.  **Ver Conciertos**: Muestra una lista de todos los conciertos disponibles, incluyendo artista, fecha, ciudad y secciones con sus precios y stock.
3.  **Comprar Entrada**: Permite a los usuarios comprar un boleto para un concierto y sección específicos, siempre que haya stock disponible.
4.  **Ver Mis Boletos**: Muestra todos los boletos que un usuario ha comprado.

### Para Administradores (o Usuarios con Permisos):

1.  **Registrar Concierto**: Permite añadir nuevos conciertos al sistema, especificando artista, fecha, ciudad y las diferentes secciones con sus precios y stock.

## Cómo Ejecutar el Proyecto

1.  **Clonar el Repositorio**:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd beatpass
    ```
2.  **Ejecutar la Aplicación**:
    ```bash
    python main.py
    ```

## Archivos de Datos

-   `data/usuarios.csv`: Almacena la información de los usuarios registrados (nombre, correo).
-   `data/conciertos.json`: Contiene los detalles de todos los conciertos disponibles.
-   `data/boletos.json`: Guarda los boletos comprados por los usuarios.

## Pruebas

El proyecto incluye un directorio `tests/` con pruebas unitarias para las funcionalidades de usuarios y boletos:

-   `test_boletos.py`: Pruebas para la lógica de compra y visualización de boletos.
-   `test_usuarios.py`: Pruebas para el registro y validación de usuarios.

Para ejecutar las pruebas, asegúrate de tener `pytest` instalado (`pip install pytest`) y luego ejecuta:

```bash
pytest
```
