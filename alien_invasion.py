import sys
import pygame

from settings import Settings


class AlienInvasion:
    """Класс ресурсов и управления игрой"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Цвет фона
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        # Запуск основного цикла игры
        while True:
            # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
            # При каждом проходе цикла перерисовывается экран
            self.screen.fill(self.settings.bg_color)
            # Отображение последнеего прорисованного экрана
            pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
