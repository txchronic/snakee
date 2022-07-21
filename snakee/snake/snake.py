from random import choice
from pygame import draw, Rect, Surface


class Snake:
    def __init__(self, surf_w: int, surf_h: int, colors: list) -> None:
        self.turn = "right"
        self.__colors = [choice(colors) for _ in range(3)]
        self.pos = self.move(surf_w, surf_h)

    def draw(self, surf: Surface) -> None:
        for i, pos in enumerate(self.pos):
            draw.rect(surf, self.__colors[i], Rect(pos[0], pos[1], 10, 10))

    def move(self, max_w: int, max_h: int) -> None | list:
        if hasattr(self, "pos"):
            if self.turn == "right":
                self.pos = [
                    [self.pos[0][0] + 10, self.pos[0][1]],
                    *self.pos[:-1],
                ]
            elif self.turn == "left":
                self.pos = [
                    [self.pos[0][0] - 10, self.pos[0][1]],
                    *self.pos[:-1],
                ]
            elif self.turn == "up":
                self.pos = [
                    [self.pos[0][0], self.pos[0][1] - 10],
                    *self.pos[:-1],
                ]
            elif self.turn == "down":
                self.pos = [
                    [self.pos[0][0], self.pos[0][1] + 10],
                    *self.pos[:-1],
                ]
        else:
            return [
                [max_w // 2 - 10, max_h // 2],
                [max_w // 2 - 20, max_h // 2],
                [max_w // 2 - 30, max_h // 2],
            ]

    def add_part(self) -> None:
        self.pos.insert(-1, self.pos[-1])
        self.__colors.append(choice(self.__colors))
