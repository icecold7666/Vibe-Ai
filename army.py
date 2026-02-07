import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """表示单个左巴杨的类"""
    def __init__(self,ai_settings,screen):
        """初始化左巴杨并设置其起始位置"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image_original = pygame.image.load('images/army.bmp')
        self.image = pygame.transform.scale(self.image_original, (60, 80))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制左巴杨"""
        self.screen.blit(self.image, self.rect)

    #移动
    def update(self):
        """向右移动"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """如果左巴杨位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True



