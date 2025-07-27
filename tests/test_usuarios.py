import pytest
from unittest.mock import patch, mock_open
from usuarios import registrar_usuario, validar_usuario_registrado, cargar_usuarios_csv, guardar_usuarios_csv

class TestRegistrarUsuario:
    """Tests para la función registrar_usuario."""
    
    def test_registrar_usuario_exitoso(self, temp_data_dir):
        """Test registro exitoso de usuario."""
        resultado = registrar_usuario("Pedro Ramírez", "pedro@email.com")
        assert resultado is None
        
        # Verificar que el usuario se guardó
        usuarios = cargar_usuarios_csv()
        assert len(usuarios) == 1
        assert usuarios[0]["nombre"] == "Pedro Ramírez"
        assert usuarios[0]["correo"] == "pedro@email.com"
    
    def test_registrar_usuario_nombre_vacio(self, temp_data_dir):
        """Test registro con nombre vacío."""
        resultado = registrar_usuario("", "test@email.com")
        assert resultado == "El nombre no puede estar vacío y solo puede contener letras y espacios."
    
    def test_registrar_usuario_nombre_con_numeros(self, temp_data_dir):
        """Test registro con nombre que contiene números."""
        resultado = registrar_usuario("Juan123", "test@email.com")
        assert resultado == "El nombre no puede estar vacío y solo puede contener letras y espacios."
    
    def test_registrar_usuario_nombre_con_caracteres_especiales(self, temp_data_dir):
        """Test registro con nombre que contiene caracteres especiales."""
        resultado = registrar_usuario("Juan@", "test@email.com")
        assert resultado == "El nombre no puede estar vacío y solo puede contener letras y espacios."
    
    def test_registrar_usuario_nombre_con_espacios_valido(self, temp_data_dir):
        """Test registro con nombre que contiene espacios (válido)."""
        resultado = registrar_usuario("Juan Carlos", "test@email.com")
        assert resultado is None
    
    def test_registrar_usuario_correo_invalido_sin_arroba(self, temp_data_dir):
        """Test registro con correo sin @."""
        resultado = registrar_usuario("Juan", "juanemail.com")
        assert resultado == "Correo electrónico inválido."
    
    def test_registrar_usuario_correo_invalido_sin_dominio(self, temp_data_dir):
        """Test registro con correo sin dominio."""
        resultado = registrar_usuario("Juan", "juan@")
        assert resultado == "Correo electrónico inválido."
    
    def test_registrar_usuario_correo_invalido_sin_extension(self, temp_data_dir):
        """Test registro con correo sin extensión."""
        resultado = registrar_usuario("Juan", "juan@email")
        assert resultado == "Correo electrónico inválido."
    
    def test_registrar_usuario_correo_duplicado(self, temp_data_dir):
        """Test registro con correo ya existente."""
        # Registrar primer usuario
        registrar_usuario("Juan", "juan@email.com")
        
        # Intentar registrar segundo usuario con mismo correo
        resultado = registrar_usuario("Pedro", "juan@email.com")
        assert resultado == "El correo ya está registrado."
    
    def test_registrar_usuario_correos_diferentes_caso(self, temp_data_dir):
        """Test que correos con diferente caso se consideran diferentes."""
        # Registrar primer usuario
        registrar_usuario("Juan", "juan@email.com")
        
        # Registrar segundo usuario con mismo correo en mayúsculas
        resultado = registrar_usuario("Pedro", "JUAN@EMAIL.COM")
        assert resultado is None  # Debería permitirlo (case sensitive)

class TestValidarUsuarioRegistrado:
    """Tests para la función validar_usuario_registrado."""
    
    def test_validar_usuario_registrado_correo_vacio(self, temp_data_dir):
        """Test validación con correo vacío."""
        resultado = validar_usuario_registrado("")
        assert resultado == "El correo no puede estar vacío."
    
    def test_validar_usuario_registrado_correo_none(self, temp_data_dir):
        """Test validación con correo None."""
        resultado = validar_usuario_registrado(None)
        assert resultado == "El correo no puede estar vacío."
    
    def test_validar_usuario_no_registrado(self, temp_data_dir):
        """Test validación con usuario no registrado."""
        resultado = validar_usuario_registrado("noexiste@email.com")
        assert resultado == "El correo electrónico no está registrado. Por favor, regístrese primero."
    
    def test_validar_usuario_registrado_exitoso(self, temp_data_dir):
        """Test validación exitosa de usuario registrado."""
        # Registrar usuario primero
        registrar_usuario("Juan", "juan@email.com")
        
        # Validar usuario
        resultado = validar_usuario_registrado("juan@email.com")
        assert resultado is None

class TestCargaryGuardarUsuarios:
    """Tests para las funciones de carga y guardado de usuarios."""
    
    def test_cargar_usuarios_csv_archivo_vacio(self, temp_data_dir):
        """Test cargar usuarios desde archivo CSV vacío."""
        usuarios = cargar_usuarios_csv()
        assert usuarios == []
    
    def test_guardar_usuarios_csv(self, temp_data_dir):
        """Test guardar usuarios en CSV."""
        usuarios = [
            {"nombre": "Juan", "correo": "juan@email.com"},
            {"nombre": "María", "correo": "maria@email.com"}
        ]
        
        guardar_usuarios_csv(usuarios)
        
        # Verificar que se guardaron correctamente
        usuarios_cargados = cargar_usuarios_csv()
        assert usuarios_cargados == usuarios
    
    def test_registrar_multiples_usuarios(self, temp_data_dir):
        """Test registrar múltiples usuarios."""
        # Registrar varios usuarios
        assert registrar_usuario("Juan", "juan@email.com") is None
        assert registrar_usuario("María", "maria@email.com") is None
        assert registrar_usuario("Pedro", "pedro@email.com") is None
        
        # Verificar que todos se guardaron
        usuarios = cargar_usuarios_csv()
        assert len(usuarios) == 3
        
        correos = [u["correo"] for u in usuarios]
        assert "juan@email.com" in correos
        assert "maria@email.com" in correos
        assert "pedro@email.com" in correos
