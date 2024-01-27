import pygame
from graphics.pages.base.page import Page
from numba import njit, jit


class StartPage(Page):

    _progress: float
    _screen: pygame.Surface

    def __init__(self, screen: pygame.Surface):

        self._progress = 0.0
        self._screen = screen

    def build_content(self):
        # Simulating loading process
        if self._progress < 1.0:
            self._progress += 0.01

        # Dimensions for the loading bar
        bar_width, bar_height = 400, 50
        bar_x, bar_y = (self._screen.get_width() - bar_width) // 2, (self._screen.get_height() - bar_height) // 2

        # Draw the outline of the loading bar
        pygame.draw.rect(self._screen, (255, 255, 255), [bar_x, bar_y, bar_width, bar_height], 2)

        # Fill the loading bar according to the current progress
        fill_width = int(self._progress * bar_width)
        pygame.draw.rect(self._screen, (255, 255, 255), [bar_x, bar_y, fill_width, bar_height])

