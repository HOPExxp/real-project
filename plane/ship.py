import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    #设置飞船的基本信息,先得到主屏幕的信息--screen
    def __init__(self,bj_settings,screen):
        super(Ship, self).__init__()
        '''初始化飞船并设置其初始位置'''
        #接收飞船移动速度值  并将飞船的centerx值转化为float值
        self.bj_settings = bj_settings
        #加载主屏幕并获取其外接矩形  参考位置
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        #加载飞船图像并获取其外接矩形   实际要放的图形
        self.image = pygame.image.load('image/飞机2.png')
        self.rect = self.image.get_rect()
        #----------
        #设置飞船的位置信息--主屏幕的中间及底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_Right = False
        self.moving_Left = False
    def continue_update(self):
        if self.moving_Right and self.rect.right < self.screen_rect.right:
            self.center += self.bj_settings.ship_speed
        if self.moving_Left and self.rect.left > 0:
            self.center -= self.bj_settings.ship_speed
        #再次将self.center值传给self.rect值
        self.rect.centerx = self.center
    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        self.center = self.screen_rect.centerx