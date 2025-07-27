import tkinter as tk
from tkinter import ttk, messagebox
from usuarios import registrar_usuario
from conciertos import listar_conciertos, buscar_concierto_por_id, registrar_concierto
from boletos import generar_boleto, mostrar_boletos_usuario

class BeatPassGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 BeatPass - Entradas para Conciertos")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a2e')
        
        # Configurar el estilo
        self.configurar_estilos()
        
        # Centrar la ventana en la pantalla
        self.centrar_ventana()
        
        self.crear_menu_principal()
    
    def configurar_estilos(self):
        """Configura los estilos y colores de la aplicación"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Colores del tema
        self.colores = {
            'primario': '#16213e',
            'secundario': '#0f3460', 
            'acento': '#e94560',
            'texto': '#ffffff',
            'texto_secundario': '#b8b8b8',
            'fondo': '#1a1a2e',
            'tarjeta': '#16213e',
            'hover': '#e94560'
        }
        
        # Configurar estilos de ttk
        style.configure('Custom.TCombobox', 
                       fieldbackground=self.colores['tarjeta'],
                       background=self.colores['primario'],
                       foreground=self.colores['texto'])
        
        style.configure('Custom.Treeview',
                       background=self.colores['tarjeta'],
                       foreground=self.colores['texto'],
                       fieldbackground=self.colores['tarjeta'])
        
        style.configure('Custom.Treeview.Heading',
                       background=self.colores['acento'],
                       foreground=self.colores['texto'],
                       font=('Segoe UI', 10, 'bold'))
    
    def centrar_ventana(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        pos_x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        pos_y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
    
    def crear_boton_estilizado(self, parent, texto, comando, icono="🎵", color_fondo=None):
        """Crea un botón con estilo personalizado"""
        if color_fondo is None:
            color_fondo = self.colores['acento']
            
        frame_boton = tk.Frame(parent, bg=parent['bg'])
        frame_boton.pack(pady=8, padx=20, fill=tk.X)
        
        boton = tk.Button(frame_boton, 
                         text=f"{icono} {texto}",
                         command=comando,
                         font=('Segoe UI', 12, 'bold'),
                         bg=color_fondo,
                         fg=self.colores['texto'],
                         activebackground=self.colores['hover'],
                         activeforeground=self.colores['texto'],
                         border=0,
                         relief=tk.FLAT,
                         padx=30,
                         pady=15,
                         cursor='hand2')
        
        boton.pack(fill=tk.X)
        
        # Efectos hover
        def on_enter(e):
            boton.configure(bg=self.colores['hover'])
            
        def on_leave(e):
            boton.configure(bg=color_fondo)
            
        boton.bind("<Enter>", on_enter)
        boton.bind("<Leave>", on_leave)
        
        return boton

    def crear_menu_principal(self):
        self.limpiar_ventana()

        # Frame principal con gradiente
        frame_principal = tk.Frame(self.root, bg=self.colores['fondo'])
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        # Header con logo y título
        frame_header = tk.Frame(frame_principal, bg=self.colores['fondo'])
        frame_header.pack(fill=tk.X, pady=(0, 30))
        
        titulo_principal = tk.Label(frame_header, 
                                  text="🎵 BeatPass", 
                                  font=('Segoe UI', 32, 'bold'),
                                  fg=self.colores['acento'],
                                  bg=self.colores['fondo'])
        titulo_principal.pack()
        
        subtitulo = tk.Label(frame_header,
                           text="Tu entrada al mundo de la música",
                           font=('Segoe UI', 14),
                           fg=self.colores['texto_secundario'],
                           bg=self.colores['fondo'])
        subtitulo.pack(pady=(5, 0))

        # Frame para los botones del menú
        frame_menu = tk.Frame(frame_principal, bg=self.colores['fondo'])
        frame_menu.pack(expand=True, fill=tk.BOTH)

        # Contenedor central para los botones
        contenedor_botones = tk.Frame(frame_menu, bg=self.colores['fondo'])
        contenedor_botones.pack(expand=True)

        # Botones del menú principal con iconos y colores
        self.crear_boton_estilizado(contenedor_botones, "Registrarse", 
                                   self.mostrar_formulario_registro, "👤")
        
        self.crear_boton_estilizado(contenedor_botones, "Ver Conciertos", 
                                   self.mostrar_lista_conciertos, "🎪")
        
        self.crear_boton_estilizado(contenedor_botones, "Comprar Entrada", 
                                   self.mostrar_formulario_compra, "🎫")
        
        self.crear_boton_estilizado(contenedor_botones, "Ver Mis Entradas", 
                                   self.mostrar_boletos_usuario, "📋")
        
        self.crear_boton_estilizado(contenedor_botones, "Registrar Concierto", 
                                   self.mostrar_formulario_registro_concierto, "🎤", 
                                   self.colores['secundario'])
        
        # Botón de salir con estilo diferente
        frame_salir = tk.Frame(frame_menu, bg=self.colores['fondo'])
        frame_salir.pack(side=tk.BOTTOM, pady=20)
        
        btn_salir = tk.Button(frame_salir, 
                            text="🚪 Salir",
                            command=self.root.quit,
                            font=('Segoe UI', 10),
                            bg='#2c2c54',
                            fg=self.colores['texto_secundario'],
                            activebackground='#40407a',
                            border=0,
                            relief=tk.FLAT,
                            padx=20,
                            pady=10,
                            cursor='hand2')
        btn_salir.pack()

    def crear_entrada_estilizada(self, parent, texto_label, ancho=40):
        """Crea una entrada de texto con estilo personalizado"""
        frame_entrada = tk.Frame(parent, bg=parent['bg'])
        frame_entrada.pack(pady=10, padx=20, fill=tk.X)
        
        label = tk.Label(frame_entrada, 
                        text=texto_label,
                        font=('Segoe UI', 11, 'bold'),
                        fg=self.colores['texto'],
                        bg=parent['bg'])
        label.pack(anchor=tk.W, pady=(0, 5))
        
        entrada = tk.Entry(frame_entrada,
                          font=('Segoe UI', 11),
                          bg=self.colores['tarjeta'],
                          fg=self.colores['texto'],
                          insertbackground=self.colores['texto'],
                          relief=tk.FLAT,
                          bd=0,
                          width=ancho)
        entrada.pack(fill=tk.X, ipady=8)
        
        # Borde inferior decorativo
        borde = tk.Frame(frame_entrada, height=2, bg=self.colores['acento'])
        borde.pack(fill=tk.X, pady=(1, 0))
        
        return entrada

    def crear_frame_contenido(self, titulo, icono="🎵"):
        """Crea un frame estilizado para el contenido"""
        frame_principal = tk.Frame(self.root, bg=self.colores['fondo'])
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Header
        frame_header = tk.Frame(frame_principal, bg=self.colores['fondo'])
        frame_header.pack(fill=tk.X, pady=(0, 20))
        
        titulo_frame = tk.Label(frame_header,
                               text=f"{icono} {titulo}",
                               font=('Segoe UI', 24, 'bold'),
                               fg=self.colores['acento'],
                               bg=self.colores['fondo'])
        titulo_frame.pack()
        
        # Frame de contenido
        frame_contenido = tk.Frame(frame_principal, 
                                 bg=self.colores['tarjeta'],
                                 relief=tk.FLAT,
                                 bd=0)
        frame_contenido.pack(fill=tk.BOTH, expand=True, pady=10)
        
        return frame_contenido

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_formulario_registro(self):
        self.limpiar_ventana()
        
        frame_contenido = self.crear_frame_contenido("Registro de Usuario", "👤")

        # Entradas estilizadas
        self.entry_nombre = self.crear_entrada_estilizada(frame_contenido, "📝 Nombre Completo:")
        self.entry_correo = self.crear_entrada_estilizada(frame_contenido, "📧 Correo Electrónico:")

        # Frame para botones
        frame_botones = tk.Frame(frame_contenido, bg=frame_contenido['bg'])
        frame_botones.pack(fill=tk.X, pady=30, padx=20)

        # Botón registrar
        btn_guardar = tk.Button(frame_botones, 
                               text="✅ Registrar",
                               command=self.registrar_nuevo_usuario,
                               font=('Segoe UI', 12, 'bold'),
                               bg=self.colores['acento'],
                               fg=self.colores['texto'],
                               activebackground=self.colores['hover'],
                               border=0,
                               relief=tk.FLAT,
                               padx=30,
                               pady=12,
                               cursor='hand2')
        btn_guardar.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)

        # Botón volver
        btn_volver = tk.Button(frame_botones, 
                              text="🔙 Volver al Menú",
                              command=self.crear_menu_principal,
                              font=('Segoe UI', 12),
                              bg=self.colores['secundario'],
                              fg=self.colores['texto'],
                              activebackground='#0f4c75',
                              border=0,
                              relief=tk.FLAT,
                              padx=30,
                              pady=12,
                              cursor='hand2')
        btn_volver.pack(side=tk.RIGHT, padx=(10, 0), fill=tk.X, expand=True)

    def registrar_nuevo_usuario(self):
        nombre = self.entry_nombre.get().strip()
        correo = self.entry_correo.get().strip()
        
        # Validación básica
        if not nombre or not correo:
            messagebox.showerror("❌ Error de Validación", 
                               "Por favor, complete todos los campos.")
            return
            
        mensaje = registrar_usuario(nombre, correo)
        if mensaje:
            messagebox.showerror("❌ Error en el Registro", mensaje)
            return
            
        messagebox.showinfo("✅ Registro Exitoso", 
                          f"¡Bienvenido/a {nombre}!\nUsuario registrado correctamente.")
        self.crear_menu_principal()

    def realizar_compra(self):
        correo = self.entry_correo_compra.get().strip()
        selected_concierto_index = self.combo_conciertos.current()
        selected_seccion_index = self.combo_secciones.current()

        # Validaciones
        if not correo:
            messagebox.showerror("❌ Error", "Por favor, ingrese su correo electrónico.")
            return
            
        if selected_concierto_index == -1:
            messagebox.showerror("❌ Error", "Por favor, seleccione un concierto.")
            return
            
        if selected_seccion_index == -1:
            messagebox.showerror("❌ Error", "Por favor, seleccione una sección.")
            return

        try:
            id_concierto = self.conciertos[selected_concierto_index]['id']
            nombre_seccion = self.combo_secciones.get()

            mensaje = generar_boleto(correo, id_concierto, nombre_seccion)
            if mensaje:
                messagebox.showerror("❌ Error en la Compra", mensaje)
            else:
                messagebox.showinfo("🎉 Compra Exitosa", 
                                  "¡Entrada comprada con éxito!\n"
                                  "Revisa tu correo para más detalles.")
                self.crear_menu_principal()
        except (IndexError, KeyError) as e:
            messagebox.showerror("❌ Error", "Error al procesar la compra. Intente nuevamente.")

    def registrar_nuevo_concierto(self):
        artista = self.entry_artista.get().strip()
        fecha = self.entry_fecha.get().strip()
        ciudad = self.entry_ciudad.get().strip()

        # Validaciones básicas
        if not artista or not fecha or not ciudad:
            messagebox.showerror("❌ Error de Validación", 
                               "Por favor, complete todos los campos del concierto.")
            return

        if not self.secciones_entries:
            messagebox.showerror("❌ Error de Validación", 
                               "Debe agregar al menos una sección.")
            return

        secciones = []
        for i, entry_set in enumerate(self.secciones_entries):
            nombre = entry_set['nombre'].get().strip()
            precio_str = entry_set['precio'].get().strip()
            stock_str = entry_set['stock'].get().strip()

            # Validar campos de sección
            if not nombre:
                messagebox.showerror("❌ Error de Sección", 
                                   f"El nombre de la sección {i+1} no puede estar vacío.")
                return
            
            if not precio_str:
                messagebox.showerror("❌ Error de Sección", 
                                   f"El precio de la sección {i+1} no puede estar vacío.")
                return
                
            if not stock_str:
                messagebox.showerror("❌ Error de Sección", 
                                   f"El stock de la sección {i+1} no puede estar vacío.")
                return
            
            try:
                precio = int(precio_str)
                if precio <= 0:
                    messagebox.showerror("❌ Error de Precio", 
                                       f"El precio de la sección {i+1} debe ser un número positivo.")
                    return
            except ValueError:
                messagebox.showerror("❌ Error de Precio", 
                                   f"El precio de la sección {i+1} debe ser un número válido.")
                return
            
            try:
                stock = int(stock_str)
                if stock <= 0:
                    messagebox.showerror("❌ Error de Stock", 
                                       f"El stock de la sección {i+1} debe ser un número positivo.")
                    return
            except ValueError:
                messagebox.showerror("❌ Error de Stock", 
                                   f"El stock de la sección {i+1} debe ser un número válido.")
                return
            
            secciones.append({"nombre": nombre, "precio": precio, "stock": stock})

        mensaje_error = registrar_concierto(artista, fecha, ciudad, secciones)

        if mensaje_error:
            messagebox.showerror("❌ Error de Registro", mensaje_error)
        else:
            messagebox.showinfo("🎉 Registro Exitoso", 
                              f"¡Concierto de {artista} registrado correctamente!\n"
                              f"Fecha: {fecha}\nCiudad: {ciudad}")
            self.crear_menu_principal()

    def mostrar_lista_conciertos(self):
        self.limpiar_ventana()
        
        frame_contenido = self.crear_frame_contenido("Conciertos Disponibles", "🎪")
        
        # Frame para la tabla
        frame_tabla = tk.Frame(frame_contenido, bg=frame_contenido['bg'])
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Crear Treeview estilizado
        tree = ttk.Treeview(frame_tabla, 
                           columns=("ID", "Artista", "Fecha", "Ciudad"), 
                           show="headings",
                           style="Custom.Treeview",
                           height=15)
        
        # Configurar columnas
        tree.heading("ID", text="🆔 ID")
        tree.heading("Artista", text="🎤 Artista")
        tree.heading("Fecha", text="📅 Fecha")
        tree.heading("Ciudad", text="🏙️ Ciudad")
        
        tree.column("ID", width=80, anchor=tk.CENTER)
        tree.column("Artista", width=250, anchor=tk.W)
        tree.column("Fecha", width=150, anchor=tk.CENTER)
        tree.column("Ciudad", width=200, anchor=tk.W)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Cargar datos
        conciertos = listar_conciertos()
        if conciertos:
            for i, c in enumerate(conciertos):
                # Alternar colores de fila
                tag = 'even' if i % 2 == 0 else 'odd'
                tree.insert("", tk.END, values=(c['id'], c['artista'], c['fecha'], c['ciudad']), tags=(tag,))
        else:
            # Mensaje cuando no hay conciertos
            no_data_label = tk.Label(frame_tabla,
                                   text="🎭 No hay conciertos disponibles en este momento",
                                   font=('Segoe UI', 14),
                                   fg=self.colores['texto_secundario'],
                                   bg=frame_contenido['bg'])
            no_data_label.pack(expand=True)
        
        # Configurar tags para alternar colores
        tree.tag_configure('even', background=self.colores['primario'])
        tree.tag_configure('odd', background=self.colores['tarjeta'])
        
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Botón volver
        frame_boton = tk.Frame(frame_contenido, bg=frame_contenido['bg'])
        frame_boton.pack(fill=tk.X, pady=20, padx=20)
        
        btn_volver = tk.Button(frame_boton, 
                              text="🔙 Volver al Menú",
                              command=self.crear_menu_principal,
                              font=('Segoe UI', 12, 'bold'),
                              bg=self.colores['secundario'],
                              fg=self.colores['texto'],
                              activebackground='#0f4c75',
                              border=0,
                              relief=tk.FLAT,
                              padx=30,
                              pady=12,
                              cursor='hand2')
        btn_volver.pack()

    def mostrar_formulario_compra(self):
        self.limpiar_ventana()
        
        frame_contenido = self.crear_frame_contenido("Comprar Entrada", "🎫")

        # Entrada de correo
        self.entry_correo_compra = self.crear_entrada_estilizada(frame_contenido, "📧 Correo del Usuario:")

        # Frame para selección de concierto
        frame_concierto = tk.Frame(frame_contenido, bg=frame_contenido['bg'])
        frame_concierto.pack(pady=10, padx=20, fill=tk.X)
        
        label_concierto = tk.Label(frame_concierto,
                                  text="🎪 Seleccionar Concierto:",
                                  font=('Segoe UI', 11, 'bold'),
                                  fg=self.colores['texto'],
                                  bg=frame_contenido['bg'])
        label_concierto.pack(anchor=tk.W, pady=(0, 5))
        
        self.combo_conciertos = ttk.Combobox(frame_concierto,
                                           font=('Segoe UI', 11),
                                           style="Custom.TCombobox",
                                           state="readonly")
        self.combo_conciertos.pack(fill=tk.X, ipady=8)

        # Frame para selección de sección
        frame_seccion = tk.Frame(frame_contenido, bg=frame_contenido['bg'])
        frame_seccion.pack(pady=10, padx=20, fill=tk.X)
        
        label_seccion = tk.Label(frame_seccion,
                               text="🎭 Seleccionar Sección:",
                               font=('Segoe UI', 11, 'bold'),
                               fg=self.colores['texto'],
                               bg=frame_contenido['bg'])
        label_seccion.pack(anchor=tk.W, pady=(0, 5))
        
        self.combo_secciones = ttk.Combobox(frame_seccion,
                                          font=('Segoe UI', 11),
                                          style="Custom.TCombobox",
                                          state="readonly")
        self.combo_secciones.pack(fill=tk.X, ipady=8)

        # Cargar conciertos y configurar eventos
        self.cargar_conciertos_en_combobox()
        self.combo_conciertos.bind("<<ComboboxSelected>>", self.actualizar_secciones)

        # Frame para botones
        frame_botones = tk.Frame(frame_contenido, bg=frame_contenido['bg'])
        frame_botones.pack(fill=tk.X, pady=30, padx=20)

        # Botón comprar
        btn_comprar = tk.Button(frame_botones,
                               text="💳 Comprar Entrada",
                               command=self.realizar_compra,
                               font=('Segoe UI', 12, 'bold'),
                               bg=self.colores['acento'],
                               fg=self.colores['texto'],
                               activebackground=self.colores['hover'],
                               border=0,
                               relief=tk.FLAT,
                               padx=30,
                               pady=12,
                               cursor='hand2')
        btn_comprar.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)

        # Botón volver
        btn_volver = tk.Button(frame_botones,
                              text="🔙 Volver al Menú",
                              command=self.crear_menu_principal,
                              font=('Segoe UI', 12),
                              bg=self.colores['secundario'],
                              fg=self.colores['texto'],
                              activebackground='#0f4c75',
                              border=0,
                              relief=tk.FLAT,
                              padx=30,
                              pady=12,
                              cursor='hand2')
        btn_volver.pack(side=tk.RIGHT, padx=(10, 0), fill=tk.X, expand=True)

    def cargar_conciertos_en_combobox(self):
        self.conciertos = listar_conciertos()
        if self.conciertos:
            self.combo_conciertos['values'] = [f"{c['artista']} en {c['ciudad']}" for c in self.conciertos]

    def actualizar_secciones(self, event):
        try:
            selected_concierto_index = self.combo_conciertos.current()
            if selected_concierto_index != -1:
                selected_concierto = self.conciertos[selected_concierto_index]
                self.combo_secciones['values'] = [s['nombre'] for s in selected_concierto['secciones']]
                self.combo_secciones.set("")
        except IndexError:
            messagebox.showerror("Error", "Índice de concierto fuera de rango.")
            self.combo_conciertos.set("")
            self.combo_secciones.set("")
            self.combo_secciones['values'] = []

    def realizar_compra(self):
        correo = self.entry_correo_compra.get()
        selected_concierto_index = self.combo_conciertos.current()
        selected_seccion_index = self.combo_secciones.current()

        if selected_concierto_index == -1 or selected_seccion_index == -1:
            messagebox.showerror("Error", "Por favor, seleccione un concierto y una sección.")
            return

        id_concierto = self.conciertos[selected_concierto_index]['id']
        nombre_seccion = self.combo_secciones.get()

        mensaje = generar_boleto(correo, id_concierto, nombre_seccion)
        if mensaje:
            messagebox.showerror("Error en la Compra", mensaje)
        else:
            messagebox.showinfo("Compra Exitosa", "¡Boleto comprado con éxito!")
            self.crear_menu_principal()

    def mostrar_boletos_usuario(self):
        self.limpiar_ventana()
        
        frame_contenido = self.crear_frame_contenido("Mis Entradas", "📋")

        # Entrada de correo
        self.entry_correo_ver = self.crear_entrada_estilizada(frame_contenido, "📧 Ingrese su Correo Electrónico:")

        # Frame para botones
        frame_botones = tk.Frame(frame_contenido, bg=frame_contenido['bg'])
        frame_botones.pack(fill=tk.X, pady=20, padx=20)

        # Botón buscar
        btn_buscar = tk.Button(frame_botones,
                              text="🔍 Buscar Mis Entradas",
                              command=self.buscar_y_mostrar_boletos,
                              font=('Segoe UI', 12, 'bold'),
                              bg=self.colores['acento'],
                              fg=self.colores['texto'],
                              activebackground=self.colores['hover'],
                              border=0,
                              relief=tk.FLAT,
                              padx=30,
                              pady=12,
                              cursor='hand2')
        btn_buscar.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)

        # Botón volver
        btn_volver = tk.Button(frame_botones,
                              text="🔙 Volver al Menú",
                              command=self.crear_menu_principal,
                              font=('Segoe UI', 12),
                              bg=self.colores['secundario'],
                              fg=self.colores['texto'],
                              activebackground='#0f4c75',
                              border=0,
                              relief=tk.FLAT,
                              padx=30,
                              pady=12,
                              cursor='hand2')
        btn_volver.pack(side=tk.RIGHT, padx=(10, 0), fill=tk.X, expand=True)

    def buscar_y_mostrar_boletos(self):
        correo = self.entry_correo_ver.get()
        if not correo:
            messagebox.showerror("❌ Error", "Por favor, ingrese su correo electrónico.")
            return
        
        boletos_o_error = mostrar_boletos_usuario(correo)

        if isinstance(boletos_o_error, str):
            messagebox.showerror("❌ Error", boletos_o_error)
            return

        boletos = boletos_o_error

        # Limpiar resultados previos
        if hasattr(self, 'frame_boletos_lista') and self.frame_boletos_lista.winfo_exists():
            self.frame_boletos_lista.destroy()
        if hasattr(self, 'no_boletos_label') and self.no_boletos_label.winfo_exists():
            self.no_boletos_label.destroy()

        if not boletos:
            # Frame para mensaje de no boletos
            frame_mensaje = tk.Frame(self.root, bg=self.colores['fondo'])
            frame_mensaje.pack(fill=tk.BOTH, expand=True, pady=20)
            
            self.no_boletos_label = tk.Label(frame_mensaje,
                                           text="🎫 No se encontraron entradas para este usuario",
                                           font=('Segoe UI', 16),
                                           fg=self.colores['texto_secundario'],
                                           bg=self.colores['fondo'])
            self.no_boletos_label.pack(expand=True)
            return

        # Frame para mostrar boletos
        self.frame_boletos_lista = tk.Frame(self.root, bg=self.colores['tarjeta'])
        self.frame_boletos_lista.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 30))

        # Título de resultados
        titulo_resultados = tk.Label(self.frame_boletos_lista,
                                   text="🎟️ Tus Entradas",
                                   font=('Segoe UI', 18, 'bold'),
                                   fg=self.colores['acento'],
                                   bg=self.colores['tarjeta'])
        titulo_resultados.pack(pady=20)

        # Frame para la tabla
        frame_tabla = tk.Frame(self.frame_boletos_lista, bg=self.colores['tarjeta'])
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Crear Treeview para boletos
        tree = ttk.Treeview(frame_tabla,
                           columns=("Artista", "Fecha", "Ciudad", "Sección", "Precio"),
                           show="headings",
                           style="Custom.Treeview",
                           height=10)

        # Configurar columnas
        tree.heading("Artista", text="🎤 Artista")
        tree.heading("Fecha", text="📅 Fecha")
        tree.heading("Ciudad", text="🏙️ Ciudad")
        tree.heading("Sección", text="🎭 Sección")
        tree.heading("Precio", text="💰 Precio")

        tree.column("Artista", width=200, anchor=tk.W)
        tree.column("Fecha", width=120, anchor=tk.CENTER)
        tree.column("Ciudad", width=150, anchor=tk.W)
        tree.column("Sección", width=120, anchor=tk.CENTER)
        tree.column("Precio", width=100, anchor=tk.CENTER)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        # Cargar datos de boletos
        for i, boleto in enumerate(boletos):
            concierto = buscar_concierto_por_id(boleto['concierto_id'])
            if concierto:
                tag = 'even' if i % 2 == 0 else 'odd'
                precio_texto = f"${boleto['precio']}"
                tree.insert("", tk.END, 
                           values=(concierto['artista'], concierto['fecha'], 
                                  concierto['ciudad'], boleto['seccion'], precio_texto),
                           tags=(tag,))

        # Configurar tags para alternar colores
        tree.tag_configure('even', background=self.colores['primario'])
        tree.tag_configure('odd', background=self.colores['tarjeta'])

        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Información adicional
        total_boletos = len(boletos)
        total_precio = sum(boleto['precio'] for boleto in boletos)
        
        frame_info = tk.Frame(self.frame_boletos_lista, bg=self.colores['tarjeta'])
        frame_info.pack(fill=tk.X, padx=20, pady=10)
        
        info_text = f"📊 Total de entradas: {total_boletos} | 💵 Gasto total: ${total_precio}"
        label_info = tk.Label(frame_info,
                            text=info_text,
                            font=('Segoe UI', 12, 'bold'),
                            fg=self.colores['acento'],
                            bg=self.colores['tarjeta'])
        label_info.pack()

    def mostrar_formulario_registro_concierto(self):
        self.limpiar_ventana()
        
        frame_contenido = self.crear_frame_contenido("Registrar Nuevo Concierto", "🎤")

        # Información del concierto
        self.entry_artista = self.crear_entrada_estilizada(frame_contenido, "🎤 Nombre del Artista:")
        self.entry_fecha = self.crear_entrada_estilizada(frame_contenido, "📅 Fecha del Concierto (YYYY-MM-DD):")
        self.entry_ciudad = self.crear_entrada_estilizada(frame_contenido, "🏙️ Ciudad:")

        # Frame para secciones
        frame_secciones_container = tk.Frame(frame_contenido, bg=frame_contenido['bg'])
        frame_secciones_container.pack(fill=tk.X, pady=20, padx=20)
        
        # Título de secciones
        titulo_secciones = tk.Label(frame_secciones_container,
                                   text="🎭 Configuración de Secciones",
                                   font=('Segoe UI', 14, 'bold'),
                                   fg=self.colores['acento'],
                                   bg=frame_contenido['bg'])
        titulo_secciones.pack(anchor=tk.W, pady=(0, 10))
        
        # Frame scrollable para secciones
        canvas = tk.Canvas(frame_secciones_container, bg=frame_contenido['bg'], height=200)
        scrollbar_secciones = ttk.Scrollbar(frame_secciones_container, orient="vertical", command=canvas.yview)
        self.frame_secciones = tk.Frame(canvas, bg=frame_contenido['bg'])
        
        self.frame_secciones.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.frame_secciones, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar_secciones.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar_secciones.pack(side="right", fill="y")
        
        self.secciones_entries = []
        self.agregar_seccion_entry()

        # Frame para botón agregar sección
        frame_agregar = tk.Frame(frame_contenido, bg=frame_contenido['bg'])
        frame_agregar.pack(fill=tk.X, pady=10, padx=20)
        
        btn_agregar_seccion = tk.Button(frame_agregar,
                                       text="➕ Agregar Sección",
                                       command=self.agregar_seccion_entry,
                                       font=('Segoe UI', 10, 'bold'),
                                       bg=self.colores['primario'],
                                       fg=self.colores['texto'],
                                       activebackground=self.colores['secundario'],
                                       border=0,
                                       relief=tk.FLAT,
                                       padx=20,
                                       pady=8,
                                       cursor='hand2')
        btn_agregar_seccion.pack()

        # Frame para botones principales
        frame_botones = tk.Frame(frame_contenido, bg=frame_contenido['bg'])
        frame_botones.pack(fill=tk.X, pady=30, padx=20)

        # Botón registrar concierto
        btn_guardar_concierto = tk.Button(frame_botones,
                                         text="🎪 Registrar Concierto",
                                         command=self.registrar_nuevo_concierto,
                                         font=('Segoe UI', 12, 'bold'),
                                         bg=self.colores['acento'],
                                         fg=self.colores['texto'],
                                         activebackground=self.colores['hover'],
                                         border=0,
                                         relief=tk.FLAT,
                                         padx=30,
                                         pady=12,
                                         cursor='hand2')
        btn_guardar_concierto.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)

        # Botón volver
        btn_volver = tk.Button(frame_botones,
                              text="🔙 Volver al Menú",
                              command=self.crear_menu_principal,
                              font=('Segoe UI', 12),
                              bg=self.colores['secundario'],
                              fg=self.colores['texto'],
                              activebackground='#0f4c75',
                              border=0,
                              relief=tk.FLAT,
                              padx=30,
                              pady=12,
                              cursor='hand2')
        btn_volver.pack(side=tk.RIGHT, padx=(10, 0), fill=tk.X, expand=True)

    def agregar_seccion_entry(self):
        # Frame para una sección individual
        frame_seccion = tk.Frame(self.frame_secciones, 
                               bg=self.colores['primario'],
                               relief=tk.FLAT,
                               bd=1)
        frame_seccion.pack(fill=tk.X, pady=5, padx=5)
        
        # Número de sección
        num_seccion = len(self.secciones_entries) + 1
        titulo_seccion = tk.Label(frame_seccion,
                                text=f"🎭 Sección {num_seccion}",
                                font=('Segoe UI', 11, 'bold'),
                                fg=self.colores['acento'],
                                bg=self.colores['primario'])
        titulo_seccion.pack(anchor=tk.W, padx=10, pady=(5, 0))
        
        # Frame para los campos de entrada
        frame_campos = tk.Frame(frame_seccion, bg=self.colores['primario'])
        frame_campos.pack(fill=tk.X, padx=10, pady=5)

        # Campo nombre
        frame_nombre = tk.Frame(frame_campos, bg=self.colores['primario'])
        frame_nombre.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        tk.Label(frame_nombre, text="Nombre:", 
                font=('Segoe UI', 9),
                fg=self.colores['texto'],
                bg=self.colores['primario']).pack(anchor=tk.W)
        
        entry_nombre = tk.Entry(frame_nombre,
                              font=('Segoe UI', 9),
                              bg=self.colores['tarjeta'],
                              fg=self.colores['texto'],
                              insertbackground=self.colores['texto'],
                              relief=tk.FLAT,
                              bd=0)
        entry_nombre.pack(fill=tk.X, ipady=4)

        # Campo precio
        frame_precio = tk.Frame(frame_campos, bg=self.colores['primario'])
        frame_precio.pack(side=tk.LEFT, padx=5)
        
        tk.Label(frame_precio, text="Precio:", 
                font=('Segoe UI', 9),
                fg=self.colores['texto'],
                bg=self.colores['primario']).pack(anchor=tk.W)
        
        entry_precio = tk.Entry(frame_precio,
                              font=('Segoe UI', 9),
                              bg=self.colores['tarjeta'],
                              fg=self.colores['texto'],
                              insertbackground=self.colores['texto'],
                              relief=tk.FLAT,
                              bd=0,
                              width=10)
        entry_precio.pack(ipady=4)

        # Campo stock
        frame_stock = tk.Frame(frame_campos, bg=self.colores['primario'])
        frame_stock.pack(side=tk.LEFT, padx=(5, 0))
        
        tk.Label(frame_stock, text="Stock:", 
                font=('Segoe UI', 9),
                fg=self.colores['texto'],
                bg=self.colores['primario']).pack(anchor=tk.W)
        
        entry_stock = tk.Entry(frame_stock,
                             font=('Segoe UI', 9),
                             bg=self.colores['tarjeta'],
                             fg=self.colores['texto'],
                             insertbackground=self.colores['texto'],
                             relief=tk.FLAT,
                             bd=0,
                             width=10)
        entry_stock.pack(ipady=4)

        # Botón eliminar sección (solo si hay más de una)
        if len(self.secciones_entries) > 0:
            btn_eliminar = tk.Button(frame_campos,
                                   text="🗑️",
                                   command=lambda: self.eliminar_seccion_entry(frame_seccion),
                                   font=('Segoe UI', 8),
                                   bg='#e74c3c',
                                   fg=self.colores['texto'],
                                   activebackground='#c0392b',
                                   border=0,
                                   relief=tk.FLAT,
                                   padx=5,
                                   pady=2,
                                   cursor='hand2')
            btn_eliminar.pack(side=tk.RIGHT, padx=(10, 0), pady=(15, 0))

        self.secciones_entries.append({
            "frame": frame_seccion,
            "nombre": entry_nombre,
            "precio": entry_precio,
            "stock": entry_stock
        })
    
    def eliminar_seccion_entry(self, frame_seccion):
        """Elimina una sección específica"""
        # Encontrar y remover la sección de la lista
        for i, entrada in enumerate(self.secciones_entries):
            if entrada["frame"] == frame_seccion:
                entrada["frame"].destroy()
                self.secciones_entries.pop(i)
                break
        
        # Renumerar las secciones restantes
        self.renumerar_secciones()
    
    def renumerar_secciones(self):
        """Renumera las secciones después de eliminar una"""
        for i, entrada in enumerate(self.secciones_entries):
            # Buscar el label del título y actualizarlo
            for widget in entrada["frame"].winfo_children():
                if isinstance(widget, tk.Label) and "Sección" in widget.cget("text"):
                    widget.config(text=f"🎭 Sección {i + 1}")
                    break

    def registrar_nuevo_concierto(self):
        artista = self.entry_artista.get().strip()
        fecha = self.entry_fecha.get().strip()
        ciudad = self.entry_ciudad.get().strip()

        secciones = []
        for i, entry_set in enumerate(self.secciones_entries):
            nombre = entry_set['nombre'].get().strip()
            precio_str = entry_set['precio'].get().strip()
            stock_str = entry_set['stock'].get().strip()

            if not nombre:
                messagebox.showerror("Error de Registro de Concierto", f"El nombre de la sección {i+1} no puede estar vacío.")
                return
            
            try:
                precio = int(precio_str)
                if precio <= 0:
                    messagebox.showerror("Error de Registro de Concierto", f"El precio de la sección {i+1} debe ser un número positivo.")
                    return
            except ValueError:
                messagebox.showerror("Error de Registro de Concierto", f"El precio de la sección {i+1} es inválido. Debe ser un número entero.")
                return
            
            try:
                stock = int(stock_str)
                if stock <= 0:
                    messagebox.showerror("Error de Registro de Concierto", f"El stock de la sección {i+1} debe ser un número positivo.")
                    return
            except ValueError:
                messagebox.showerror("Error de Registro de Concierto", f"El stock de la sección {i+1} es inválido. Debe ser un número entero.")
                return
            
            secciones.append({"nombre": nombre, "precio": precio, "stock": stock})

        mensaje_error = registrar_concierto(artista, fecha, ciudad, secciones)

        if mensaje_error:
            messagebox.showerror("Error de Registro de Concierto", mensaje_error)
        else:
            messagebox.showinfo("Registro de Concierto Exitoso", f"Concierto de {artista} registrado correctamente.")
            self.crear_menu_principal()

    def cargar_conciertos_en_combobox(self):
        self.conciertos = listar_conciertos()
        if self.conciertos:
            valores_combo = []
            for c in self.conciertos:
                texto = f"🎤 {c['artista']} - 📅 {c['fecha']} - 🏙️ {c['ciudad']}"
                valores_combo.append(texto)
            self.combo_conciertos['values'] = valores_combo
        else:
            self.combo_conciertos['values'] = ["No hay conciertos disponibles"]

    def actualizar_secciones(self, event):
        try:
            selected_concierto_index = self.combo_conciertos.current()
            if selected_concierto_index != -1 and selected_concierto_index < len(self.conciertos):
                selected_concierto = self.conciertos[selected_concierto_index]
                valores_secciones = []
                for s in selected_concierto['secciones']:
                    valores_secciones.append(s['nombre'])  # Solo el nombre para la lógica
                self.combo_secciones['values'] = valores_secciones
                self.combo_secciones.set("")
        except (IndexError, KeyError):
            messagebox.showerror("❌ Error", "Error al cargar las secciones del concierto.")
            self.combo_conciertos.set("")
            self.combo_secciones.set("")
            self.combo_secciones['values'] = []

if __name__ == "__main__":
    root = tk.Tk()
    
    # Configurar icono de la ventana (opcional)
    try:
        # Si tienes un archivo de icono, puedes descomentarlo
        # root.iconbitmap('icon.ico')
        pass
    except:
        pass
    
    # Hacer que la ventana sea redimensionable
    root.minsize(800, 600)
    
    app = BeatPassGUI(root)
    root.mainloop()
