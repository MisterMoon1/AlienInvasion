import os
import sys
import pygame

from settings import Settings
from ship import Ship
from hero import Hero
from bullet import Bullet


class AlienInvasion:
    """Класс ресурсов и управления игрой"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.hero = Hero(self)
        self.bullets = pygame.sprite.Group
        # Цвет фона
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        # Запуск основного цикла игры
        while True:
            # Отслеживание событий клавиатуры и мыши
            self._chek_events()
            self.ship.update()
            self.bullets.update()
            # При каждом проходе цикла перерисовывается экран
            self._update_screen()

    def _chek_events(self):
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
            elif event == pygame.K_q:
                sys.exit()
            # Перемещение вправо и влево
            elif event.type == pygame.KEYDOWN:
                self.check_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_events_keyup(event)

    def check_events_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def check_events_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
        # Прорисовка экрана
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.hero.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.update()
        # Отображение последнеего прорисованного экрана
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
