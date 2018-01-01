import pygame
from pygame.locals import *

class Pygame:
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((450, 450))
        pygame.display.set_caption("Free MacGyver from the bowels of the enemy!")
        #Music of Macgyver
        pygame.mixer.music.load("Generique.mp3")
        pygame.mixer.music.play()

    def flip(self):
        pygame.display.flip()

    def load_image(self, image_path):
        return pygame.image.load(image_path).convert()

    def blit(self, image, position=(0, 0)):
        self.window.blit(image, position)

    def timer_tick(self, fps):
        pygame.time.Clock().tick(fps)

    def get_event(self):
        return pygame.event.get()

    def stop_music(self):
        pygame.mixer.music.stop()
