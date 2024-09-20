import os


def get_invited_names(file_path: str) -> list[str]:
    if not os.path.exists(file_path):
        raise FileNotFoundError
    with open(file_path, mode='r', encoding='utf-8') as file:
        return file.readlines()


def read_template_letter(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError
    with open(file_path, mode='r', encoding='utf-8') as file:
        return file.read()


def write_invitation(content: str, person_name: str, save_path: str) -> None:
    person_name = person_name.strip()
    file_path = os.path.join(save_path, f"letter_for_{person_name}.txt")

    with open(file_path, mode='w', encoding='utf-8') as file:
        letter = content.replace("[name]", person_name)
        file.write(letter)
