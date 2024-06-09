#!/usr/bin/env python
import argparse


def bmi_2() -> None:
    # Enter your height in meters e.g., 1.55
    height = float(input())
    # Enter your weight in kilograms e.g., 72
    weight = int(input())
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    bmi = weight / height ** 2
    message = "Your BMI is {}, you {}."

    if bmi < 18.5:
        print(message.format(bmi, "are underweight"))
    elif bmi < 25:
        print(message.format(bmi, "have a normal weight"))
    elif bmi < 30:
        print(message.format(bmi, "are slightly overweight"))
    elif bmi < 35:
        print(message.format(bmi, "are obese"))
    else:
        print(message.format(bmi, "are clinically obese"))


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
                       choices=range(3), default=0, help="choose function")
    args = parse.parse_args()

    if args.option == 0:
        rollercoaster()
    if args.option == 1:
        even_or_odd()
    if args.option == 2:
        bmi_2()


if __name__ == '__main__':
    main()
