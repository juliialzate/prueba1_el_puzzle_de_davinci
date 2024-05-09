import pygame
from Imagen import mimagen
from pygame.locals import *
from info import *

class puzzle:
    
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("XD") 
    screen.fill((255, 255, 255))
        
    def __init__(self):
        self.imagen1 = mimagen("imagen1","imagenes\monalisa1.png",0,0)
        self.imagen2 = mimagen("imagen2","imagenes\monalisa2.png",0,1)
        self.imagen3 = mimagen("imagen3","imagenes\monalisa3.png",0,2)
        self.imagen4 = mimagen("imagen4","imagenes\monalisa4.png",1,0)
        self.imagen5 = mimagen("imagen5","imagenes\monalisa5.png",1,1)
        self.imagen6 = mimagen("imagen6","imagenes\monalisa6.png",1,2)
        self.imagen7 = mimagen("imagen7","imagenes\monalisa7.png",2,0)
        self.imagen8 = mimagen("imagen8","imagenes\monalisa8.png",2,1)
        self.imagen9 = mimagen("imagen9","imagenes\monalisa9.png",2,2)
        
        self.lista_imagenes = [self.imagen1,self.imagen2,self.imagen3,self.imagen4,self.imagen5,self.imagen6,self.imagen8,self.imagen9]
    
    def encontrar_imagen(self, x, y):
        for imagen in self.lista_imagenes:
            if imagen.get_cord_x() == x and imagen.get_cord_y() == y:
                return imagen
        return None
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.imagen9.get_cord_y() != 2:
                        # Movemos la imagen a la derecha (si no está en el borde derecho)
                        self.imagen9.set_cord_y((self.imagen9.get_cord_y() + 1)% 3) 
                        print(self.imagen9.get_cord_x(),self.imagen9.get_cord_y())
                    elif event.key == pygame.K_LEFT and self.imagen9.get_cord_y() != 0:
                        # Movemos la imagen a la izquierda (si no está en el borde izquierdo)
                        self.imagen9.set_cord_y((self.imagen9.get_cord_y() -1)% 3)
                        self.imagen8.set_cord_y((self.imagen8.get_cord_y() +1)% 3)
                        print(self.imagen9.get_cord_x(),self.imagen9.get_cord_y())
            
                    elif event.key == pygame.K_DOWN and self.imagen9.get_cord_x() != 2:
                        # Movemos la imagen hacia abajo (si no está en el borde inferior)
                        self.imagen9.set_cord_x((self.imagen9.get_cord_x() + 1) % 3)
                        print(self.imagen9.get_cord_x(),self.imagen9.get_cord_y())
                    elif event.key == pygame.K_UP and self.imagen9.get_cord_x() != 0:
                        # Movemos la imagen hacia arriba (si no está en el borde superior)
                        self.imagen9.set_cord_x((self.imagen9.get_cord_x() - 1) % 3)
                        print(self.imagen9.get_cord_x(),self.imagen9.get_cord_y())

            self.pintar_imagenes()
            pygame.display.flip()

        
    def pintar_imagenes(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, (255, 0, 0), (i * 100, 0), (i * 100, 300), 2)
        for i in range(1, 3):
            pygame.draw.line(self.screen, (255, 0, 0), (0, i * 100), (300, i * 100), 2)

        celda = 100
        self.screen.blit(self.imagen1.get_image(), (self.imagen1.get_cord_y() * celda, self.imagen1.get_cord_x() * celda))
        self.screen.blit(self.imagen2.get_image(), (self.imagen2.get_cord_y() * celda, self.imagen2.get_cord_x() * celda))
        self.screen.blit(self.imagen3.get_image(), (self.imagen3.get_cord_y() * celda, self.imagen3.get_cord_x() * celda))
        self.screen.blit(self.imagen4.get_image(), (self.imagen4.get_cord_y() * celda, self.imagen4.get_cord_x() * celda))
        self.screen.blit(self.imagen5.get_image(), (self.imagen5.get_cord_y() * celda, self.imagen5.get_cord_x() * celda))
        self.screen.blit(self.imagen6.get_image(), (self.imagen6.get_cord_y() * celda, self.imagen6.get_cord_x() * celda))
        self.screen.blit(self.imagen7.get_image(), (self.imagen7.get_cord_y() * celda, self.imagen7.get_cord_x() * celda))
        self.screen.blit(self.imagen8.get_image(), (self.imagen8.get_cord_y() * celda, self.imagen8.get_cord_x() * celda))
        self.screen.blit(self.imagen9.get_image(), (self.imagen9.get_cord_y() * celda, self.imagen9.get_cord_x() * celda))