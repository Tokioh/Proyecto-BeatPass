import pytest
from datetime import date, datetime
from conciertos import registrar_concierto, listar_conciertos, buscar_concierto_por_id

class TestRegistrarConcierto:
    """Tests para la función registrar_concierto."""
    
    def test_registrar_concierto_exitoso(self, temp_data_dir):
        """Test registro exitoso de concierto."""
        secciones = [
            {"nombre": "VIP", "precio": "200", "stock": "10"},
            {"nombre": "General", "precio": "100", "stock": "50"}
        ]
        
        resultado = registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        assert resultado is None
    
    def test_registrar_concierto_artista_vacio(self, temp_data_dir):
        """Test registro con artista vacío."""
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
        
        resultado = registrar_concierto("", "2025-12-25", "Quito", secciones)
        assert resultado == "El artista no puede estar vacío."
    
    def test_registrar_concierto_fecha_pasada(self, temp_data_dir):
        """Test registro con fecha en el pasado."""
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
        
        resultado = registrar_concierto("Coldplay", "2020-01-01", "Quito", secciones)
        assert resultado == "La fecha debe ser en el futuro."
    
    def test_registrar_concierto_fecha_hoy(self, temp_data_dir):
        """Test registro con fecha de hoy."""
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
        fecha_hoy = date.today().strftime("%Y-%m-%d")
        
        resultado = registrar_concierto("Coldplay", fecha_hoy, "Quito", secciones)
        assert resultado == "La fecha debe ser en el futuro."
    
    def test_registrar_concierto_formato_fecha_invalido(self, temp_data_dir):
        """Test registro con formato de fecha inválido."""
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
        
        resultado = registrar_concierto("Coldplay", "25-12-2025", "Quito", secciones)
        assert resultado == "Formato de fecha inválido. Use YYYY-MM-DD."
    
    def test_registrar_concierto_ciudad_vacia(self, temp_data_dir):
        """Test registro con ciudad vacía."""
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
        
        resultado = registrar_concierto("Coldplay", "2025-12-25", "", secciones)
        assert resultado == "La ciudad no puede estar vacía."
    
    def test_registrar_concierto_ciudad_caracteres_especiales(self, temp_data_dir):
        """Test registro con ciudad con caracteres especiales."""
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
        
        resultado = registrar_concierto("Coldplay", "2025-12-25", "Quito123", secciones)
        assert resultado == "La ciudad solo puede contener letras y espacios."
    
    def test_registrar_concierto_sin_secciones(self, temp_data_dir):
        """Test registro sin secciones."""
        resultado = registrar_concierto("Coldplay", "2025-12-25", "Quito", [])
        assert resultado == "Debe haber al menos una sección."
    
    def test_registrar_concierto_seccion_sin_nombre(self, temp_data_dir):
        """Test registro con sección sin nombre."""
        secciones = [{"nombre": "", "precio": "200", "stock": "10"}]
        
        resultado = registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        assert resultado == "El nombre de la sección no puede estar vacío."
    
    def test_registrar_concierto_precio_invalido(self, temp_data_dir):
        """Test registro con precio inválido."""
        secciones = [{"nombre": "VIP", "precio": "abc", "stock": "10"}]
        
        resultado = registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        assert resultado == "Precio inválido."
    
    def test_registrar_concierto_precio_negativo(self, temp_data_dir):
        """Test registro con precio negativo."""
        secciones = [{"nombre": "VIP", "precio": "-100", "stock": "10"}]
        
        resultado = registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        assert resultado == "El precio debe ser positivo."
    
    def test_registrar_concierto_precio_cero(self, temp_data_dir):
        """Test registro con precio cero."""
        secciones = [{"nombre": "VIP", "precio": "0", "stock": "10"}]
        
        resultado = registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        assert resultado == "El precio debe ser positivo."
    
    def test_registrar_concierto_stock_invalido(self, temp_data_dir):
        """Test registro con stock inválido."""
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "abc"}]
        
        resultado = registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        assert resultado == "Stock inválido."
    
    def test_registrar_concierto_stock_negativo(self, temp_data_dir):
        """Test registro con stock negativo."""
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "-5"}]
        
        resultado = registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        assert resultado == "El stock no puede ser negativo."
    
    def test_registrar_concierto_stock_cero(self, temp_data_dir):
        """Test registro con stock cero."""
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "0"}]
        
        resultado = registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        assert resultado is None  # Stock cero está permitido
    
    def test_registrar_concierto_id_secuencial(self, temp_data_dir):
        """Test que los IDs se asignan secuencialmente."""
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
        
        # Registrar primer concierto
        registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        
        # Registrar segundo concierto
        registrar_concierto("Imagine Dragons", "2025-11-15", "Guayaquil", secciones)
        
        conciertos = listar_conciertos()
        assert len(conciertos) == 2
        assert conciertos[0]["id"] == 1
        assert conciertos[1]["id"] == 2


class TestListarConciertos:
    """Tests para la función listar_conciertos."""
    
    def test_listar_conciertos_vacio(self, temp_data_dir):
        """Test listar conciertos cuando no hay ninguno."""
        conciertos = listar_conciertos()
        assert conciertos == []
    
    def test_listar_conciertos_con_datos(self, temp_data_dir):
        """Test listar conciertos con datos existentes."""
        # Registrar algunos conciertos primero
        secciones1 = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
        secciones2 = [{"nombre": "General", "precio": "100", "stock": "50"}]
        
        registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones1)
        registrar_concierto("Imagine Dragons", "2025-11-15", "Guayaquil", secciones2)
        
        conciertos = listar_conciertos()
        assert len(conciertos) == 2
        assert conciertos[0]["artista"] == "Coldplay"
        assert conciertos[1]["artista"] == "Imagine Dragons"


class TestBuscarConciertoPorId:
    """Tests para la función buscar_concierto_por_id."""
    
    def test_buscar_concierto_lista_vacia(self, temp_data_dir):
        """Test buscar concierto cuando no hay conciertos."""
        concierto = buscar_concierto_por_id(1)
        assert concierto is None
