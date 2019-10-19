import pygame
from sys import exit
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group
from game_status import GameStatus
from button import Button
from score import Scoreboard
from alien import Alien
#游戏三次结束后如果不操作还会更新外星人！！！,也可以继续得分（一轮）
#重新开始游戏速度没有恢复到初始值  ！！！
#等级出现四 ，和可继续得分一轮有关    只有全部消灭外星人时才增加等级，但是相撞、到底部也加，而且速度一直加
#外星人的计数也有问题3-3-2-1-0

#最高分也会重置  #不会重置
#分数也没有重置#  会重置
#主函数，运行整个游戏
def main():
    #----------
    #init初始化所有模块，并检查
    pygame.init()
    #----------
    #从配置文件中拿参数
    bj_settings = Settings()
    #----------
    #设置屏幕大小,flags:扩展选项
    screen = pygame.display.set_mode((bj_settings.screen_width,bj_settings.screen_height),pygame.RESIZABLE,32)
    #设置游戏主题
    pygame.display.set_caption('Alien Invasion')
    #设置窗口图标
    icon = pygame.image.load('image/ship.bmp')
    pygame.display.set_icon(icon)
    status = GameStatus(bj_settings)
    sc = Scoreboard( bj_settings, screen, status)
    #-----------
    #创建一个船的对象，调用船的位置方法
    ship = Ship(bj_settings,screen)
    # alien = Alien(screen)
    #-----------
    bullets = Group()
    aliens = Group()
    game_functions.create_aliens(screen,bj_settings,aliens,ship)
    play_button = Button(bj_settings, screen,'PLAY' )
    while True:
        game_functions.check_events(screen, bj_settings, ship, bullets,status,play_button,aliens,sc)
        game_functions.update_screen(status, screen, bj_settings, ship, aliens, bullets, play_button,sc)
        if status.game_active:
            ship.continue_update()
            # bullets.update()
            # game_functions.update_bullets(bullets)
            game_functions.update_screen(status,screen,bj_settings,ship,aliens,bullets,play_button,sc)
        # game_functions.update_bullets(bullets)
        # #对事件进行监控
        # for event in pygame.event.get():
        #     #设置背景颜色,screen接收到一个Surface对象
        #     screen.fill(bj_settings.bj_color)
        #     #设置船的位置
        #     ship.blitme()
        #     #pygame.quit()和pygame.QUIT的区别？
        #     if event.type == pygame.QUIT:
        #         #系统退出
        #         exit()
        # #更新屏幕
        # pygame.display.flip()
main()