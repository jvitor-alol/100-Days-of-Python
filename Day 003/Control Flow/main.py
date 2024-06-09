#!/usr/bin/env python
import argparse


def even_or_odd() -> None:
    #  Which number do you want to check?
    number = int(input())
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇

    if number % 2 == 0:
        print(f"This is an even number.")
    else:
        print(f"This is an odd number.")


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
    parse = argparse.ArgumentParser()
    parse.add_argument("-o", "--option", type=int,
                       choices=range(2), default=0, help="choose function")
    args = parse.parse_args()

    if args.option == 0:
        rollercoaster()
    if args.option == 1:
        even_or_odd()


if __name__ == '__main__':
    main()
