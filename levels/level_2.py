"""
levels/level_2.py - Configuración del Nivel 2 (Mayor dificultad con enemigos saltarines).
"""
import pygame
import config
from levels.level_base import Level
from entities.enemy import PatrolEnemy, JumperEnemy


class Level2(Level):
    def __init__(self, jugador):
        super().__init__(jugador)

        # Posición inicial del jugador
        self.jugador.rect.x = 50
        self.jugador.rect.y = 480

        # Disposición de Plataformas más escalonada
        self.plataformas = [
            pygame.Rect(0, 550, config.ANCHO_PANTALLA, 50),     # Suelo principal
            pygame.Rect(100, 430, 160, 20),                    # Escalón 1
            pygame.Rect(320, 330, 180, 20),                    # Escalón central
            pygame.Rect(550, 230, 200, 20),                    # Escalón elevado
            pygame.Rect(50, 180, 180, 20)                     # Plataforma superior izquierda
        ]

        # Combinación de enemigos patrulleros y saltarines
        self.enemigos.add(PatrolEnemy(120, 390, velocidad=3.0))
        self.enemigos.add(JumperEnemy(350, 280, intervalo_salto_ms=1800))
        self.enemigos.add(JumperEnemy(580, 180, intervalo_salto_ms=1500))
        self.enemigos.add(PatrolEnemy(400, 500, velocidad=2.2))