#!/usr/bin/env python
from quiz import QUESTION_DATA, Question


def main() -> None:
    question_bank = [
        Question(question['text'], question['answer']) for
        question in QUESTION_DATA
    ]

    print(question_bank[0].text, question_bank[0].answer)


if __name__ == '__main__':
    main()
