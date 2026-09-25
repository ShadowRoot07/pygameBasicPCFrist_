"""
config.py - Constantes globales y parámetros de configuración del juego.
"""

# --- Configuración de Pantalla y Rendimiento ---
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
FPS = 60
TITULO_JUEGO = "Plataformas 2D - Juego de Pruebas"

# --- Paleta de Colores (RGB) ---
COLOR_FONDO = (30, 30, 35)           # Gris oscuro / Antracita
COLOR_PLATAFORMA = (100, 200, 100)    # Verde suave
COLOR_JUGADOR = (0, 191, 255)         # Azul celeste (Deep Sky Blue)
COLOR_PROYECTIL = (255, 220, 0)       # Amarillo
COLOR_ENEMIGO = (220, 50, 50)         # Rojo

# --- Parámetros de Física Global ---
GRAVEDAD = 0.8
VELOCIDAD_TERMINAL = 20.0

# --- Atributos del Jugador ---
JUGADOR_ANCHO = 40
JUGADOR_ALTO = 40
JUGADOR_VELOCIDAD = 6.0
JUGADOR_FUERZA_SALTO = -14.0
JUGADOR_HP_MAX = 20
JUGADOR_TIEMPO_INMUNIDAD_MS = 1000  # 1 segundo de inmunidad tras recibir daño

# --- Atributos de los Proyectiles ---
PROYECTIL_ANCHO = 12
PROYECTIL_ALTO = 6
PROYECTIL_VELOCIDAD = 12.0
PROYECTIL_COOLDOWN_MS = 250         # Cadencia de tiro (1 disparo cada 250ms)

# --- Atributos de los Enemigos ---
ENEMIGO_DANIO = 5                   # Daño infligido al jugador
ENEMIGO_ANCHO_BASE = 36
ENEMIGO_ALTO_BASE = 36
ENEMIGO_VELOCIDAD_BASE = 2.0