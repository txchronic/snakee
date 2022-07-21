from __future__ import annotations

from snake.snake import Snake
from food.food import Food
from ai.ai import Ai

import pygame as pg


class Game:
    def __init__(
        self,
        win_size=(640, 480),
        win_title="Snake",
        ai_type="euc",
        bg_color=pg.Color(254, 254, 254),
        sc_color=pg.Color(19, 21, 21),
        food_color=pg.Color(247, 44, 37),
        snake_colors=[pg.Color(88, 129, 87)],
    ) -> None:
        self.__state = True
        self.__score = 0
        self.__clock = pg.time.Clock()

        self.__bg_color, self.__sc_color = self.set_colors(bg_color, sc_color)
        self.__surface = self.set_surface(win_size, win_title)
        self.__max_w = self.__surface.get_width()
        self.__max_h = self.__surface.get_height()
        self.__snake = self.set_snake(snake_colors)
        self.__food = self.set_food(food_color)
        self.__ai = self.set_ai(ai_type)

    def set_ai(self, ai_type: str) -> None | Ai:
        ai = Ai(ai_type)

        if hasattr(self, "__ai"):
            self.__ai = ai
        else:
            return ai

    def set_colors(self, bg: pg.Color, sc: pg.Color) -> None | pg.Color:
        if hasattr(self, "__bg_color") and hasattr(self, "__sc_color"):
            self.__bg_color, self.__sc_color = bg, sc
        else:
            return bg, sc

    def set_surface(self, size: tuple, title: str) -> None | pg.Surface:
        scr = pg.display.set_mode(size)
        pg.display.set_caption(title)

        if hasattr(self, "__surface"):
            self.__surface = scr
        else:
            return scr

    def set_snake(self, colors: list[pg.Color]) -> None | Snake:
        snake = Snake(self.__max_w, self.__max_h, colors)

        if hasattr(self, "__snake"):
            self.__snake = snake
        else:
            return snake

    def set_food(self, color: pg.Color) -> None | Food:
        food = Food(self.__max_w, self.__max_h, self.__snake.pos, color)

        if hasattr(self, "__food"):
            self.__food = food
        else:
            return food

    def __check_rules(self) -> bool:
        if (
            self.__snake.pos[0] in self.__snake.pos[1:] or
            not(0 < self.__snake.pos[0][0] < self.__max_w) or
            not(0 < self.__snake.pos[0][1] < self.__max_h) or
            any([True for j in pg.event.get() if j.type == pg.QUIT])
        ):
            return False
        else:
            return True

    def __update_game(self) -> None:
        if self.__check_rules() is False:
            self.__state = False
        else:
            self.__surface.fill(self.__bg_color)

            # SCORE
            font = pg.font.SysFont(pg.font.match_font("Georgia"), 30)
            rend = font.render(f"{self.__score}", True, self.__sc_color)
            rect = rend.get_rect()
            rect.midtop = (self.__max_w // 2, 20)

            # SNAKE
            self.__snake.turn = self.__ai.gen(
                self.__snake, self.__food, self.__max_w, self.__max_h
            )
            self.__snake.move(self.__max_w, self.__max_h)

            # FOOD
            if self.__food.pos == self.__snake.pos[0]:
                self.__score += 1
                self.__snake.add_part()
                self.__food.move(self.__snake.pos, self.__max_w, self.__max_h)

            # VISUAL
            self.__surface.blit(rend, rect)
            self.__snake.draw(self.__surface)
            self.__food.draw(self.__surface)

            pg.display.flip()
            self.__clock.tick(25)

    def start_game(self) -> None:
        pg.init()

        while self.__state:
            self.__update_game()

        # pg.time.wait(10000)

        print(f"\nGAME OVER!\nFinal score: {self.__score}\n")
