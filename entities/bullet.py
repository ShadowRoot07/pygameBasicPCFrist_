"""
entities/bullet.py - Proyectiles amarillos disparados por el jugador.
"""
import pygame
import config


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, direccion: int):
        """
        :param x: Posición inicial X
        :param y: Posición inicial Y
        :param direccion: 1 para la derecha, -1 para la izquierda
        """
        super().__init__()

        # Crear la superficie del proyectil (amarillo)
        self.image = pygame.Surface((config.PROYECTIL_ANCHO, config.PROYECTIL_ALTO))
        self.image.fill(config.COLOR_PROYECTIL)

        self.rect = self.image.get_rect()
        # Ajustar la posición inicial para que el disparo salga del centro del jugador
        if direccion >= 0:
            self.rect.left = x
        else:
            self.rect.right = x
            
        self.rect.centery = y

        self.direccion = direccion
        self.velocidad = config.PROYECTIL_VELOCIDAD

    def update(self):
        """Mueve el proyectil y lo destruye si sale de los límites de la pantalla."""
        self.rect.x += self.velocidad * self.direccion

        # Eliminar del grupo de sprites si sale de la pantalla
        if self.rect.right < 0 or self.rect.left > config.ANCHO_PANTALLA:
            self.kill()