import pygame
import time

from .pages.base.page import Page
from .pages.start import StartPage


class Graphics:

    window = [800, 600]  # Set up Window Size
    window_name = "MegaQuest"

    # Properties
    _page: int
    _current_page: Page

    def __init__(self):
        pygame.init()

        self._screen = pygame.display.set_mode(self.window)
        pygame.display.set_caption(self.window_name)

        self._current_page = StartPage(self._screen)

    def render(self):
        self._screen.fill((0, 0, 0))  # Clear screen

        self._current_page.build_content()

        pygame.display.flip()

    def track_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

