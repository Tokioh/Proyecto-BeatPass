import tkinter as tk
from tkinter import ttk, messagebox
from usuarios import registrar_usuario
from conciertos import listar_conciertos, buscar_concierto_por_id, registrar_concierto
from boletos import generar_boleto, mostrar_boletos_usuario

class BeatPassGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BeatPass - Entradas para Conciertos")
        self.root.geometry("800x600")

        self.crear_menu_principal()

    def crear_menu_principal(self):
        self.limpiar_ventana()

        frame_menu = tk.Frame(self.root)
        frame_menu.pack(pady=20)

        titulo = tk.Label(frame_menu, text="Bienvenido a BeatPass", font=("Arial", 24, "bold"))
        titulo.pack(pady=10)

        btn_registrar = tk.Button(frame_menu, text="Registrarse", command=self.mostrar_formulario_registro)
        btn_registrar.pack(pady=5, fill=tk.X)

        btn_ver_conciertos = tk.Button(frame_menu, text="Ver Conciertos", command=self.mostrar_lista_conciertos)
        btn_ver_conciertos.pack(pady=5, fill=tk.X)

        btn_comprar_boleto = tk.Button(frame_menu, text="Comprar Entrada", command=self.mostrar_formulario_compra)
        btn_comprar_boleto.pack(pady=5, fill=tk.X)

        btn_ver_boletos = tk.Button(frame_menu, text="Ver Mis Entradas", command=self.mostrar_boletos_usuario)
        btn_ver_boletos.pack(pady=5, fill=tk.X)

        btn_registrar_concierto = tk.Button(frame_menu, text="Registrar Concierto", command=self.mostrar_formulario_registro_concierto)
        btn_registrar_concierto.pack(pady=5, fill=tk.X)

        btn_salir = tk.Button(frame_menu, text="Salir", command=self.root.quit)
        btn_salir.pack(pady=20, fill=tk.X)

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_formulario_registro(self):
        self.limpiar_ventana()

        frame_registro = tk.Frame(self.root)
        frame_registro.pack(pady=20)

        tk.Label(frame_registro, text="Nombre Completo:", font=("Arial", 12)).pack(pady=5)
        self.entry_nombre = tk.Entry(frame_registro, width=40)
        self.entry_nombre.pack()

        tk.Label(frame_registro, text="Correo Electrónico:", font=("Arial", 12)).pack(pady=5)
        self.entry_correo = tk.Entry(frame_registro, width=40)
        self.entry_correo.pack()

        btn_guardar = tk.Button(frame_registro, text="Registrar", command=self.registrar_nuevo_usuario)
        btn_guardar.pack(pady=20)

        btn_volver = tk.Button(frame_registro, text="Volver al Menú", command=self.crear_menu_principal)
        btn_volver.pack()

    def registrar_nuevo_usuario(self):
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        mensaje = registrar_usuario(nombre, correo)
        if mensaje:
            messagebox.showerror("Error en la Compra", mensaje)
            return
        messagebox.showinfo("Registro Exitoso", f"Usuario {nombre} registrado correctamente.")
        self.crear_menu_principal()

    def mostrar_lista_conciertos(self):
        self.limpiar_ventana()
        frame_conciertos = tk.Frame(self.root)
        frame_conciertos.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        tk.Label(frame_conciertos, text="Conciertos Disponibles", font=("Arial", 18, "bold")).pack(pady=10)
        tree = ttk.Treeview(frame_conciertos, columns=("ID", "Artista", "Fecha", "Ciudad"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Artista", text="Artista")
        tree.heading("Fecha", text="Fecha")
        tree.heading("Ciudad", text="Ciudad")
        conciertos = listar_conciertos()
        if conciertos:
            for c in conciertos:
                tree.insert("", tk.END, values=(c['id'], c['artista'], c['fecha'], c['ciudad']))
        tree.pack(pady=10, fill=tk.BOTH, expand=True)
        btn_volver = tk.Button(frame_conciertos, text="Volver al Menú", command=self.crear_menu_principal)
        btn_volver.pack(pady=10)

    def mostrar_formulario_compra(self):
        self.limpiar_ventana()
        frame_compra = tk.Frame(self.root)
        frame_compra.pack(pady=20)

        tk.Label(frame_compra, text="Correo del Usuario:", font=("Arial", 12)).pack(pady=5)
        self.entry_correo_compra = tk.Entry(frame_compra, width=40)
        self.entry_correo_compra.pack()

        tk.Label(frame_compra, text="Concierto:", font=("Arial", 12)).pack(pady=5)
        self.combo_conciertos = ttk.Combobox(frame_compra, width=38)
        self.combo_conciertos.pack()

        tk.Label(frame_compra, text="Sección:", font=("Arial", 12)).pack(pady=5)
        self.combo_secciones = ttk.Combobox(frame_compra, width=38)
        self.combo_secciones.pack()

        self.cargar_conciertos_en_combobox()
        self.combo_conciertos.bind("<<ComboboxSelected>>", self.actualizar_secciones)

        btn_comprar = tk.Button(frame_compra, text="Comprar", command=self.realizar_compra)
        btn_comprar.pack(pady=20)
        btn_volver = tk.Button(frame_compra, text="Volver al Menú", command=self.crear_menu_principal)
        btn_volver.pack()

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
        frame_boletos = tk.Frame(self.root)
        frame_boletos.pack(pady=20)
        tk.Label(frame_boletos, text="Correo del Usuario:", font=("Arial", 12)).pack(pady=5)
        self.entry_correo_ver = tk.Entry(frame_boletos, width=40)
        self.entry_correo_ver.pack()
        btn_buscar = tk.Button(frame_boletos, text="Buscar Boletos", command=self.buscar_y_mostrar_boletos)
        btn_buscar.pack(pady=10)
        btn_volver = tk.Button(frame_boletos, text="Volver al Menú", command=self.crear_menu_principal)
        btn_volver.pack()

    def buscar_y_mostrar_boletos(self):
        correo = self.entry_correo_ver.get()
        boletos = mostrar_boletos_usuario(correo)

        for widget in self.root.winfo_children():
            if isinstance(widget, (ttk.Treeview, tk.Text)):
                widget.destroy()

        if not boletos:
            tk.Label(self.root, text="No se encontraron boletos para este usuario.", font=("Arial", 12)).pack(pady=20)
            return

        frame_boletos_lista = tk.Frame(self.root)
        frame_boletos_lista.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        tree = ttk.Treeview(frame_boletos_lista, columns=("Artista", "Fecha", "Ciudad", "Sección"), show="headings")
        tree.heading("Artista", text="Artista")
        tree.heading("Fecha", text="Fecha")
        tree.heading("Ciudad", text="Ciudad")
        tree.heading("Sección", text="Sección")

        for boleto in boletos:
            concierto = buscar_concierto_por_id(boleto['concierto_id'])
            if concierto:
                tree.insert("", tk.END, values=(concierto['artista'], concierto['fecha'], concierto['ciudad'], boleto['seccion']))

        tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def mostrar_formulario_registro_concierto(self):
        self.limpiar_ventana()

        frame_concierto = tk.Frame(self.root)
        frame_concierto.pack(pady=20)

        tk.Label(frame_concierto, text="Artista:", font=("Arial", 12)).pack(pady=5)
        self.entry_artista = tk.Entry(frame_concierto, width=40)
        self.entry_artista.pack()

        tk.Label(frame_concierto, text="Fecha (YYYY-MM-DD):", font=("Arial", 12)).pack(pady=5)
        self.entry_fecha = tk.Entry(frame_concierto, width=40)
        self.entry_fecha.pack()

        tk.Label(frame_concierto, text="Ciudad:", font=("Arial", 12)).pack(pady=5)
        self.entry_ciudad = tk.Entry(frame_concierto, width=40)
        self.entry_ciudad.pack()

        tk.Label(frame_concierto, text="Secciones:", font=("Arial", 12)).pack(pady=10)
        self.frame_secciones = tk.Frame(frame_concierto)
        self.frame_secciones.pack()
        self.secciones_entries = []
        self.agregar_seccion_entry()

        btn_agregar_seccion = tk.Button(frame_concierto, text="+", command=self.agregar_seccion_entry)
        btn_agregar_seccion.pack(pady=5)

        btn_guardar_concierto = tk.Button(frame_concierto, text="Registrar Concierto", command=self.registrar_nuevo_concierto)
        btn_guardar_concierto.pack(pady=20)

        btn_volver = tk.Button(frame_concierto, text="Volver al Menú", command=self.crear_menu_principal)
        btn_volver.pack()

    def agregar_seccion_entry(self):
        frame_seccion = tk.Frame(self.frame_secciones)
        frame_seccion.pack(pady=2)

        tk.Label(frame_seccion, text="Nombre:").pack(side=tk.LEFT)
        entry_nombre = tk.Entry(frame_seccion, width=15)
        entry_nombre.pack(side=tk.LEFT, padx=5)

        tk.Label(frame_seccion, text="Precio:").pack(side=tk.LEFT)
        entry_precio = tk.Entry(frame_seccion, width=10)
        entry_precio.pack(side=tk.LEFT, padx=5)

        tk.Label(frame_seccion, text="Stock:").pack(side=tk.LEFT)
        entry_stock = tk.Entry(frame_seccion, width=10)
        entry_stock.pack(side=tk.LEFT, padx=5)

        self.secciones_entries.append({
            "nombre": entry_nombre,
            "precio": entry_precio,
            "stock": entry_stock
        })

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

if __name__ == "__main__":
    root = tk.Tk()
    app = BeatPassGUI(root)
    root.mainloop()
