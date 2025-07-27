"""
Archivo de estilos y componentes personalizados para BeatPass GUI
Este archivo contiene widgets personalizados y configuraciones de estilo avanzadas
"""

import tkinter as tk
from tkinter import ttk
import math

class GradientFrame(tk.Frame):
    """Frame con gradiente de fondo"""
    def __init__(self, parent, color1="#1a1a2e", color2="#16213e", **kwargs):
        super().__init__(parent, **kwargs)
        self.color1 = color1
        self.color2 = color2
        self.bind('<Configure>', self._draw_gradient)
        
    def _draw_gradient(self, event=None):
        """Dibuja un gradiente en el fondo del frame"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        
        if width > 1 and height > 1:
            canvas = tk.Canvas(self, width=width, height=height)
            canvas.place(x=0, y=0)
            
            # Crear gradiente vertical
            r1, g1, b1 = self._hex_to_rgb(self.color1)
            r2, g2, b2 = self._hex_to_rgb(self.color2)
            
            for i in range(height):
                ratio = i / height
                r = int(r1 + (r2 - r1) * ratio)
                g = int(g1 + (g2 - g1) * ratio)
                b = int(b1 + (b2 - b1) * ratio)
                color = f"#{r:02x}{g:02x}{b:02x}"
                canvas.create_line(0, i, width, i, fill=color)
                
    def _hex_to_rgb(self, hex_color):
        """Convierte color hexadecimal a RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

class AnimatedButton(tk.Button):
    """Botón con animaciones hover"""
    def __init__(self, parent, **kwargs):
        self.normal_bg = kwargs.get('bg', '#e94560')
        self.hover_bg = kwargs.pop('hover_bg', '#ff6b8a')  # Remover hover_bg de kwargs
        self.animation_speed = kwargs.pop('animation_speed', 50)
        
        super().__init__(parent, **kwargs)
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
        
    def _on_enter(self, event):
        """Animación de entrada del mouse"""
        self.configure(bg=self.hover_bg)
        self.configure(relief=tk.RAISED)
        
    def _on_leave(self, event):
        """Animación de salida del mouse"""
        self.configure(bg=self.normal_bg)
        self.configure(relief=tk.FLAT)

class StyledEntry(tk.Frame):
    """Entry con placeholder y estilos personalizados"""
    def __init__(self, parent, placeholder="", **kwargs):
        super().__init__(parent, bg=kwargs.get('bg', '#16213e'))
        
        self.placeholder = placeholder
        self.placeholder_color = '#808080'
        self.normal_color = '#ffffff'
        
        # Entry principal
        self.entry = tk.Entry(self, 
                             font=('Segoe UI', 11),
                             bg='#16213e',
                             fg=self.normal_color,
                             insertbackground=self.normal_color,
                             relief=tk.FLAT,
                             bd=0,
                             **kwargs)
        self.entry.pack(fill=tk.X, ipady=8, padx=5, pady=5)
        
        # Borde inferior
        self.border = tk.Frame(self, height=2, bg='#e94560')
        self.border.pack(fill=tk.X)
        
        # Configurar placeholder
        self._set_placeholder()
        self.entry.bind('<FocusIn>', self._on_focus_in)
        self.entry.bind('<FocusOut>', self._on_focus_out)
        
    def _set_placeholder(self):
        """Establece el texto placeholder"""
        self.entry.insert(0, self.placeholder)
        self.entry.configure(fg=self.placeholder_color)
        
    def _on_focus_in(self, event):
        """Evento cuando el entry recibe foco"""
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, tk.END)
            self.entry.configure(fg=self.normal_color)
        self.border.configure(bg='#ff6b8a')
            
    def _on_focus_out(self, event):
        """Evento cuando el entry pierde foco"""
        if not self.entry.get():
            self._set_placeholder()
        self.border.configure(bg='#e94560')
            
    def get(self):
        """Obtiene el valor del entry"""
        value = self.entry.get()
        return "" if value == self.placeholder else value
        
    def set(self, value):
        """Establece el valor del entry"""
        self.entry.delete(0, tk.END)
        if value:
            self.entry.insert(0, value)
            self.entry.configure(fg=self.normal_color)
        else:
            self._set_placeholder()

class NotificationToast(tk.Toplevel):
    """Notificación toast personalizada"""
    def __init__(self, parent, message, tipo="info", duration=3000):
        super().__init__(parent)
        
        # Configuraciones de la ventana
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        
        # Colores según el tipo
        colors = {
            'info': ('#3498db', '#ffffff'),
            'success': ('#27ae60', '#ffffff'), 
            'warning': ('#f39c12', '#ffffff'),
            'error': ('#e74c3c', '#ffffff')
        }
        
        bg_color, fg_color = colors.get(tipo, colors['info'])
        
        # Frame principal
        frame = tk.Frame(self, bg=bg_color, padx=20, pady=15)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Mensaje
        label = tk.Label(frame, 
                        text=message,
                        font=('Segoe UI', 10, 'bold'),
                        bg=bg_color,
                        fg=fg_color)
        label.pack()
        
        # Posicionar en la esquina superior derecha
        self.update_idletasks()
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()
        
        screen_width = self.winfo_screenwidth()
        x = screen_width - width - 20
        y = 20
        
        self.geometry(f'{width}x{height}+{x}+{y}')
        
        # Auto-cerrar después del tiempo especificado
        self.after(duration, self.destroy)
        
        # Animación de entrada
        self._animate_in()
        
    def _animate_in(self):
        """Animación de entrada del toast"""
        self.attributes('-alpha', 0.0)
        self._fade_in()
        
    def _fade_in(self, alpha=0.0):
        """Efecto fade in"""
        alpha += 0.1
        self.attributes('-alpha', alpha)
        if alpha < 1.0:
            self.after(50, lambda: self._fade_in(alpha))

class ProgressCircle(tk.Canvas):
    """Indicador de progreso circular"""
    def __init__(self, parent, size=50, thickness=5, **kwargs):
        super().__init__(parent, width=size, height=size, **kwargs)
        
        self.size = size
        self.thickness = thickness
        self.progress = 0
        self.max_progress = 100
        
        self.configure(bg=kwargs.get('bg', '#1a1a2e'), highlightthickness=0)
        
    def set_progress(self, value):
        """Establece el progreso (0-100)"""
        self.progress = max(0, min(value, self.max_progress))
        self._draw()
        
    def _draw(self):
        """Dibuja el círculo de progreso"""
        self.delete("all")
        
        # Círculo de fondo
        margin = self.thickness
        self.create_oval(margin, margin, 
                        self.size - margin, self.size - margin,
                        outline='#2c2c54', width=self.thickness)
        
        # Círculo de progreso
        if self.progress > 0:
            extent = (self.progress / self.max_progress) * 360
            self.create_arc(margin, margin,
                           self.size - margin, self.size - margin,
                           start=90, extent=-extent,
                           outline='#e94560', width=self.thickness,
                           style='arc')
        
        # Texto del porcentaje
        self.create_text(self.size // 2, self.size // 2,
                        text=f"{self.progress}%",
                        font=('Segoe UI', 8, 'bold'),
                        fill='#ffffff')

class CardFrame(tk.Frame):
    """Frame estilo tarjeta con sombra"""
    def __init__(self, parent, title="", **kwargs):
        super().__init__(parent, **kwargs)
        
        # Frame principal con efecto de sombra
        self.configure(bg='#0f0f23', relief=tk.FLAT, bd=0)
        
        # Frame de contenido
        self.content_frame = tk.Frame(self, 
                                     bg='#16213e',
                                     relief=tk.FLAT,
                                     bd=0)
        self.content_frame.pack(fill=tk.BOTH, expand=True, 
                               padx=2, pady=2)
        
        if title:
            # Header de la tarjeta
            header = tk.Frame(self.content_frame, 
                            bg='#e94560',
                            height=40)
            header.pack(fill=tk.X)
            header.pack_propagate(False)
            
            title_label = tk.Label(header,
                                  text=title,
                                  font=('Segoe UI', 12, 'bold'),
                                  bg='#e94560',
                                  fg='#ffffff')
            title_label.pack(expand=True)

# Funciones de utilidad para efectos especiales
def add_shadow_effect(widget, color='#000000', offset=(2, 2)):
    """Agrega efecto de sombra a un widget"""
    shadow = tk.Frame(widget.master,
                     bg=color,
                     width=widget.winfo_reqwidth() + offset[0],
                     height=widget.winfo_reqheight() + offset[1])
    
    # Posicionar la sombra detrás del widget
    shadow.place(x=widget.winfo_x() + offset[0],
                y=widget.winfo_y() + offset[1])
    
    # Traer el widget al frente
    widget.lift()

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    """Crea un rectángulo con esquinas redondeadas en un Canvas"""
    points = []
    
    # Esquina superior izquierda
    for i in range(90, 181, 1):
        x = x1 + radius - radius * math.cos(math.radians(i))
        y = y1 + radius - radius * math.sin(math.radians(i))
        points.extend([x, y])
    
    # Esquina superior derecha
    for i in range(0, 91, 1):
        x = x2 - radius + radius * math.cos(math.radians(i))
        y = y1 + radius - radius * math.sin(math.radians(i))
        points.extend([x, y])
    
    # Esquina inferior derecha
    for i in range(270, 361, 1):
        x = x2 - radius + radius * math.cos(math.radians(i))
        y = y2 - radius + radius * math.sin(math.radians(i))
        points.extend([x, y])
    
    # Esquina inferior izquierda
    for i in range(180, 271, 1):
        x = x1 + radius - radius * math.cos(math.radians(i))
        y = y2 - radius + radius * math.sin(math.radians(i))
        points.extend([x, y])
    
    return canvas.create_polygon(points, smooth=True, **kwargs)

class ModernScrollbar(ttk.Scrollbar):
    """Scrollbar con estilo moderno"""
    def __init__(self, parent, **kwargs):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar estilos del scrollbar
        style.configure("Modern.Vertical.TScrollbar",
                       gripcount=0,
                       background='#2c2c54',
                       darkcolor='#1a1a2e',
                       lightcolor='#2c2c54',
                       troughcolor='#1a1a2e',
                       bordercolor='#2c2c54',
                       arrowcolor='#e94560',
                       focuscolor='none')
        
        style.map("Modern.Vertical.TScrollbar",
                 background=[('active', '#e94560'),
                           ('pressed', '#ff6b8a')])
        
        super().__init__(parent, style="Modern.Vertical.TScrollbar", **kwargs)

# Paleta de colores recomendada
BEATPASS_COLORS = {
    'primary': '#16213e',
    'secondary': '#0f3460',
    'accent': '#e94560',
    'success': '#27ae60',
    'warning': '#f39c12',
    'error': '#e74c3c',
    'info': '#3498db',
    'text': '#ffffff',
    'text_secondary': '#b8b8b8',
    'background': '#1a1a2e',
    'card': '#16213e',
    'hover': '#ff6b8a',
    'border': '#2c2c54'
}

# Fuentes recomendadas
BEATPASS_FONTS = {
    'title': ('Segoe UI', 24, 'bold'),
    'subtitle': ('Segoe UI', 18, 'bold'),
    'heading': ('Segoe UI', 14, 'bold'),
    'body': ('Segoe UI', 11),
    'small': ('Segoe UI', 9),
    'button': ('Segoe UI', 12, 'bold')
}
