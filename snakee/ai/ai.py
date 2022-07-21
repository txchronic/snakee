import numpy as np

from snake.snake import Snake
from food.food import Food


class Ai:
    def __init__(self, ai_type: str) -> None:
        self.__ai_type = ai_type

    def __gen_moves(self, s_pos: list) -> list:
        moves = [
            ["right", [s_pos[0][0] + 10, s_pos[0][1]]],
            ["left", [s_pos[0][0] - 10, s_pos[0][1]]],
            ["up", [s_pos[0][0], s_pos[0][1] - 10]],
            ["down", [s_pos[0][0], s_pos[0][1] + 10]]
        ]

        return moves

    def __euc(self, snake: Snake, food: Food, w: int, h: int) -> str:
        s_pos, f_pos = snake.pos, food.pos
        moves = self.__gen_moves(s_pos)

        moves = [
            [j[0], np.linalg.norm(abs(np.array(f_pos) - j[1]))]
            for j in moves
            if j[1] not in s_pos[1:] and (0 < j[1][0] < w and 0 < j[1][1] < h)
        ]

        moves = list(sorted(moves, key=lambda x: x[1]))

        if moves == []:
            return snake.turn
        else:
            return moves[0][0]

    def gen(self, snake: Snake, food: Food, max_w: int, max_h: int) -> str:
        if self.__ai_type == "euc":
            t = self.__euc(snake, food, max_w, max_h)

        return t
