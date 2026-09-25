# Juego bien fregoOOOOONN en la PC

El primer juego que hice en mi computadora a base de mi determinacion y con el poder de mis huevos, **¡¡¡HAY SIIIIIIIIIIIIIIII!!!**

Un juego de plataformas estilo Arcade en 2D desarrollado en Python con Pygame. Incluye mecánicas de movimiento, disparos, enemigos, barra de estado (HUD) y transición entre múltiples niveles.

---

## 🚀 Características

- **Sistemas de Movimiento y Combate:** Movimiento fluido con salto, caída rápida y sistema de proyectiles.
- **Niveles Progresivos:** Transición automática al derrotar a todos los enemigos de un nivel.
- **Interfaz de Usuario (HUD):** Visualización en tiempo real del HP del jugador y el nivel actual.
- **Flujo Completo de Partida:** Pantallas dinámicas para *Game Over* y *Victoria* con opción de reinicio instantáneo.

---

## 🛠️ Requisitos Previos

- Python 3.10 o superior
- Terminal / PowerShell

---

## 📥 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
   cd TU_REPOSITORIO
   ```

2. **Crear y activar el entorno virtual:**

* **En Windows (PowerShell):**

    ```bash
    python -m venv venv
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    .\venv\Scripts\Activate.ps1
    ```

* **En Linux / macOS:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instalar dependencias:**

    ```bash
    pip install pygame-ce
    ```

## 📁 Estructura del Proyecto

    ```bash
    ├── config.py          # Ajustes globales (pantalla, colores, FPS)
    ├── main.py            # Punto de entrada y Game Loop principal
    ├── entities/          # Módulos del jugador, enemigos y proyectiles
    ├── levels/            # Lógica y composición de los niveles
    └── ui/                # Componentes de la interfaz visual (HUD)
    ```

## ⚙️ Ejecución


**Asegúrate de tener el entorno virtual activado y ejecuta:**

    ```bash
    python main.py
    ```