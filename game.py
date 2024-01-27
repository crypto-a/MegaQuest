from graphics.graphics import Graphics
import time


class Game(object):
    """
    This class is incharge of the main game processes.
    """
    def __init__(self):
        self._graphics = Graphics()

    def start(self):
        """
        This method is the main game loop
        """
        running = True
        while running:

            self._graphics.render()
            self._graphics.track_events()

            time.sleep(0.05)  # Used to control refresh rate



