#!/usr/bin/env python
import sys
import os.path
from random import shuffle

from art import text2art
from unidecode import unidecode

from check_input import check_input


CIPHER_PATH = './key.txt'
ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4',
    '5', '6', '7', '8', '9', '0']


def cipher_key_generator() -> list[str]:
    cipher_key: list[str] = []

    if not os.path.isfile(CIPHER_PATH):
        shuffle(ALPHABET)
        cipher_key = ALPHABET
        with open(CIPHER_PATH, 'w', encoding='utf-8') as file:
            file.write(' '.join(cipher_key))
    else:
        with open(CIPHER_PATH, mode='r', encoding='utf-8') as file:
            content = file.readlines()
            cipher_key = content[0].strip().split(' ')

    return cipher_key


def caesar_cipher(direction: str, plain_text: str, shift: int,
                  cipher_key: list[str]) -> str:
    if direction == 'decode':
        shift *= -1

    cipher_text = []
    for char in plain_text:
        if char in cipher_key:
            shifted_index = (cipher_key.index(char) + shift) % len(cipher_key)
            cipher_text.append(cipher_key[shifted_index])
        else:
            cipher_text.append(char)

    return ''.join(cipher_text)


def main() -> None:
    print(text2art("Caesar Cipher"))

    key = cipher_key_generator()

    direction = check_input(
        "Type 'encode' to encrypt / 'decode' to decrypt: ",
        lambda x: x in ['encode', 'decode'])
    text = unidecode(input("Type your message: ").lower())
    shift = int(check_input("Type the shift number: ", lambda x: x.isdigit()))

    cipher_text = caesar_cipher(direction, text, shift, key)
    print(f"\n{direction.capitalize()}d message is:\n" + cipher_text)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
