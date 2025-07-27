"""
Demostración de las mejoras implementadas en la interfaz BeatPass
Este archivo muestra ejemplos de los componentes mejorados
"""

import tkinter as tk
from tkinter import ttk
from gui_styles import *

def demo_componentes():
    """Función de demostración de los nuevos componentes"""
    
    # Crear ventana de demo
    demo_window = tk.Tk()
    demo_window.title("🎨 BeatPass - Demo de Componentes Mejorados")
    demo_window.geometry("800x600")
    demo_window.configure(bg=BEATPASS_COLORS['background'])
    
    # Frame principal con scroll
    main_frame = tk.Frame(demo_window, bg=BEATPASS_COLORS['background'])
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Título principal
    title = tk.Label(main_frame,
                    text="🎵 Componentes Mejorados de BeatPass",
                    font=BEATPASS_FONTS['title'],
                    fg=BEATPASS_COLORS['accent'],
                    bg=BEATPASS_COLORS['background'])
    title.pack(pady=(0, 20))
    
    # Demo de CardFrame
    card1 = CardFrame(main_frame, title="🎫 Tarjeta de Entrada")
    card1.pack(fill=tk.X, pady=10)
    
    demo_text1 = tk.Label(card1.content_frame,
                         text="Esta es una tarjeta estilizada que puede contener información\n"
                              "de entradas, conciertos o cualquier otro contenido.",
                         font=BEATPASS_FONTS['body'],
                         fg=BEATPASS_COLORS['text'],
                         bg=card1.content_frame['bg'],
                         justify=tk.LEFT)
    demo_text1.pack(padx=15, pady=15)
    
    # Demo de botones animados
    buttons_frame = tk.Frame(main_frame, bg=BEATPASS_COLORS['background'])
    buttons_frame.pack(fill=tk.X, pady=10)
    
    card2 = CardFrame(buttons_frame, title="🎮 Botones Interactivos")
    card2.pack(fill=tk.X)
    
    btn_frame = tk.Frame(card2.content_frame, bg=card2.content_frame['bg'])
    btn_frame.pack(padx=15, pady=15)
    
    AnimatedButton(btn_frame,
                  text="🎤 Botón Principal",
                  bg=BEATPASS_COLORS['accent'],
                  hover_bg=BEATPASS_COLORS['hover'],
                  fg=BEATPASS_COLORS['text'],
                  font=BEATPASS_FONTS['button'],
                  border=0,
                  relief=tk.FLAT,
                  padx=20,
                  pady=10,
                  cursor='hand2',
                  command=lambda: mostrar_toast("¡Botón presionado!", "success")).pack(side=tk.LEFT, padx=5)
    
    AnimatedButton(btn_frame,
                  text="🎪 Botón Secundario", 
                  bg=BEATPASS_COLORS['secondary'],
                  hover_bg=BEATPASS_COLORS['primary'],
                  fg=BEATPASS_COLORS['text'],
                  font=BEATPASS_FONTS['button'],
                  border=0,
                  relief=tk.FLAT,
                  padx=20,
                  pady=10,
                  cursor='hand2',
                  command=lambda: mostrar_toast("Función secundaria", "info")).pack(side=tk.LEFT, padx=5)
    
    # Demo de entradas estilizadas
    card3 = CardFrame(main_frame, title="📝 Campos de Entrada Mejorados")
    card3.pack(fill=tk.X, pady=10)
    
    entries_frame = tk.Frame(card3.content_frame, bg=card3.content_frame['bg'])
    entries_frame.pack(fill=tk.X, padx=15, pady=15)
    
    entry1 = StyledEntry(entries_frame, placeholder="🎤 Nombre del artista...")
    entry1.pack(fill=tk.X, pady=5)
    
    entry2 = StyledEntry(entries_frame, placeholder="📧 Correo electrónico...")
    entry2.pack(fill=tk.X, pady=5)
    
    entry3 = StyledEntry(entries_frame, placeholder="🏙️ Ciudad del evento...")
    entry3.pack(fill=tk.X, pady=5)
    
    # Demo de progreso circular
    card4 = CardFrame(main_frame, title="📊 Indicadores de Progreso")
    card4.pack(fill=tk.X, pady=10)
    
    progress_frame = tk.Frame(card4.content_frame, bg=card4.content_frame['bg'])
    progress_frame.pack(padx=15, pady=15)
    
    # Crear varios círculos de progreso
    progress_values = [25, 50, 75, 100]
    progress_labels = ["Registros", "Conciertos", "Ventas", "Completado"]
    
    for i, (value, label) in enumerate(zip(progress_values, progress_labels)):
        frame = tk.Frame(progress_frame, bg=progress_frame['bg'])
        frame.pack(side=tk.LEFT, padx=20)
        
        circle = ProgressCircle(frame, size=60, thickness=6, bg=progress_frame['bg'])
        circle.pack()
        circle.set_progress(value)
        
        label_widget = tk.Label(frame,
                               text=label,
                               font=BEATPASS_FONTS['small'],
                               fg=BEATPASS_COLORS['text'],
                               bg=progress_frame['bg'])
        label_widget.pack(pady=5)
    
    # Función para mostrar toasts
    def mostrar_toast(mensaje, tipo):
        NotificationToast(demo_window, mensaje, tipo)
    
    # Botones de demo para toasts
    card5 = CardFrame(main_frame, title="🔔 Notificaciones Toast")
    card5.pack(fill=tk.X, pady=10)
    
    toast_frame = tk.Frame(card5.content_frame, bg=card5.content_frame['bg'])
    toast_frame.pack(padx=15, pady=15)
    
    toast_types = [
        ("✅ Éxito", "success", "¡Operación completada con éxito!"),
        ("ℹ️ Info", "info", "Esta es una notificación informativa"),
        ("⚠️ Advertencia", "warning", "Advertencia: Revisa la información"),
        ("❌ Error", "error", "Ha ocurrido un error en la operación")
    ]
    
    for text, tipo, mensaje in toast_types:
        btn = AnimatedButton(toast_frame,
                           text=text,
                           bg=BEATPASS_COLORS['primary'],
                           hover_bg=BEATPASS_COLORS['secondary'],
                           fg=BEATPASS_COLORS['text'],
                           font=BEATPASS_FONTS['body'],
                           border=0,
                           relief=tk.FLAT,
                           padx=15,
                           pady=8,
                           cursor='hand2',
                           command=lambda m=mensaje, t=tipo: mostrar_toast(m, t))
        btn.pack(side=tk.LEFT, padx=5)
    
    # Frame de información final
    info_frame = tk.Frame(main_frame, bg=BEATPASS_COLORS['background'])
    info_frame.pack(fill=tk.X, pady=20)
    
    info_text = tk.Label(info_frame,
                        text="🎨 Estas mejoras hacen que BeatPass tenga una interfaz moderna y atractiva\n"
                             "✨ Los componentes son reutilizables y fáciles de personalizar\n"
                             "🚀 La experiencia del usuario es mucho más fluida e intuitiva",
                        font=BEATPASS_FONTS['body'],
                        fg=BEATPASS_COLORS['text_secondary'],
                        bg=BEATPASS_COLORS['background'],
                        justify=tk.CENTER)
    info_text.pack()
    
    # Botón para cerrar
    close_btn = AnimatedButton(info_frame,
                              text="🔙 Cerrar Demo",
                              bg=BEATPASS_COLORS['error'],
                              hover_bg='#c0392b',
                              fg=BEATPASS_COLORS['text'],
                              font=BEATPASS_FONTS['button'],
                              border=0,
                              relief=tk.FLAT,
                              padx=30,
                              pady=12,
                              cursor='hand2',
                              command=demo_window.destroy)
    close_btn.pack(pady=20)
    
    demo_window.mainloop()

if __name__ == "__main__":
    demo_componentes()
