import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,screen,bj_settings,ship):
        self.screen = screen
        super().__init__()
        self.speed = bj_settings.bullet_speed
        self.color = bj_settings.bullet_color
        #创建一个矩形，并设置正确的位置
        self.rect = pygame.Rect(0,0,bj_settings.bullet_width,bj_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #将子弹的y坐标转化为float值
        self.y = float(self.rect.y)
    #更新子弹的位置
    def update_bullet(self):
        self.y -= self.speed
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
