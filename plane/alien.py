import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,screen,bj_settings):
        self.screen = screen
        self.bj_settings = bj_settings
        super().__init__()
        #加载外星人图片
        self.image = pygame.image.load('image/飞机2.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update_alien(self):
        self.rect.x += self.bj_settings.alien_speed * self.bj_settings.alien_direction
    def check_edge(self):
        if self.rect.right >= self.bj_settings.screen_width:
            return True
        elif self.rect.left < 0:
            return True