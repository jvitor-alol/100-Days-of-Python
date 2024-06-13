#!/usr/bin/env python
import sys
import os.path
import argparse
from random import shuffle

from art import text2art
from unidecode import unidecode
from termcolor import colored

from check_input import check_input


CIPHER_PATH = './key.txt'
ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4',
    '5', '6', '7', '8', '9', '0']


def cipher_key_generator(filepath: str = CIPHER_PATH) -> list[str]:
    cipher_key: list[str] = []

    if not os.path.isfile(filepath):
        shuffle(ALPHABET)
        cipher_key = ALPHABET
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(' '.join(cipher_key))
    else:
        with open(filepath, mode='r', encoding='utf-8') as file:
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


def main(parse: argparse.ArgumentParser) -> None:
    print(text2art("Caesar Cipher"))

    args = parse.parse_args()
    key = cipher_key_generator(args.key)

    if args.mode:
        direction = args.mode
    else:
        direction = check_input(
            "Type 'encode' to encrypt / 'decode' to decrypt: ",
            lambda x: x in ['encode', 'decode'])

    if args.text:
        text = args.text.lower()
    else:
        text = unidecode(input("Type your message: ").lower())

    if args.shift:
        shift = args.shift
    else:
        shift = int(check_input(
            "Type the shift number: ", lambda x: x.isdigit()))

    cipher_text = caesar_cipher(direction, text, shift, key)
    print(f"\n{direction.capitalize()}d message is:")
    print(colored(cipher_text, "green", attrs=["blink"]))
    sys.exit()


if __name__ == '__main__':
    parse = argparse.ArgumentParser(
        description="""
        Encrypts or decrypts messages using the Caesar cipher method.""")

    parse.add_argument(
        '-m', '--mode', type=str, choices=['encode', 'decode'],
        help="Selects the cipher mode: "
        "'encode' to encrypt or 'decode' to decrypt.")
    parse.add_argument(
        '-s', '--shift', type=int,
        help="Specifies a number for the shift amount of the Caesar cipher.")
    parse.add_argument(
        '-t', '--text', type=str,
        help="Plain text message to encrypt or decrypt.")
    parse.add_argument(
        '-k', '--key', type=str, default='./key.txt',
        help="Path to cipher key in the system.")

    try:
        main(parse)
    except KeyboardInterrupt:
        sys.exit(1)
