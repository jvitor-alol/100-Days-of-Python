class Question:
    def __init__(self, text: str, answer: str) -> None:
        self._text = text
        self._answer = answer

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        if len(new_text) < 10:
            raise ValueError("Question is too short")
        self._text = new_text

    @property
    def answer(self) -> bool:
        return self._answer

    @answer.setter
    def answer(self, new_answer: bool) -> None:
        if not isinstance(new_answer, bool):
            raise ValueError("Answer must be either true or false")
        self._answer = new_answer
