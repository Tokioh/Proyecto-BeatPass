import pytest
from usuarios import registrar_usuario
from conciertos import registrar_concierto
from boletos import generar_boleto, mostrar_boletos_usuario

class TestIntegracionCompleta:
    """Tests de integración que prueban el flujo completo del sistema."""
    
    def test_flujo_completo_compra_boleto(self, temp_data_dir):
        """Test del flujo completo: registro de usuario -> registro de concierto -> compra de boleto."""
        
        # 1. Registrar usuario
        resultado_usuario = registrar_usuario("Juan Pérez", "juan@email.com")
        assert resultado_usuario is None
        
        # 2. Registrar concierto
        secciones = [
            {"nombre": "VIP", "precio": "200", "stock": "5"},
            {"nombre": "General", "precio": "100", "stock": "50"}
        ]
        resultado_concierto = registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        assert resultado_concierto is None
        
        # 3. Comprar boleto
        resultado_boleto = generar_boleto("juan@email.com", 1, "VIP")
        assert resultado_boleto is None
        
        # 4. Verificar boletos del usuario
        boletos = mostrar_boletos_usuario("juan@email.com")
        assert len(boletos) == 1
        assert boletos[0]["usuario"] == "juan@email.com"
        assert boletos[0]["concierto_id"] == 1
        assert boletos[0]["seccion"] == "VIP"
        assert boletos[0]["precio"] == 200
    
    def test_flujo_multiple_usuarios_mismo_concierto(self, temp_data_dir):
        """Test múltiples usuarios comprando boletos para el mismo concierto."""
        
        # Registrar usuarios
        registrar_usuario("Juan Pérez", "juan@email.com")
        registrar_usuario("María García", "maria@email.com")
        registrar_usuario("Carlos López", "carlos@email.com")
        
        # Registrar concierto
        secciones = [
            {"nombre": "VIP", "precio": "200", "stock": "2"},
            {"nombre": "General", "precio": "100", "stock": "10"}
        ]
        registrar_concierto("Imagine Dragons", "2025-11-15", "Guayaquil", secciones)
        
        # Comprar boletos
        assert generar_boleto("juan@email.com", 1, "VIP") is None
        assert generar_boleto("maria@email.com", 1, "VIP") is None
        assert generar_boleto("carlos@email.com", 1, "General") is None
        
        # Verificar que se agotó el stock de VIP
        resultado_sin_stock = generar_boleto("juan@email.com", 1, "VIP")
        assert "No hay más boletos" in resultado_sin_stock
        
        # Verificar boletos individuales
        boletos_juan = mostrar_boletos_usuario("juan@email.com")
        boletos_maria = mostrar_boletos_usuario("maria@email.com")
        boletos_carlos = mostrar_boletos_usuario("carlos@email.com")
        
        assert len(boletos_juan) == 1
        assert len(boletos_maria) == 1
        assert len(boletos_carlos) == 1
        
        assert boletos_juan[0]["seccion"] == "VIP"
        assert boletos_maria[0]["seccion"] == "VIP"
        assert boletos_carlos[0]["seccion"] == "General"
    
    def test_flujo_usuario_multiples_conciertos(self, temp_data_dir):
        """Test un usuario comprando boletos para múltiples conciertos."""
        
        # Registrar usuario
        registrar_usuario("Juan Pérez", "juan@email.com")
        
        # Registrar múltiples conciertos
        secciones1 = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
        secciones2 = [{"nombre": "General", "precio": "150", "stock": "20"}]
        secciones3 = [{"nombre": "Platino", "precio": "300", "stock": "5"}]
        
        registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones1)
        registrar_concierto("Imagine Dragons", "2025-11-15", "Guayaquil", secciones2)
        registrar_concierto("Ed Sheeran", "2025-10-20", "Cuenca", secciones3)
        
        # Comprar boletos para cada concierto
        assert generar_boleto("juan@email.com", 1, "VIP") is None
        assert generar_boleto("juan@email.com", 2, "General") is None
        assert generar_boleto("juan@email.com", 3, "Platino") is None
        
        # Verificar todos los boletos del usuario
        boletos = mostrar_boletos_usuario("juan@email.com")
        assert len(boletos) == 3
        
        conciertos_ids = [b["concierto_id"] for b in boletos]
        assert 1 in conciertos_ids
        assert 2 in conciertos_ids
        assert 3 in conciertos_ids
        
        # Verificar precios
        total_gastado = sum(b["precio"] for b in boletos)
        assert total_gastado == 650  # 200 + 150 + 300
    
    def test_flujo_error_usuario_no_registrado(self, temp_data_dir):
        """Test del flujo cuando se intenta comprar sin estar registrado."""
        
        # Registrar concierto sin registrar usuario
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
        registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        
        # Intentar comprar boleto sin estar registrado
        resultado = generar_boleto("noregistrado@email.com", 1, "VIP")
        assert "no está registrado" in resultado
        
        # Verificar que no se generó ningún boleto
        # Como el usuario no está registrado, no podemos usar mostrar_boletos_usuario
        from boletos import cargar_boletos_json
        boletos = cargar_boletos_json()
        assert len(boletos) == 0
    
    def test_flujo_validaciones_consecutivas(self, temp_data_dir):
        """Test que las validaciones funcionan correctamente en secuencia."""
        
        # 1. Intentar registrar usuario con datos inválidos
        assert "nombre no puede estar vacío" in registrar_usuario("", "juan@email.com")
        assert "Correo electrónico inválido" in registrar_usuario("Juan", "email-invalido")
        
        # 2. Registrar usuario correctamente
        assert registrar_usuario("Juan Pérez", "juan@email.com") is None
        
        # 3. Intentar registrar concierto con datos inválidos
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "10"}]
        assert "artista no puede estar vacío" in registrar_concierto("", "2025-12-25", "Quito", secciones)
        assert "fecha debe ser en el futuro" in registrar_concierto("Coldplay", "2020-01-01", "Quito", secciones)
        
        # 4. Registrar concierto correctamente
        assert registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones) is None
        
        # 5. Intentar comprar boleto con datos inválidos
        assert "Concierto no encontrado" in generar_boleto("juan@email.com", 999, "VIP")
        assert "Sección no encontrada" in generar_boleto("juan@email.com", 1, "NoExiste")
        
        # 6. Comprar boleto correctamente
        assert generar_boleto("juan@email.com", 1, "VIP") is None
        
        # 7. Verificar el resultado final
        boletos = mostrar_boletos_usuario("juan@email.com")
        assert len(boletos) == 1

class TestIntegracionDatos:
    """Tests de integración enfocados en la persistencia de datos."""
    
    def test_persistencia_datos_entre_operaciones(self, temp_data_dir):
        """Test que los datos se mantienen entre diferentes operaciones."""
        
        # Registrar datos iniciales
        registrar_usuario("Juan Pérez", "juan@email.com")
        secciones = [{"nombre": "VIP", "precio": "200", "stock": "5"}]
        registrar_concierto("Coldplay", "2025-12-25", "Quito", secciones)
        generar_boleto("juan@email.com", 1, "VIP")
        
        # Verificar que los datos persisten después de más operaciones
        registrar_usuario("María García", "maria@email.com")
        generar_boleto("maria@email.com", 1, "VIP")
        
        # Verificar que ambos usuarios mantienen sus boletos
        boletos_juan = mostrar_boletos_usuario("juan@email.com")
        boletos_maria = mostrar_boletos_usuario("maria@email.com")
        
        assert len(boletos_juan) == 1
        assert len(boletos_maria) == 1
        assert boletos_juan[0]["usuario"] == "juan@email.com"
        assert boletos_maria[0]["usuario"] == "maria@email.com"
    

