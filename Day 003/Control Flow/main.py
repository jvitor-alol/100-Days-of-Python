#!/usr/bin/env python
import argparse


def rollercoaster() -> None:
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))
    if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age? "))
        if age >= 18:
            print("Your ticket costs $12.")
        elif age >= 12:
            print("Your ticket costs $7.")
        else:
            print("Your ticket costs $5.")
    else:
        print("Too bad, pipsqueak. 🤭")


def main() -> None:
    rollercoaster()


if __name__ == '__main__':
    main()
