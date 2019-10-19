import pygame
from sys import exit
from bullet import Bullet
from alien import Alien
from time import sleep
def check_events(screen, bj_settings, ship, bullets,status,play_button,aliens,sc):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            down_event(screen, bj_settings, ship, event, bullets)
        elif event.type == pygame.KEYUP:
            up_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
         mouse_x, mouse_y = pygame.mouse.get_pos()
         check_play_button(bj_settings, screen, status, play_button, ship, aliens,
                           bullets, mouse_x, mouse_y,sc)
# def check_play_button(stats, play_button, mouse_x, mouse_y):
#     """ 在玩家单击 Play 按钮时开始新游戏 """
#     if play_button.rect.collidepoint(mouse_x, mouse_y):
#         stats.game_active = True
def check_play_button(bj_settings, screen, status, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y,sc):
    """ 在玩家单击 Play 按钮时开始新游戏 """
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not status.game_active:
        #隐藏光标！！
        pygame.mouse.set_visible(False)
        bj_settings.initialize_dynamic_settings()
        # 重置游戏统计信息
        status.reset_game()
        status.game_active = True
        # 重置记分牌图像
        sc.prep_score()
        sc.prep_high_score()
        sc.prep_level()
        sc.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并让飞船居中
        create_aliens(screen,bj_settings,aliens,ship)
        ship.center_ship()
def down_event(screen,bj_settings,ship,event,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_Right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_Left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(screen, bj_settings, ship,bullets)
def fire_bullet(screen, bj_settings, ship,bullets):
    if len(bullets) < bj_settings.bullets_allow:
        new_bullet = Bullet(screen, bj_settings, ship)
        bullets.add(new_bullet)
def up_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_Right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_Left = False
def update_bullets(bullets,screen,bj_settings,aliens,ship,status,sc):
    for bul in bullets:
        bul.update_bullet()
        bul.draw_bullet()
    for bull in bullets.copy():
        if bull.rect.bottom <= 0:
            bullets.remove(bull)
    check_collisions(bullets, screen, bj_settings, aliens, ship,status,sc)
def check_collisions(bullets,screen,bj_settings,aliens,ship,status,sc):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            status.score += bj_settings.alien_points * len(aliens)
            sc.prep_score()
        check_high_score(status, sc)
    if len(aliens) == 0:
        # # 提高等级
        # status.level += 1
        # sc.prep_level()
        bullets.empty()
        bj_settings.increase_speed()
        create_aliens(screen,bj_settings,aliens,ship)
        ship.center_ship()
        sleep(1)
def check_high_score(stats, sb):
    """ 检查是否诞生了新的最高得分 """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
def update_aliens(status,aliens,bj_settings,ship,bullets,screen,sc):
    # """ 更新外星人群中所有外星人的位置 """
    check_alien_edge(aliens,bj_settings)
    for alien in aliens:
        alien.update_alien()
    if pygame.sprite.spritecollideany(ship,aliens):
        hit_ship(status,screen,bj_settings,aliens,ship,bullets,sc)
    check_alien_bottom(status,screen,bj_settings,aliens,ship,bullets,sc)
def check_alien_bottom(status,screen,bj_settings,aliens,ship,bullets,sc):
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            hit_ship(status,screen,bj_settings,aliens,ship,bullets,sc)
            break #最好有break 不会卡死？？？？？
def hit_ship(status,screen,bj_settings,aliens,ship,bullets,sc):
    if status.ship_left >= 0:
        # 更新记分牌
        sc.prep_ships()
        # 提高等级#              应该写到检查外人人数为0 那里，测试用c
        status.level += 1
        sc.prep_level()
        status.ship_left -= 1
        aliens.empty()
        bullets.empty()
        bj_settings.increase_speed()
        create_aliens(screen,bj_settings,aliens,ship)
        ship.center_ship()
        sleep(1)
    else:
        status.game_active = False
        pygame.mouse.set_visible(True)
################################################
# def create_aliens(screen,bj_settings,aliens,ship):
#    """ 创建外星人群 """
#    # 创建一个外星人，并计算一行可容纳多少个外星人
#    # 外星人间距为外星人宽度
#    alien = Alien(screen,bj_settings)
#    alien_width = alien.rect.width
#    available_space_x = bj_settings.screen_width - 2 * alien_width
#    num_col = int(available_space_x / (2 * alien_width))
#    num_row = 0
#    # 创建第一行外星人
#    for alien_number in range(num_col):
#    # 创建一个外星人并将其加入当前行
#    #    create_group(aliens, screen, bj_settings,alien_width, num_col, num_row)
#        alien = Alien( screen, bj_settings)
#        alien.x = alien_width + 2 * alien_width * alien_number
#        alien.rect.x = alien.x
#        aliens.add(alien)
# def create_group(aliens,screen,bj_settings,alien_width,num_col,num_row):
#     alien = Alien(screen,bj_settings)
#     # alien_width = alien.rect.width
#     alien.x = alien_width + 2*alien_width*num_col
#     alien.rect.x = alien.x  #不能直接用alien.rect.width操作？
#     aliens.add(alien)
#################################################################错误
# #创建外星人组,失败，全部重合成一个！！！！！  解决！！！！！！！！！！！！！！！1
def create_aliens(screen,bj_settings,aliens,ship):
    alien = Alien(screen,bj_settings)
    num_column = get_number(bj_settings,alien)
    num_rows = get_num_rows(bj_settings,alien,ship)
    for row in range(num_rows):
        for num in range(num_column):
            create_group(aliens, screen,bj_settings,num_column,num_rows,num,row)
def get_number(bj_settings,alien):
    numbers = int(bj_settings.screen_width / (alien.rect.width * 2))
    return numbers
def create_group(aliens,screen,bj_settings,num_col,num_row,num,row):
    alien = Alien(screen,bj_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien.rect.width + alien_width * 2 * num
    # alien.x = alien.rect.width + alien_width * 2 * num_col  #num_col是最大数值，
    # 乘后只会呈现最后那个外星人，因为alien_col必不会跟随循环改变
    alien.y = alien.rect.height + alien_height * 2 * row
    # alien.y = alien.rect.height + alien_width * 2 * num_row
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)
#在多行创建外星人
def get_num_rows(bj__settings,alien,ship):
    avaliable_y = bj__settings.screen_height - alien.rect.height*5 - ship.rect.height
    nums = int(avaliable_y / (2 * alien.rect.height))
    return nums
#########################################################错误
#检查外星人是否到边缘
def check_alien_edge(aliens,bj_settings):
    for alien in aliens:
        if alien.check_edge():
            check_direction(aliens,bj_settings)
            break
def check_direction(aliens,bj_settings):
    for alien in aliens:
        alien.rect.y += bj_settings.alien_drop_speed
    bj_settings.alien_direction *= -1
def update_screen(status,screen,bj_settings,ship,aliens,bullets,play_button,sc):
    #填充颜色
    screen.fill(bj_settings.bj_color)
    # if status.game_active:
    aliens.draw(screen)
    # 重绘所有子弹--同时出现     先填充屏幕再绘制子弹
    # print(bullets)
    update_bullets(bullets,screen,bj_settings,aliens,ship,status,sc)
    update_aliens(status,aliens,bj_settings,ship,bullets,screen,sc)
    # 设置船的位置
    ship.blitme()
    sc.show_score()
    if not status.game_active:
        play_button.draw_button()
    # 更新屏幕
    pygame.display.flip()
