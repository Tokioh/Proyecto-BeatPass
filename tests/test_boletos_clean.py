import pytest
from boletos import generar_boleto, mostrar_boletos_usuario, cargar_boletos_json, guardar_boletos_json
from usuarios import registrar_usuario
from conciertos import registrar_concierto

class TestGenerarBoleto:
    """Tests para la función generar_boleto."""
    
    def setup_method(self):
        """Configuración inicial para cada test."""
        # Datos de ejemplo que se usarán en múltiples tests
        self.secciones_ejemplo = [
            {"nombre": "VIP", "precio": "200", "stock": "10"},
            {"nombre": "General", "precio": "100", "stock": "50"}
        ]
    
    def test_generar_boleto_exitoso(self, temp_data_dir):
        """Test generación exitosa de boleto."""
        # Registrar usuario
        registrar_usuario("Juan Pérez", "juan@email.com")
        
        # Registrar concierto
        registrar_concierto("Coldplay", "2025-12-25", "Quito", self.secciones_ejemplo)
        
        # Generar boleto
        resultado = generar_boleto("juan@email.com", 1, "VIP")
        assert resultado is None
    
    def test_generar_boleto_usuario_no_registrado(self, temp_data_dir):
        """Test generar boleto con usuario no registrado."""
        # Registrar concierto
        registrar_concierto("Coldplay", "2025-12-25", "Quito", self.secciones_ejemplo)
        
        # Intentar generar boleto sin registrar usuario
        resultado = generar_boleto("noregistrado@email.com", 1, "VIP")
        assert resultado == "El correo electrónico no está registrado. Por favor, regístrese primero."
    
    def test_generar_boleto_correo_vacio(self, temp_data_dir):
        """Test generar boleto con correo vacío."""
        resultado = generar_boleto("", 1, "VIP")
        assert resultado == "El correo electrónico no está registrado. Por favor, regístrese primero."
    
    def test_generar_boleto_concierto_inexistente(self, temp_data_dir):
        """Test generar boleto para concierto que no existe."""
        # Registrar usuario
        registrar_usuario("Juan Pérez", "juan@email.com")
        
        # Intentar generar boleto para concierto inexistente
        resultado = generar_boleto("juan@email.com", 999, "VIP")
        assert resultado == "Concierto no encontrado."
    
    def test_generar_boleto_seccion_inexistente(self, temp_data_dir):
        """Test generar boleto para sección que no existe."""
        # Registrar usuario
        registrar_usuario("Juan Pérez", "juan@email.com")
        
        # Registrar concierto
        registrar_concierto("Coldplay", "2025-12-25", "Quito", self.secciones_ejemplo)
        
        # Intentar generar boleto para sección inexistente
        resultado = generar_boleto("juan@email.com", 1, "Platinum")
        assert resultado == "Sección no encontrada."
    
    def test_generar_boleto_reduce_stock(self, temp_data_dir):
        """Test que la generación de boleto reduce el stock."""
        # Registrar usuario
        registrar_usuario("Juan Pérez", "juan@email.com")
        
        # Registrar concierto con stock limitado
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "2"}]
        registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        
        # Generar primer boleto
        resultado = generar_boleto("juan@email.com", 1, "VIP")
        assert resultado is None


class TestMostrarBoletosUsuario:
    """Tests para la función mostrar_boletos_usuario."""
    
    def test_mostrar_boletos_usuario_no_registrado(self, temp_data_dir):
        """Test mostrar boletos de usuario no registrado."""
        boletos = mostrar_boletos_usuario("noregistrado@email.com")
        assert boletos == []
    
    def test_mostrar_boletos_usuario_sin_boletos(self, temp_data_dir):
        """Test mostrar boletos de usuario sin boletos."""
        # Registrar usuario
        registrar_usuario("Juan Pérez", "juan@email.com")
        
        # Consultar boletos
        boletos = mostrar_boletos_usuario("juan@email.com")
        assert boletos == []
    
    def test_mostrar_boletos_usuario_correo_vacio(self, temp_data_dir):
        """Test mostrar boletos con correo vacío."""
        boletos = mostrar_boletos_usuario("")
        assert boletos == []
