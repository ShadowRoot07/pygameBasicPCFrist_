"""
levels/level_1.py - Configuración del Nivel 1 (Introducción con enemigos patrulleros).
"""
import pygame
import config
from levels.level_base import Level
from entities.enemy import PatrolEnemy


class Level1(Level):
    def __init__(self, jugador):
        super().__init__(jugador)

        # Posición inicial del jugador para este nivel
        self.jugador.rect.x = 50
        self.jugador.rect.y = 450

        # Disposición de Plataformas (x, y, ancho, alto)
        self.plataformas = [
            pygame.Rect(0, 550, config.ANCHO_PANTALLA, 50),     # Suelo principal
            pygame.Rect(150, 420, 200, 20),                    # Plataforma izquierda
            pygame.Rect(450, 320, 250, 20),                    # Plataforma derecha
        ]

        # Spawns de Enemigos
        self.enemigos.add(PatrolEnemy(200, 380, velocidad=2.0))
        self.enemigos.add(PatrolEnemy(500, 280, velocidad=2.5))
        self.enemigos.add(PatrolEnemy(600, 500, velocidad=1.8))