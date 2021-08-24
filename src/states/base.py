import pygame as pg
import pygame.font as pgfont
from pygame import event as pgevent

class BaseState(object):
    def __init__(self) -> None:
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.font: pgfont.Font = pg.font.Font(None, 24)

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event: pgevent.Event):
        if event.type == pg.QUIT:
            self.quit = True

    def update(self, dt):
        pass

    def draw(self, surface):
        pass
