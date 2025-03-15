import pygame
import pygame_menu

class KeyboardMover(pygame.sprite.Sprite):
    def __init__(self, vehicle, Key):
        self.vehicle = vehicle
        self.pressedKey = ord(Key)
        
    def processOneEvent(self):
        userKey =  pygame.key.get_pressed()
        if userKey[self.pressedKey]:
            self.vehicle.setPosition(self.vehicle.getX() + 1, self.vehicle.getY())
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):     #Check if the event is a "QUIT" event (e.g. user close the window)
                return False  
        return True