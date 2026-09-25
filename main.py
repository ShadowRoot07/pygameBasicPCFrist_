"""
main.py - Punto de entrada principal y bucle de juego (Game Loop).
"""
import sys
import pygame
import config
from entities.player import Player
from levels.level_1 import Level1
from levels.level_2 import Level2
from ui.hud import HUD


def reiniciar_juego():
    """Inicializa un nuevo estado del jugador y carga el primer nivel."""
    jugador = Player(x=50, y=450)
    niveles = [Level1(jugador), Level2(jugador)]
    return jugador, niveles, 0  # 0 es el índice del primer nivel


def main():
    # 1. Inicialización de Pygame
    pygame.init()
    pantalla = pygame.display.set_mode((config.ANCHO_PANTALLA, config.ALTO_PANTALLA))
    pygame.display.set_caption(config.TITULO_JUEGO)
    reloj = pygame.time.Clock()

    # 2. Instanciación de componentes
    hud = HUD()
    jugador, niveles, indice_nivel_actual = reiniciar_juego()
    nivel_actual = niveles[indice_nivel_actual]

    # Estados de flujo de juego
    juego_terminado = False
    juego_completado = False

    # 3. Bucle Principal
    ejecutando = True
    while ejecutando:
        # --- Manejo de Eventos de Entrada ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            if evento.type == pygame.KEYDOWN:
                # Disparo con barra espaciadora o Tecla 'K'
                if (evento.key == pygame.K_SPACE or evento.key == pygame.K_k) and not juego_terminado and not juego_completado:
                    jugador.disparar(nivel_actual.proyectiles)

                # Salir con ESC
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False

                # Reiniciar juego si se perdió o ganó
                if evento.key == pygame.K_r and (juego_terminado or juego_completado):
                    jugador, niveles, indice_nivel_actual = reiniciar_juego()
                    nivel_actual = niveles[indice_nivel_actual]
                    juego_terminado = False
                    juego_completado = False

        # --- Lógica del Juego (Update) ---
        if not juego_terminado and not juego_completado:
            # Procesar movimiento continuo de teclado (A, W, S, D)
            teclas = pygame.key.get_pressed()
            jugador.procesar_eventos(teclas)

            # Actualizar entidades y colisiones dentro del nivel activo
            nivel_actual.actualizar()

            # Comprobar estado de vida del jugador (HP = 0)
            if jugador.hp <= 0:
                juego_terminado = True

            # Comprobar si se superó el nivel activo
            if nivel_actual.esta_completado():
                indice_nivel_actual += 1
                if indice_nivel_actual < len(niveles):
                    # Avanzar al siguiente nivel manteniendo la vida del jugador
                    hp_actual = jugador.hp
                    nivel_actual = niveles[indice_nivel_actual]
                    jugador.hp = hp_actual
                else:
                    # Se superaron todos los niveles disponibles
                    juego_completado = True

        # --- Renderizado (Draw) ---
        pantalla.fill(config.COLOR_FONDO)

        # Dibujar nivel y entidades
        nivel_actual.dibujar(pantalla)

        # Dibujar Interfaz de Usuario (Barra HP y Nivel)
        hud.update(pantalla, jugador, indice_nivel_actual + 1)

        # Renderizar pantallas de estado (Game Over / Victoria)
        if juego_terminado:
            hud.renderizar_pantalla_game_over(pantalla)
        elif juego_completado:
            hud.renderizar_pantalla_victoria(pantalla)

        # Actualizar fotograma
        pygame.display.flip()
        reloj.tick(config.FPS)

    # Finalización limpia
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()