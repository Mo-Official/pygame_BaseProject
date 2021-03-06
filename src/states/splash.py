import pygame as pg
from pygame import event as pgevent
from .base import BaseState

class Splash(BaseState):
    def __init__(self) -> None:
        super(Splash, self).__init__()
        self.title = self.font.render("Incomplete Game", True, pg.Color("blue"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "MENU"
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 5000:
            self.done = True

    def get_event(self, event: pgevent.Event):
        if event.type == pg.KEYUP:
            self.done = True


    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
        
