class Settings():#游戏设置
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (181,184,182)
        self.ship_speed_factor = 1.5
        #创建子弹
        self.bullet_speed_factor = 5
        self.bullet_width = 30
        self.bullet_hight = 15
        self.bullet_color=60,60,60
        self.bullets_allowed = 3
        #创建外星人
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 4
        #fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1


        #血量
        self.ships_limit=3
        #加快游戏速度
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        #初始化
        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 0.5
        self.fleet_direction = 1
        self.alien_points = 50

    #提升游戏
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.bullet_width += self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)




