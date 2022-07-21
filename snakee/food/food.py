from random import randrange
from pygame import draw, Rect, Surface


class Food:
    def __init__(self, surf_w: int, surf_h: int, s_pos: list, color) -> None:
        self.pos = self.move(s_pos, surf_w, surf_h)
        self.__color = color

    def draw(self, surf: Surface) -> None:
        draw.rect(
            surf, self.__color, Rect(self.pos[0], self.pos[1], 10, 10)
        )

    def move(self, s_pos: list, max_w: int, max_h: int) -> list:
        pos = s_pos[0]

        while pos in s_pos:
            pos = [
                randrange(1, max_w // 10) * 10,
                randrange(1, max_h // 10) * 10,
            ]

        if hasattr(self, "pos"):
            self.pos = pos
        else:
            return pos
