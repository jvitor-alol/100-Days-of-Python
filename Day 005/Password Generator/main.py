#!/usr/bin/env python
import random

# Password Generator Project
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator(password_lenght: int, charset: list[str]) -> str:
    password = ""
    for _ in range(password_lenght):
        password += charset.pop(random.randint(0, len(charset) - 1))

    return password


def main() -> None:
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(
        input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    num_chars = nr_letters + nr_symbols + nr_numbers

    password_letters = [random.choice(LETTERS) for _ in range(nr_letters)]
    password_symbols = [random.choice(SYMBOLS) for _ in range(nr_symbols)]
    password_numbers = [random.choice(NUMBERS) for _ in range(nr_numbers)]
    charset = password_letters + password_numbers + password_symbols

    print("Your new password is:\n" + password_generator(num_chars, charset))


if __name__ == '__main__':
    main()
