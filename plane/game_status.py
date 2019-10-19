class GameStatus():
    def __init__(self,bj_settiings):
        self.bj_settings =bj_settiings
        self.reset_game()
        self.game_active = False
        # 在任何情况下都不应重置最高得分
        self.high_score = 0
    def reset_game(self):
        self.ship_left = self.bj_settings.ship_limit
        #需重置
        self.score = 0
        self.level = 1

