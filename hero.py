from logging import root
from tkinter import Label

import pygame
from settings import Settings


class Hero:
    """Класс для управления монстром"""

    def __init__(self, ai_game):
        """Инициализация монстра и его начального положения"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        """Загружает изображение монстра и получает прямоугольник"""
        self.image = pygame.image.load('images/monstr.bmp')
        self.rect = self.image.get_rect()
        """Все монстры появляются в центре"""
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Рисует монстра в теущей позиции"""
        self.screen.blit(self.image, self.rect)
