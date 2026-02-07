import pygame

class Man():
    """飞机"""
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像（确保images/ship.bmp路径正确）
        self.image_original = pygame.image.load('images/ship.bmp')

        self.image = pygame.transform.scale(self.image_original, (60, 80))#缩放

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船位于屏幕底部中央（原注释写的“中央”，实际是底部中央，更符合游戏习惯）
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.centery = self.screen_rect.centery

        #精度
        self.center = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0 :
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.centery = self.center_y


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
        self.center_y = self.screen_rect.bottom

