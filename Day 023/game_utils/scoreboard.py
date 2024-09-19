from turtle import Turtle

FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self._game_level = 1

        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    @property
    def game_level(self) -> int:
        return self._game_level

    @game_level.setter
    def game_level(self, new_level: int) -> None:
        self._game_level = new_level

    def increase_level(self, increment: int = 1) -> None:
        self.game_level += increment
        self.update_scoreboard()

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Level: {self.game_level}", font=FONT)
