"""
entities/enemy.py - Clases para los enemigos rojos (Clase base y comportamientos).
"""
import pygame
import config


class Enemy(pygame.sprite.Sprite):
    """Clase base abstracta/general para todos los enemigos rojos."""

    def __init__(self, x: int, y: int, hp: int = 10, danio: int = config.ENEMIGO_DANIO):
        super().__init__()

        # Apariencia base (Cuadro Rojo)
        self.image = pygame.Surface((config.ENEMIGO_ANCHO_BASE, config.ENEMIGO_ALTO_BASE))
        self.image.fill(config.COLOR_ENEMIGO)
        self.rect = self.image.get_rect(topleft=(x, y))

        # Atributos de estado
        self.hp = hp
        self.danio = danio
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.en_suelo = False

    def recibir_danio(self, cantidad: int):
        """Disminuye los puntos de vida del enemigo y lo destruye si llega a 0."""
        self.hp -= cantidad
        if self.hp <= 0:
            self.kill()

    def aplicar_fisicas(self, plataformas):
        """Maneja la gravedad y colisiones de los enemigos con las plataformas."""
        # Aplicar Gravedad
        self.vel_y += config.GRAVEDAD
        if self.vel_y > config.VELOCIDAD_TERMINAL:
            self.vel_y = config.VELOCIDAD_TERMINAL

        # Movimiento Horizontal y Colisiones (Rebote en paredes)
        self.rect.x += self.vel_x
        for plat in plataformas:
            if self.rect.colliderect(plat):
                if self.vel_x > 0:
                    self.rect.right = plat.left
                    self.vel_x *= -1  # Invertir dirección
                elif self.vel_x < 0:
                    self.rect.left = plat.right
                    self.vel_x *= -1  # Invertir dirección

        # Mantener dentro de los límites de la pantalla
        if self.rect.left <= 0:
            self.rect.left = 0
            self.vel_x *= -1
        elif self.rect.right >= config.ANCHO_PANTALLA:
            self.rect.right = config.ANCHO_PANTALLA
            self.vel_x *= -1

        # Movimiento Vertical y Colisiones
        self.rect.y += self.vel_y
        self.en_suelo = False

        for plat in plataformas:
            if self.rect.colliderect(plat):
                if self.vel_y > 0:  # Cayendo
                    self.rect.bottom = plat.top
                    self.vel_y = 0.0
                    self.en_suelo = True
                elif self.vel_y < 0:  # Subiendo
                    self.rect.top = plat.bottom
                    self.vel_y = 0.0


class PatrolEnemy(Enemy):
    """Enemigo terrestre que patrulla en una dirección a velocidad constante."""

    def __init__(self, x: int, y: int, velocidad: float = config.ENEMIGO_VELOCIDAD_BASE):
        super().__init__(x, y, hp=10)
        self.vel_x = velocidad

    def update(self, plataformas):
        self.aplicar_fisicas(plataformas)


class JumperEnemy(Enemy):
    """Enemigo que salta a intervalos de tiempo regulares."""

    def __init__(self, x: int, y: int, intervalo_salto_ms: int = 2000):
        super().__init__(x, y, hp=15)
        self.intervalo_salto = intervalo_salto_ms
        self.ultimo_salto = pygame.time.get_ticks()
        self.vel_x = config.ENEMIGO_VELOCIDAD_BASE * 0.5  # Se mueve más lento horizontalmente

    def update(self, plataformas):
        tiempo_actual = pygame.time.get_ticks()

        # Saltar si ha transcurrido el tiempo y está apoyado en una superficie
        if self.en_suelo and (tiempo_actual - self.ultimo_salto >= self.intervalo_salto):
            self.vel_y = -10.0
            self.ultimo_salto = tiempo_actual

        self.aplicar_fisicas(plataformas)