#!/usr/bin/env python

def is_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True


def main() -> None:
    # Which year do you want to check?
    year = int(input())
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    if is_leap_year(year):
        print("Leap year")
    else:
        print("Not leap year")


if __name__ == '__main__':
    main()
