def clean_text(text: str) -> str:
    """Remove line breaks and extra spaces."""
    return " ".join(text.split())


QUESTION_DATA = [
    {
        "text": "A slug's blood is green.",
        "answer": "True"
    },
    {
        "text": "The loudest animal is the African Elephant.",
        "answer": "False"
    },
    {
        "text": "Approximately one quarter of human bones are in the feet.",
        "answer": "True"
    },
    {
        "text":
        clean_text("""\
        The total surface area of a human lungs is the size of a football \
        pitch.
        """),
        "answer": "True"
    },
    {
        "text":
        clean_text("""
        In West Virginia, USA, if you accidentally hit an animal with your \
        car, you are free to take it home to eat.
        """),
        "answer": "True"
    },
    {
        "text":
        clean_text("""\
        In London, UK, if you happen to die in the House of Parliament, \
        you are entitled to a state funeral.
        """),
        "answer": "False"
    },
    {
        "text": "It is illegal to pee in the Ocean in Portugal.",
        "answer": "True"
    },
    {
        "text": "You can lead a cow down stairs but not up stairs.",
        "answer": "False"
    },
    {
        "text": "Google was originally called 'Backrub'.",
        "answer": "True"
    },
    {
        "text": "Buzz Aldrin's mother's maiden name was 'Moon'.",
        "answer": "True"
    },
    {
        "text":
        clean_text("""\
        No piece of square dry paper can be folded in half more than \
        7 times.
        """),
        "answer": "False"
    },
    {
        "text": "A few ounces of chocolate can kill a small dog.",
        "answer": "True"
    },
    {
        "text": "The average person walks the equivalent of three times "
                "around the world in a lifetime.",
        "answer": "True"
    },
    {
        "text": "The Mona Lisa was stolen from the Louvre in 1911.",
        "answer": "True"
    },
    {
        "text": "The unicorn is the national animal of Scotland.",
        "answer": "True"
    },
    {
        "text": "Honey never spoils.",
        "answer": "True"
    },
    {
        "text": "The Great Wall of China is visible from space.",
        "answer": "False"
    },
    {
        "text": "Octopuses have three hearts.",
        "answer": "True"
    },
    {
        "text": "Bananas grow on trees.",
        "answer": "False"
    },
    {
        "text": "Humans and dinosaurs coexisted.",
        "answer": "False"
    },
    {
        "text": "A group of flamingos is called a 'flamboyance'.",
        "answer": "True"
    },
    {
        "text": "Water makes up about 70% of the human body.",
        "answer": "True"
    },
    {
        "text": "Mount Everest is the tallest mountain in the world.",
        "answer": "True"
    },
    {
        "text": "Sharks are mammals.",
        "answer": "False"
    },
    {
        "text": "The human nose can detect over 1 trillion scents.",
        "answer": "True"
    },
    {
        "text": "Venus is the hottest planet in our solar system.",
        "answer": "True"
    },
    {
        "text": "Bats are blind.",
        "answer": "False"
    },
    {
        "text": "Light travels faster than sound.",
        "answer": "True"
    },
    {
        "text": "Humans have four blood types: A, B, AB, and O.",
        "answer": "True"
    },
    {
        "text": "An octopus can fit through any hole larger than its beak.",
        "answer": "True"
    }
]
