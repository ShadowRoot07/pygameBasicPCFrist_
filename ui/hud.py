"""
ui/hud.py - Módulo para la Interfaz de Usuario (Barra de HP, nivel, Game Over).
"""
import pygame
import config


class HUD:
    def __init__(self):
        # Fuente predeterminada de Pygame
        self.fuente_pequena = pygame.font.SysFont("arial", 18, bold=True)
        self.fuente_grande = pygame.font.SysFont("arial", 48, bold=True)

    def dibujar_barra_hp(self, superficie: pygame.Surface, hp_actual: int, hp_max: int):
        """Dibuja una barra de HP con texto en la esquina superior izquierda."""
        ancho_barra = 200
        alto_barra = 20
        x, y = 20, 20

        # Cálculo de proporción de vida
        porcentaje = max(0, hp_actual / hp_max)
        ancho_actual = int(ancho_barra * porcentaje)

        # Color dinámico de la barra según la vida restante
        if porcentaje > 0.5:
            color_hp = (50, 205, 50)    # Verde
        elif porcentaje > 0.25:
            color_hp = (255, 165, 0)   # Naranja
        else:
            color_hp = (220, 20, 60)    # Rojo

        # Fondo de la barra (Gris oscuro) y borde
        rect_fondo = pygame.Rect(x, y, ancho_barra, alto_barra)
        rect_hp = pygame.Rect(x, y, ancho_actual, alto_barra)

        pygame.draw.rect(superficie, (50, 50, 50), rect_fondo)
        pygame.draw.rect(superficie, color_hp, rect_hp)
        pygame.draw.rect(superficie, (255, 255, 255), rect_fondo, 2)  # Borde blanco

        # Texto numérico (ej. "HP: 15 / 20")
        texto_hp = self.fuente_pequena.render(f"HP: {hp_actual} / {hp_max}", True, (255, 255, 255))
        superficie.blit(texto_hp, (x + 10, y + 1))

    def dibujar_info_nivel(self, superficie: pygame.Surface, numero_nivel: int):
        """Muestra el número de nivel actual en la esquina superior derecha."""
        texto_nivel = self.fuente_pequena.render(f"NIVEL {numero_nivel}", True, (255, 255, 255))
        rect_texto = texto_nivel.get_rect(topright=(config.ANCHO_PANTALLA - 20, 20))
        superficie.blit(texto_nivel, rect_texto)

    def renderizar_pantalla_game_over(self, superficie: pygame.Surface):
        """Renderiza una superposición semi-transparente de Game Over."""
        overlay = pygame.Surface((config.ANCHO_PANTALLA, config.ALTO_PANTALLA), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))  # Negro con transparencia
        superficie.blit(overlay, (0, 0))

        texto = self.fuente_grande.render("GAME OVER", True, (220, 50, 50))
        rect = texto.get_rect(center=(config.ANCHO_PANTALLA // 2, config.ALTO_PANTALLA // 2 - 20))
        superficie.blit(texto, rect)

        subtexto = self.fuente_pequena.render("Presiona 'R' para reiniciar o 'ESC' para salir", True, (255, 255, 255))
        sub_rect = subtexto.get_rect(center=(config.ANCHO_PANTALLA // 2, config.ALTO_PANTALLA // 2 + 30))
        superficie.blit(subtexto, sub_rect)

    def renderizar_pantalla_victoria(self, superficie: pygame.Surface):
        """Renderiza la pantalla al completar todos los niveles."""
        overlay = pygame.Surface((config.ANCHO_PANTALLA, config.ALTO_PANTALLA), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        superficie.blit(overlay, (0, 0))

        texto = self.fuente_grande.render("¡VICTORIA!", True, (255, 215, 0))
        rect = texto.get_rect(center=(config.ANCHO_PANTALLA // 2, config.ALTO_PANTALLA // 2 - 20))
        superficie.blit(texto, rect)

        subtexto = self.fuente_pequena.render("Has derrotado a todos los enemigos. Presiona 'R' para volver a jugar", True, (255, 255, 255))
        sub_rect = subtexto.get_rect(center=(config.ANCHO_PANTALLA // 2, config.ALTO_PANTALLA // 2 + 30))
        superficie.blit(subtexto, sub_rect)

    def update(self, superficie: pygame.Surface, jugador, numero_nivel: int):
        """Método principal para actualizar todo el HUD en el frame actual."""
        self.dibujar_barra_hp(superficie, jugador.hp, config.JUGADOR_HP_MAX)
        self.dibujar_info_nivel(superficie, numero_nivel)