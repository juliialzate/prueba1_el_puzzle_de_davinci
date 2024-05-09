import pygame
import sys

# Definimos algunos colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Tamaño de la pantalla
WIDTH, HEIGHT = 300, 300

# Tamaño de la cuadrícula
GRID_SIZE = WIDTH // 3

# Inicializamos Pygame
pygame.init()

# Creamos la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matriz 3x3")

# Cargamos la imagen
image = pygame.image.load("codigo_prueba_davinci-main\imagenes\monalisa2.png")
image = pygame.transform.scale(image, (GRID_SIZE, GRID_SIZE))  # Ajustamos al tamaño de una celda

image2 = pygame.image.load("codigo_prueba_davinci-main\imagenes\monalisa1.png")
image2 = pygame.transform.scale(image2, (GRID_SIZE, GRID_SIZE))  # Ajustamos al tamaño de una celda


# Posición inicial de la imagen
image_row, image_col = 0, 0
image2_row, image2_col = 0, 1

# Función para dibujar la cuadrícula y la imagen en la posición (image_row, image_col)
def draw_grid():
    # Dibujamos las líneas verticales
    for i in range(1, 3):
        pygame.draw.line(screen, RED, (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT), 2)
    # Dibujamos las líneas horizontales
    for i in range(1, 3):
        pygame.draw.line(screen, RED, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE), 2)

    # Dibujamos la imagen en la posición (image_row, image_col)
    screen.blit(image, (image_col * GRID_SIZE, image_row * GRID_SIZE))
    screen.blit(image2, (image2_col * GRID_SIZE, image2_row * GRID_SIZE))
# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and image_col != 2:
                # Movemos la imagen a la derecha (si no está en el borde derecho)
                image_col = (image_col + 1) % 3
                image2_col = (image2_col - 1) % 3
                print(image_row,image_col)
            elif event.key == pygame.K_LEFT and image_col != 0:
                # Movemos la imagen a la izquierda (si no está en el borde izquierdo)
                image_col = (image_col - 1) % 3
                print(image_row,image_col)
            elif event.key == pygame.K_DOWN and image_row != 2:
                # Movemos la imagen hacia abajo (si no está en el borde inferior)
                image_row = (image_row + 1) % 3
                print(image_row,image_col)
            elif event.key == pygame.K_UP and image_row != 0:
                # Movemos la imagen hacia arriba (si no está en el borde superior)
                image_row = (image_row - 1) % 3
                print(image_row,image_col)

    # Rellenamos la pantalla con color blanco
    screen.fill(WHITE)
    
    # Dibujamos la cuadrícula y la imagen
    draw_grid()

    # Actualizamos la pantalla
    pygame.display.flip()
