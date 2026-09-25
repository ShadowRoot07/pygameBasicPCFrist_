"""
entities/player.py - Clase Jugador (cuadro azul, mecánicas de movimiento, HP y disparo).
"""
import pygame
import config
from entities.bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        # Apariencia (Cuadro Azul Celeste)
        self.image = pygame.Surface((config.JUGADOR_ANCHO, config.JUGADOR_ALTO))
        self.image.fill(config.COLOR_JUGADOR)
        self.rect = self.image.get_rect(topleft=(x, y))

        # Atributos de Estado
        self.hp = config.JUGADOR_HP_MAX
        self.en_suelo = False
        self.mira_derecha = True  # Determina la dirección del disparo

        # Vector de Velocidad
        self.vel_x = 0.0
        self.vel_y = 0.0

        # Temporizadores (Cooldowns)
        self.ultimo_disparo = 0
        self.ultima_inmunidad = 0
        self.es_inmune = False

    def procesar_eventos(self, teclas):
        """Procesa la entrada del teclado para movimiento y acciones."""
        self.vel_x = 0.0

        # Movimiento horizontal (A/D)
        if teclas[pygame.K_a]:
            self.vel_x = -config.JUGADOR_VELOCIDAD
            self.mira_derecha = False
        if teclas[pygame.K_d]:
            self.vel_x = config.JUGADOR_VELOCIDAD
            self.mira_derecha = True

        # Salto (W)
        if teclas[pygame.K_w] and self.en_suelo:
            self.vel_y = config.JUGADOR_FUERZA_SALTO
            self.en_suelo = False

        # Caída rápida (S)
        if teclas[pygame.K_s] and not self.en_suelo:
            self.vel_y += 1.5

    def disparar(self, grupo_proyectiles: pygame.sprite.Group):
        """Genera un nuevo proyectil amarillo si ha transcurrido el tiempo de cooldown."""
        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual - self.ultimo_disparo >= config.PROYECTIL_COOLDOWN_MS:
            self.ultimo_disparo = tiempo_actual
            direccion = 1 if self.mira_derecha else -1
            pos_x = self.rect.right if self.mira_derecha else self.rect.left

            bullet = Bullet(pos_x, self.rect.centery, direccion)
            grupo_proyectiles.add(bullet)

    def recibir_danio(self, cantidad: int):
        """Aplica daño al jugador y activa inmunidad temporal."""
        if not self.es_inmune:
            self.hp -= cantidad
            if self.hp < 0:
                self.hp = 0
            self.es_inmune = True
            self.ultima_inmunidad = pygame.time.get_ticks()

    def aplicar_fisicas(self, plataformas):
        """Maneja la gravedad, el movimiento y las colisiones con las plataformas."""
        # 1. Aplicar Gravedad
        self.vel_y += config.GRAVEDAD
        if self.vel_y > config.VELOCIDAD_TERMINAL:
            self.vel_y = config.VELOCIDAD_TERMINAL

        # 2. Movimiento Horizontal y Colisión
        self.rect.x += self.vel_x
        for plat in plataformas:
            if self.rect.colliderect(plat):
                if self.vel_x > 0:
                    self.rect.right = plat.left
                elif self.vel_x < 0:
                    self.rect.left = plat.right

        # Límites de pantalla laterales
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > config.ANCHO_PANTALLA:
            self.rect.right = config.ANCHO_PANTALLA

        # 3. Movimiento Vertical y Colisión
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

    def update(self, plataformas):
        """Actualiza físicas y temporizadores de inmunidad."""
        tiempo_actual = pygame.time.get_ticks()

        # Desactivar inmunidad tras 1 segundo
        if self.es_inmune and (tiempo_actual - self.ultima_inmunidad >= config.JUGADOR_TIEMPO_INMUNIDAD_MS):
            self.es_inmune = False

        self.aplicar_fisicas(plataformas)