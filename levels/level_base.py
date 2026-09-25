"""
levels/level_base.py - Clase base encargada de la lógica, físicas y colisiones de los niveles.
"""
import pygame
import config


class Level:
    def __init__(self, jugador):
        self.jugador = jugador
        self.plataformas = []
        self.enemigos = pygame.sprite.Group()
        self.proyectiles = pygame.sprite.Group()
        self.meta_rect = None  # Zona para avanzar de nivel (opcional)

    def actualizar(self):
        """Actualiza la posición y físicas de todas las entidades del nivel."""
        # 1. Actualizar Proyectiles
        self.proyectiles.update()

        # 2. Actualizar Enemigos
        self.enemigos.update(self.plataformas)

        # 3. Actualizar Jugador
        self.jugador.update(self.plataformas)

        # 4. Procesar Colisiones
        self.gestionar_colisiones()

    def gestionar_colisiones(self):
        """Maneja las colisiones entre Proyectiles-Enemigos y Enemigos-Jugador."""
        # Colisión: Proyectil amarillo colisiona con Enemigo rojo
        # pygame.sprite.groupcollide(grupo1, grupo2, dokill1, dokill2)
        impactos = pygame.sprite.groupcollide(self.proyectiles, self.enemigos, True, False)
        for proyectil, lista_enemigos in impactos.items():
            for enemigo in lista_enemigos:
                enemigo.recibir_danio(10)  # Cada disparo inflige 10 de daño al enemigo

        # Colisión: Enemigo rojo colisiona con Jugador azul
        enemigos_impactando = pygame.sprite.spritecollide(self.jugador, self.enemigos, False)
        for enemigo in enemigos_impactando:
            self.jugador.recibir_danio(enemigo.danio)  # Inflige 5 de daño (config.ENEMIGO_DANIO)

    def dibujar(self, superficie: pygame.Surface):
        """Dibuja todos los elementos del nivel en la pantalla."""
        # Dibujar Plataformas
        for plat in self.plataformas:
            pygame.draw.rect(superficie, config.COLOR_PLATAFORMA, plat)

        # Dibujar Proyectiles
        self.proyectiles.draw(superficie)

        # Dibujar Enemigos
        self.enemigos.draw(superficie)

        # Dibujar Jugador (efecto parpadeo si es inmune tras recibir daño)
        if not self.jugador.es_inmune or (pygame.time.get_ticks() // 100) % 2 == 0:
            superficie.blit(self.jugador.image, self.jugador.rect)

    def esta_completado(self) -> bool:
        """Determina si el nivel ha sido superado (todos los enemigos derrotados)."""
        return len(self.enemigos) == 0