class Settings:
    """Хранит все настройки игры"""

    def __init__(self):
        # Экран
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 191, 255)
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_heigth = 15
        self.bullet_color = (60, 60, 60)
