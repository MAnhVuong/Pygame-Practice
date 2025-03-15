import pygame
import pygame_menu
import KeyboardMover

class Map(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        
    def update(self, vehicleList):
        for item in vehicleList:
            self.screen.blit(item.getImage(), item.getPosition())
            pygame.display.flip() 