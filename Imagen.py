import pygame
from info import *

class mimagen:
    
    def __init__(self, nombre, direccion, x, y):
        pygame.init()
        self.nombre=nombre
        self.cord_x = x
        self.cord_y = y
        self.direccion = direccion
        self.image = pygame.image.load(self.direccion)
        self.image = pygame.transform.scale(self.image, (100,100))
        
    def get_cord_x(self):
        return self.cord_x
    
    def get_cord_y(self):
        return self.cord_y
    
    def get_direccion(self):
        return self.direccion
    
    def get_image(self):
        return self.image
    
    def get_name(self):
        return self.nombre
    
    def set_cord_x(self, valor):
        self.cord_x = valor
    def set_cord_y(self, valor):
        self.cord_y = valor