import os
from random import shuffle

from termcolor import colored

from .question import Question


class QuizBrain:
    def __init__(self, question_bank: list[Question]) -> None:
        self._question_number: int = 0
        self._question_list = question_bank

    @property
    def question_number(self) -> int:
        return self._question_number

    @question_number.setter
    def question_number(self, number: int) -> None:
        if number < 0:
            raise ValueError("Invalid question number")
        self._question_number = number

    @property
    def question_list(self) -> list[Question]:
        return self._question_list

    @question_list.setter
    def question_list(self, question_bank: list[Question]) -> None:
        if not question_bank:
            raise ValueError("List cannot be empty")
        self._question_list = question_bank

    def next_question(self) -> Question:
        """Generate random next question

        Returns:
            Question: Return a question from questions list.
        """
        shuffle(self.question_list)
        self.question_number += 1

        return self.question_list.pop()

    def ask_question_and_score(self) -> int:
        """Asks a question to the player.

        Returns:
            int: Return 1 if player guessed right and 0 if they got it wrong.
        """
        current_question = self.next_question()
        number = str(self.question_number).zfill(3)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("************************************************************")
        guess = input(f"Q.{number}: {current_question.text} (True/False): ")

        if guess.lower() == current_question.answer.lower():
            print("You got it right!")
            point = 1
        else:
            print("That's wrong.")
            point = 0

        print(f"The correct answer was: {current_question.answer}.")
        return point

    def still_has_questions(self) -> bool:
        """Check if Quiz Brain still has more questions.

        Returns:
            bool: True if question list not empty, otherwise return False.
        """
        return self.question_list

    def display_game(self) -> None:
        """Display game on terminal screen."""
        score = 0

        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(
            "***************Let's play a quiz game!***************",
            'light_blue', attrs=['blink']))
        stop = input("\nPress anything to continue...")
        while self.still_has_questions() and stop != 'stop':
            score += self.ask_question_and_score()
            print(colored(
                f"\nYour current score is: [{score}/{self.question_number}]",
                "green"))
            stop = input("Press anything to continue...")

        def center_text(text, width) -> str:
            """Center text with especified width."""
            return f"#{text:^{width-2}}#"

        # Ending message
        width = 45
        border = "#" * width
        line_1 = center_text("You've completed the quiz!", width)
        line_2 = center_text(
            f"Your final score was: [{score}/{self.question_number}]", width)

        final_message = colored(
            f"""
            {border}
            {center_text("", width)}
            {line_1}
            {line_2}
            {center_text("", width)}
            {border}
            """,
            'red', attrs=['blink']
        )
        print('\n' + final_message)
