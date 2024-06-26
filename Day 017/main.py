#!/usr/bin/env python
import sys

from quiz import QUESTION_DATA, Question, QuizBrain


def main() -> None:
    question_bank = [
        Question(question['text'], question['answer']) for
        question in QUESTION_DATA
    ]

    quiz_brain = QuizBrain(question_bank)
    quiz_brain.display_game()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
