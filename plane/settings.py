class Settings():
    #存储配置信息
    def __init__(self):
        #屏幕设置参数
        self.screen_width = 1250
        self.screen_height = 700
        self.bj_color = (200,200,200)
        self.ship_speed = 1
        self.ship_limit = 3
        self.bullet_speed = 0.5
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = 100,100,100
        self.bullets_allow = 5
        self.alien_speed = 1
        self.alien_drop_speed = 20
        self.alien_direction = 1
        self.speed_increase = 1.1
        self.initialize_dynamic_settings()
        self.score_scale = 1.5
    def initialize_dynamic_settings(self):
        """ 初始化随游戏进行而变化的设置 """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction 为 1 表示向右；为 -1 表示向左
        self.fleet_direction = 1
        #击杀每个外星人的得分数，重置游戏后恢复
        self.alien_points = 50

    def increase_speed(self):
        """ 提高速度设置 """
        self.ship_speed *= self.speed_increase
        self.bullet_speed *= self.speed_increase
        self.alien_speed *= self.speed_increase
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)